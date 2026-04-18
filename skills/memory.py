import os
from pathlib import Path

MEMORY_DIR = Path(__file__).parent.parent / "memory"

TOOL_DEFINITIONS = [
    {
        "name": "read_memory_file",
        "description": "Read a memory file (strategy, trade_log, research_log, or weekly_review).",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "Filename relative to memory/ dir (e.g. 'trade_log.md', 'strategy.md')",
                }
            },
            "required": ["filename"],
        },
    },
    {
        "name": "write_memory_file",
        "description": "Overwrite a memory file with new content.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["filename", "content"],
        },
    },
    {
        "name": "append_memory_file",
        "description": "Append content to an existing memory file.",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["filename", "content"],
        },
    },
    {
        "name": "list_memory_files",
        "description": "List all available memory files.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
]


def _safe_path(filename: str) -> Path:
    path = (MEMORY_DIR / filename).resolve()
    if not str(path).startswith(str(MEMORY_DIR.resolve())):
        raise ValueError(f"Access denied: {filename}")
    return path


def read_memory_file(filename: str) -> str:
    try:
        path = _safe_path(filename)
        if not path.exists():
            return f"File not found: {filename}"
        return path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading {filename}: {e}"


def write_memory_file(filename: str, content: str) -> str:
    try:
        path = _safe_path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return f"Written {len(content)} chars to {filename}"
    except Exception as e:
        return f"Error writing {filename}: {e}"


def append_memory_file(filename: str, content: str) -> str:
    try:
        path = _safe_path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a", encoding="utf-8") as f:
            f.write(content)
        return f"Appended {len(content)} chars to {filename}"
    except Exception as e:
        return f"Error appending to {filename}: {e}"


def list_memory_files() -> str:
    try:
        files = sorted(MEMORY_DIR.rglob("*.md"))
        return "\n".join(str(f.relative_to(MEMORY_DIR)) for f in files)
    except Exception as e:
        return f"Error listing files: {e}"


HANDLERS = {
    "read_memory_file": read_memory_file,
    "write_memory_file": write_memory_file,
    "append_memory_file": append_memory_file,
    "list_memory_files": list_memory_files,
}
