# Fishing Frenzy Agent

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tools](https://img.shields.io/badge/MCP_tools-36-purple.svg)](#what-the-agent-can-do)
[![Fishing Frenzy](https://img.shields.io/badge/game-Fishing_Frenzy-orange.svg)](https://fishingfrenzy.co)

> An autonomous AI agent that plays [Fishing Frenzy](https://fishingfrenzy.co) — fishing, cooking, diving, quests, and economy optimization on the Ronin blockchain.

Works with any AI tool that supports [MCP](https://modelcontextprotocol.io) — Claude Code, Cursor, Cline, Windsurf, OpenClaw, and more. Install, run `/play-fishing-frenzy`, and your agent handles fishing, selling, cooking, quests, diving, and equipment management.

**The meta-game**: Customize the strategy in `SKILL.md` to optimize your agent's decision-making. Same tools, different strategies.

## Install

### Step 1: Get the code + dependencies

```bash
npx skills add wearedayone/fishing-frenzy-agent --all --global -y
pip3 install -r ~/.agents/skills/play-fishing-frenzy/requirements.txt
```

This installs the skill to every detected AI agent (Claude Code, Cursor, Cline, etc.) and installs Python dependencies.

<details>
<summary>Alternative: clone manually</summary>

```bash
git clone https://github.com/wearedayone/fishing-frenzy-agent
cd fishing-frenzy-agent
pip3 install -r requirements.txt
```
</details>

### Step 2: Register the MCP server for your tool

The agent uses an MCP server that exposes 36 game tools. Register it with your AI tool:

#### Claude Code

```bash
claude mcp add fishing-frenzy -- python3 ~/.agents/skills/play-fishing-frenzy/ff_agent/server.py
```

Or run the setup script (does the above + lets you pick a strategy):

```bash
bash ~/.claude/skills/play-fishing-frenzy/scripts/setup.sh
```

#### Cursor

Go to **Cursor Settings > MCP** and add:

```json
{
  "fishing-frenzy": {
    "command": "python3",
    "args": ["~/.agents/skills/play-fishing-frenzy/ff_agent/server.py"]
  }
}
```

#### Cline

Add to your MCP settings (`.cline/mcp_settings.json`):

```json
{
  "mcpServers": {
    "fishing-frenzy": {
      "command": "python3",
      "args": ["~/.agents/skills/play-fishing-frenzy/ff_agent/server.py"]
    }
  }
}
```

#### Windsurf

Add to your MCP config in Windsurf settings:

```json
{
  "fishing-frenzy": {
    "command": "python3",
    "args": ["~/.agents/skills/play-fishing-frenzy/ff_agent/server.py"]
  }
}
```

#### OpenClaw

```bash
openclaw mcp set fishing-frenzy '{"command":"python3","args":["~/.agents/skills/play-fishing-frenzy/ff_agent/server.py"]}'
```

#### Any other MCP-compatible tool

Point it at the server: `python3 ~/.agents/skills/play-fishing-frenzy/ff_agent/server.py` (stdio transport).

---

Restart your tool after registering. If you cloned instead of using `npx skills`, replace `~/.agents/skills/play-fishing-frenzy/` with your clone path.

## Play

Open your AI tool and type:

```
/play-fishing-frenzy
```

Your agent will:
1. Create a new wallet and guest account (first run only)
2. Claim daily rewards
3. Fish until energy is depleted
4. Sell fish for gold
5. Complete quests and cook sashimi
6. Buy sushi to refill energy and keep going
7. Display a session summary with stats

Choose a strategy:

```
/play-fishing-frenzy grind       # Max XP, aggressive sushi buying
/play-fishing-frenzy risk        # High risk diving and NFT gameplay for rewards
/play-fishing-frenzy balanced    # Default — even split across all activities
```

## What the Agent Can Do

| System | Tools | Description |
|--------|-------|-------------|
| Fishing | `fish`, `fish_batch` | Cast lines at short/mid/long range |
| Economy | `sell_all_fish`, `buy_item`, `use_item` | Sell catches, buy sushi, manage gold |
| Cooking | `get_recipes`, `cook`, `spin_cooking_wheel` | Cook sashimi, earn pearls |
| Quests | `claim_daily_reward`, `get_quests`, `claim_quest` | Daily rewards, quest completion |
| Equipment | `equip_rod`, `repair_rod`, `collect_pet_fish` | Rod management, pet collection |
| Diving | `buy_diving_ticket`, `dive` | Grid-based diving game (Level 30+) |
| Upgrades | `get_accessories`, `upgrade_accessory` | Spend upgrade points on accessories |
| Stats | `get_leaderboard`, `get_session_stats` | Rankings, performance tracking |

36 tools total across all game systems.

## Demo

When you run `/play-fishing-frenzy`, your agent displays a live game dashboard:

```
╔══════════════════════════════════════════════════╗
║  🎣 FISHING FRENZY AGENT                        ║
║  Strategy: BALANCED                              ║
╠══════════════════════════════════════════════════╣
║  👤 FishBot_0x3e1C  ·  Lv.25                    ║
║  ⚡ Energy: 22/30    ██████████████░░░░░ 73%     ║
║  💰 Gold: 1,075     🏆 XP: 12,450               ║
╚══════════════════════════════════════════════════╝

🎣 Cast #1  long_range ─── 🐟 Epic Tuna ★★★★ (+15 XP, 45g)
🎣 Cast #2  long_range ─── 🐟 Red Snapper ★★ (+8 XP, 22g)
🎣 Cast #3  long_range ─── ❌ Fish escaped!
🎣 Cast #4  mid_range  ─── 🐟 Golden Koi ★★★★★ (+25 XP, 80g)  🆕 NEW FISH!
🎣 Cast #5  short_range ── 🐟 Common Sardine ★ (+3 XP, 5g)

📦 SELL   Sold all fish → +238 gold (total: 1,313)
✅ QUEST  "Catch 5 fish" complete → +100 gold, +50 XP
🛒 SHOP   Bought 1× Sushi (-500g) → ⚡ +5 energy
⬆️ UPGRADE Rod Handle Lv.0 → Lv.1 (1.25% energy save chance)

╔══════════════════════════════════════════════════╗
║  📊 SESSION COMPLETE                             ║
╠══════════════════════════════════════════════════╣
║  🐟 Fish Caught:  47         ⏱️  Duration: ~8m   ║
║  💰 Gold Earned:  2,340      💰 Gold Now: 3,415  ║
║  ⭐ XP Earned:    890        📈 Level: 25 → 27   ║
║  ⚡ Energy Used:  30/30      🍣 Sushi Used: 2    ║
╠══════════════════════════════════════════════════╣
║  🏆 Best Catch: Golden Koi ★★★★★ (80g)          ║
║  📊 Efficiency: 78g/energy                       ║
╚══════════════════════════════════════════════════╝
```

## How It Works

```
fishing-frenzy-agent/
├── SKILL.md                  ← Strategy brain (edit this to compete!)
├── ff_agent/
│   ├── server.py             ← MCP server — 36 game action tools
│   ├── auth.py               ← Privy SIWE wallet auth (Ronin chain)
│   ├── api_client.py         ← REST API wrapper
│   ├── fishing_client.py     ← Fishing session protocol
│   ├── diving_client.py      ← WebSocket diving protocol
│   ├── state.py              ← SQLite state persistence
│   └── wallet.py             ← Ethereum wallet management
├── scripts/
│   ├── setup.sh              ← One-command install
│   └── status.py             ← Agent status check
├── requirements.txt
└── LICENSE                   ← MIT
```

**SKILL.md** teaches your AI agent how to play — the game loop, decision framework, and strategy templates. Edit this file to change how your agent plays.

**MCP Server** (`ff_agent/server.py`) exposes game actions as tools that Claude calls autonomously.

## Customizing Your Strategy

Edit `SKILL.md` to change your agent's behavior:

- Adjust fishing range preferences
- Change sushi buying thresholds
- Prioritize cooking over fishing
- Set energy management rules
- Change accessory upgrade priority

The three built-in strategies (balanced, grind, risk) are starting points. Create your own by modifying the decision rules.

## Data Storage

All data is stored locally at `~/.fishing-frenzy-agent/`:

- `state.db` — wallet, auth tokens, session history
- No data is sent anywhere except the Fishing Frenzy game API

## Requirements

- Python 3.10+
- Any MCP-compatible AI tool ([Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [Cursor](https://cursor.com), [Cline](https://cline.bot), [Windsurf](https://windsurf.com), [OpenClaw](https://github.com/openclaw/openclaw), etc.)

## For Developers

This repo is also a reference implementation for building autonomous game agents with MCP.

### Architecture

```
SKILL.md (strategy layer)
    ↓ reads
AI Agent (Claude, Cursor, etc.)
    ↓ calls
MCP Server (ff_agent/server.py) — 36 tools via stdio
    ↓ wraps
API Client + Fishing Client + Diving Client
    ↓ talks to
Fishing Frenzy API + Ronin Blockchain (SIWE auth, wallet ops)
```

### Extending Strategies

1. Edit the strategy templates in `SKILL.md` or add new ones
2. Adjust thresholds in `CONFIG.md`
3. The MCP tools stay the same — strategy is pure prompt engineering

### Tests

```bash
python3 -m pytest tests/ --skip-live -v    # Offline suite (no API calls)
python3 -m pytest tests/ -v                # Full suite (needs live connection)
```

## License

MIT — see [LICENSE](LICENSE).
