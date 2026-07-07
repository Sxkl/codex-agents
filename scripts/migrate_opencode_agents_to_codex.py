#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


@dataclass
class AgentDoc:
    source_path: Path
    source_label: str
    name: str
    target_name: str
    description: str
    metadata: Dict[str, object]
    body: str


FRONTMATTER_BOUNDARY = "---"


def parse_frontmatter(text: str) -> Tuple[Dict[str, object], str]:
    if not text.startswith(FRONTMATTER_BOUNDARY):
        return {}, text

    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        return {}, text

    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONTMATTER_BOUNDARY:
            end_index = i
            break

    if end_index is None:
        return {}, text

    frontmatter_lines = lines[1:end_index]
    body = "\n".join(lines[end_index + 1 :]).lstrip("\n")
    data: Dict[str, object] = {}
    current_map_key: str | None = None

    for raw_line in frontmatter_lines:
        if not raw_line.strip():
            continue
        if raw_line.startswith("  ") and current_map_key:
            stripped = raw_line.strip()
            if ":" not in stripped:
                continue
            key, value = stripped.split(":", 1)
            nested = data.setdefault(current_map_key, {})
            if isinstance(nested, dict):
                nested[key.strip()] = parse_scalar(value.strip())
            continue

        current_map_key = None
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            data[key] = {}
            current_map_key = key
        else:
            data[key] = parse_scalar(value)

    return data, body


def parse_scalar(value: str) -> object:
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def read_agent(path: Path, prefix: str, public_safe: bool) -> AgentDoc:
    raw = path.read_text(encoding="utf-8")
    metadata, body = parse_frontmatter(raw)
    name = str(metadata.get("name") or path.stem).strip()
    target_name = f"{prefix}{name}" if prefix else name
    description = str(metadata.get("description") or f"Migrated from OpenCode agent {name}.").strip()
    source_label = path.name if public_safe else str(path)
    return AgentDoc(
        source_path=path,
        source_label=source_label,
        name=name,
        target_name=target_name,
        description=description,
        metadata=metadata,
        body=body.rstrip() + "\n",
    )


def humanize_name(name: str) -> str:
    parts = re.split(r"[-_]+", name)
    return " ".join(part.capitalize() for part in parts if part)


def first_heading(body: str) -> str | None:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def shorten(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def build_skill_markdown(agent: AgentDoc) -> str:
    meta_lines: List[str] = []
    for key in ("mode",):
        if key in agent.metadata:
            meta_lines.append(f"- Original `{key}`: `{agent.metadata[key]}`")

    tools = agent.metadata.get("tools")
    if isinstance(tools, dict) and tools:
        enabled = [name for name, allowed in tools.items() if allowed is True]
        if enabled:
            meta_lines.append("- Original `tools`: " + ", ".join(f"`{tool}`" for tool in enabled))

    permission = agent.metadata.get("permission")
    if isinstance(permission, dict) and permission:
        enabled_permissions = [
            f"`{name}={value}`" for name, value in permission.items() if str(value).strip()
        ]
        if enabled_permissions:
            meta_lines.append("- Original `permission`: " + ", ".join(enabled_permissions))

    metadata_block = ""
    if meta_lines:
        metadata_block = "## Migration Metadata\n\n" + "\n".join(meta_lines) + "\n\n"

    source_path = agent.source_label
    return (
        "---\n"
        f'name: {yaml_quote(agent.target_name)}\n'
        f'description: {yaml_quote(agent.description)}\n'
        "metadata:\n"
        f'  source: {yaml_quote("opencode")}\n'
        f'  original_name: {yaml_quote(agent.name)}\n'
        f'  original_file: {yaml_quote(source_path)}\n'
        "---\n\n"
        f"# {agent.name}\n\n"
        f"Migrated from `{source_path}`.\n\n"
        "This skill is intended to run on the current Codex session default model. Do not pin vendor-specific models when adapting it further.\n\n"
        f"{metadata_block}"
        f"{agent.body}"
    )


def build_openai_yaml(agent: AgentDoc) -> str:
    display_name = first_heading(agent.body) or humanize_name(agent.name)
    short_description = shorten(agent.description, 64)
    prompt_summary = shorten(agent.description, 96)
    default_prompt = f"Use ${agent.target_name} to help with: {prompt_summary}"
    return (
        "interface:\n"
        f"  display_name: {yaml_quote(display_name)}\n"
        f"  short_description: {yaml_quote(short_description)}\n"
        f"  default_prompt: {yaml_quote(default_prompt)}\n"
        "policy:\n"
        "  allow_implicit_invocation: true\n"
    )


def write_skill(output_root: Path, agent: AgentDoc) -> None:
    skill_dir = output_root / agent.target_name
    agents_dir = skill_dir / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(build_skill_markdown(agent), encoding="utf-8")
    (agents_dir / "openai.yaml").write_text(build_openai_yaml(agent), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate OpenCode agents to Codex skills.")
    parser.add_argument("--source", required=True, help="OpenCode agents directory")
    parser.add_argument("--output", required=True, help="Codex skills output directory")
    parser.add_argument(
        "--prefix",
        default="opencode-",
        help="Prefix to add to generated Codex skill names to avoid collisions",
    )
    parser.add_argument(
        "--public-safe",
        action="store_true",
        help="Omit absolute source paths from generated metadata and manifests",
    )
    args = parser.parse_args()

    source_dir = Path(args.source).expanduser().resolve()
    output_dir = Path(args.output).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    docs = [read_agent(path, args.prefix, args.public_safe) for path in sorted(source_dir.glob("*.md"))]
    for doc in docs:
        write_skill(output_dir, doc)

    manifest = {
        "source": source_dir.name if args.public_safe else str(source_dir),
        "output": output_dir.name if args.public_safe else str(output_dir),
        "count": len(docs),
        "skills": [doc.target_name for doc in docs],
    }
    (output_dir / "migration-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
