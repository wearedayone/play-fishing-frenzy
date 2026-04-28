# Fishing Frenzy Agent — Quick Start Guide

## What This Is

An AI agent that plays [Fishing Frenzy](https://fishingfrenzy.co) autonomously. You type `/play-fishing-frenzy`, and it creates a wallet, catches fish, sells them, buys sushi, completes quests, and levels up — all on its own.

Works with Claude Code, Cursor, Cline, Windsurf, OpenClaw, and any MCP-compatible AI tool.

---

## Prerequisites

- **Python 3.10+** — check with `python3 --version`
- **An AI tool** with MCP support (Claude Code, Cursor, Cline, Windsurf, etc.)

---

## Install

```bash
npx skills add unchartedgg/play-fishing-frenzy
```

Restart your AI tool. Python dependencies install automatically on first run.

<details>
<summary>Alternative: clone manually</summary>

```bash
git clone https://github.com/unchartedgg/play-fishing-frenzy
cd play-fishing-frenzy/play-fishing-frenzy
bash scripts/bootstrap.sh
```
</details>

---

## Play

Open your AI tool and type:

```
/play-fishing-frenzy
```

### First Run

The agent will automatically:
1. Create a new Ethereum wallet (stored locally)
2. Register a guest game account via SIWE
3. Claim your daily reward
4. Open any starter chests
5. Start fishing

No wallet, no seed phrase, no crypto needed. Everything is handled.

### What You'll See

```
╔══════════════════════════════════════════════════╗
║  🎣 FISHING FRENZY AGENT                        ║
║  Strategy: BALANCED                              ║
╠══════════════════════════════════════════════════╣
║  👤 Agent_0x3e1C  ·  Lv.1                       ║
║  ⚡ Energy: 30/30    ████████████████████ 100%    ║
║  💰 Gold: 0         🏆 XP: 0                     ║
╚══════════════════════════════════════════════════╝

🎣 Cast #1  short_range ─── 🐟 Sardine ★ (+3 XP, 5g)
🎣 Cast #2  short_range ─── 🐟 Mackerel ★★ (+6 XP, 12g)
🎣 Cast #3  short_range ─── ❌ Fish escaped!
...
📦 SELL   Sold all fish → +89 gold
🛒 SHOP   Bought 1× Sushi (-500g) → ⚡ +5 energy
```

A session takes **5-10 minutes** (fishing cooldowns are ~10 seconds each).

### Strategies

```
/play-fishing-frenzy balanced    # Default — fish, sell, cook, quests, upgrades
/play-fishing-frenzy grind       # Max casts — short range, aggressive sushi buying
/play-fishing-frenzy risk        # High risk diving and NFT gameplay for rewards
```

---

## Customize

Edit **`CONFIG.md`** to tweak thresholds:

| Setting | Default | What It Does |
|---------|---------|-------------|
| `SUSHI_BUY_THRESHOLD` | 1500 | Buy sushi when gold exceeds this |
| `GOLD_RESERVE` | 1000 | Never spend below this gold level |
| `PREFERRED_RANGE` | auto | Force a fishing range or let agent decide |
| `MAX_SUSHI_PER_SESSION` | 3 | Cap sushi purchases per session |

Edit **`SKILL.md`** to change the agent's decision-making logic itself.

---

## What to Test

| Area | How to Test | What to Look For |
|------|------------|-----------------|
| First run | `/play-fishing-frenzy` on fresh install | Wallet created, account registered, fishing starts |
| Full loop | Let a session run to completion | Fish → sell → buy sushi → fish more → session summary |
| Strategies | `/play-fishing-frenzy grind` then `/play-fishing-frenzy risk` | Different behavior (range, sushi timing, cooking) |
| Error recovery | Interrupt mid-session, then `/play-fishing-frenzy` again | Agent re-authenticates and starts a new session |
| Config changes | Edit `CONFIG.md`, run `/play-fishing-frenzy` | Agent respects new thresholds |
| Daily rewards | Run `/play-fishing-frenzy` on consecutive days | Daily reward claimed once per day |

---

## Data & Privacy

- Wallet + auth stored locally at `~/.fishing-frenzy-agent/state.db`
- No external services contacted except the Fishing Frenzy game API
- Guest account — no email, no personal data
- Delete everything: `rm -rf ~/.fishing-frenzy-agent`

---

## Troubleshooting

**"Tool not found" or MCP errors:**
```bash
# Re-install the skill
npx skills add unchartedgg/play-fishing-frenzy
# Then restart your AI tool
```

**"No module named 'mcp'" or import errors:**
```bash
# Delete the venv to force a fresh dependency install on next run
rm -rf ~/.agents/skills/play-fishing-frenzy/.venv
# Then restart your AI tool — deps will reinstall automatically
```

**Agent seems stuck:**
- Fishing has a 10-second server cooldown between casts — this is normal
- Each cast also takes 3-6 seconds of simulated gameplay
- A batch of 10 casts takes ~2 minutes

---

## Report Issues

If something breaks or feels wrong, file a bug report:

**[Report a Bug](https://github.com/unchartedgg/play-fishing-frenzy/issues/new?template=bug_report.yml)**

The form will ask for your AI tool, Python version, OS, and a description of what went wrong. Copy-paste the agent output if you can — it helps a lot.
