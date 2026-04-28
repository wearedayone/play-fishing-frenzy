#!/bin/bash
# Fishing Frenzy Agent — MCP Server Bootstrap
# Auto-installs Python dependencies on first run, then launches the server.
# Used as the MCP server command so users only need: npx skills add unchartedgg/play-fishing-frenzy

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_DIR="$SKILL_DIR/.venv"
SERVER="$SKILL_DIR/ff_agent/server.py"
REQUIREMENTS="$SKILL_DIR/requirements.txt"

# First run: create venv and install deps
if [ ! -f "$VENV_DIR/bin/python3" ]; then
    if ! command -v python3 &> /dev/null; then
        echo "ERROR: python3 not found. Install Python 3.10+ first." >&2
        exit 1
    fi
    python3 -m venv "$VENV_DIR" 2>/dev/null
    "$VENV_DIR/bin/pip" install -q -r "$REQUIREMENTS" 2>/dev/null
fi

# Deps updated: reinstall if requirements.txt is newer than the venv
if [ "$REQUIREMENTS" -nt "$VENV_DIR/.deps_installed" ]; then
    "$VENV_DIR/bin/pip" install -q -r "$REQUIREMENTS" 2>/dev/null
    touch "$VENV_DIR/.deps_installed"
fi

exec "$VENV_DIR/bin/python3" "$SERVER"
