#!/usr/bin/env python3
"""Interactive first-setup questionnaire for Fishing Frenzy Agent.

Walks new players through 4 questions that configure CONFIG.md.
Each question includes a brief explanation of the game mechanic.
"""

import os
import re
import sys


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), "CONFIG.md")


def ask(question: str, options: list[tuple[str, str]], default: int = 1) -> int:
    """Ask a multiple-choice question and return the chosen option index (1-based).

    Args:
        question: The question text.
        options: List of (label, description) tuples.
        default: Default choice (1-based).
    """
    print(f"\n  {question}\n")
    for i, (label, desc) in enumerate(options, 1):
        marker = " (default)" if i == default else ""
        print(f"    {i}) {label}{marker}")
        print(f"       {desc}")
    print()

    while True:
        try:
            raw = input(f"  Choice [1-{len(options)}, default={default}]: ").strip()
            if raw == "":
                return default
            choice = int(raw)
            if 1 <= choice <= len(options):
                return choice
            print(f"  Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print(f"  Please enter a number between 1 and {len(options)}.")
        except (EOFError, KeyboardInterrupt):
            print("\n  Setup cancelled.")
            sys.exit(0)


def update_config(key: str, value: str):
    """Update a key in CONFIG.md using regex substitution."""
    if not os.path.exists(CONFIG_PATH):
        print(f"  WARNING: CONFIG.md not found at {CONFIG_PATH}")
        return

    with open(CONFIG_PATH, "r") as f:
        content = f.read()

    # Match the key at the start of a line (inside code blocks)
    pattern = rf"^({re.escape(key)}:\s*).*$"
    replacement = rf"\g<1>{value}"
    new_content, count = re.subn(pattern, replacement, content, flags=re.MULTILINE)

    if count == 0:
        print(f"  WARNING: Could not find '{key}' in CONFIG.md")
        return

    with open(CONFIG_PATH, "w") as f:
        f.write(new_content)


def main():
    print()
    print("  ══════════════════════════════════════════")
    print("  🎣 Fishing Frenzy — Setup Your Preferences")
    print("  ══════════════════════════════════════════")

    # ── Q1: Strategy / Goal ──────────────────────────────────
    q1 = ask(
        "What's your main goal?\n"
        "  There are many ways to play and you can tailor this later.",
        [
            ("Balanced progression",
             "Moderate balance between fishing, cooking, diving, and collecting."),
            ("Level up fishing",
             "Max casts, aggressive sushi usage, selling fish for gold."),
            ("Risk to win",
             "High risk diving and NFT gameplay with potential to win rewards."),
        ],
        default=1,
    )
    strategy_map = {1: "balanced", 2: "grind", 3: "risk"}
    strategy = strategy_map[q1]
    update_config("STRATEGY", strategy)

    # Set strategy-specific defaults
    defaults = {
        "grind":    {"sushi": 800,  "reserve": 500,  "max_sushi": 0, "cook": "false", "risk": "moderate"},
        "balanced": {"sushi": 1500, "reserve": 1000, "max_sushi": 3, "cook": "true",  "risk": "moderate"},
        "risk":     {"sushi": 1000, "reserve": 500,  "max_sushi": 3, "cook": "false", "risk": "aggressive"},
    }
    strat = defaults[strategy]
    update_config("SUSHI_BUY_THRESHOLD", str(strat["sushi"]))
    update_config("GOLD_RESERVE", str(strat["reserve"]))
    update_config("MAX_SUSHI_PER_SESSION", str(strat["max_sushi"]))

    # ── Q2: Fishing style ────────────────────────────────────
    q2 = ask(
        "What is your fishing style?\n"
        "  Longer range costs more energy but gives higher rarity fish.\n"
        "  Bait improves odds but costs gold.",
        [
            ("Long range with big bait",
             "3 energy/cast, best chance at rare fish."),
            ("Medium range with medium bait",
             "2 energy/cast, good balance of rarity and volume."),
            ("Short range, no bait",
             "1 energy/cast, maximum casts per session."),
            ("Flexible — agent decides",
             "Agent picks range based on strategy and bait availability."),
        ],
        default=4,
    )
    fishing_map = {1: "long", 2: "medium", 3: "short", 4: "auto"}
    update_config("FISHING_STRATEGY", fishing_map[q2])

    # ── Q3: Fish disposal ────────────────────────────────────
    q3 = ask(
        "What do you want to do with fish?\n"
        "  Deciding what to do with fish is a key strategy.",
        [
            ("Balanced approach",
             "Cook matching recipes, collect rare fish, sell the rest."),
            ("Sell for gold",
             "Sell everything immediately for maximum gold income."),
            ("Cook for sushi and sashimi",
             "Cook matching recipes first, then sell the remainder."),
            ("Hold for now",
             "Keep fish in inventory — decide later."),
        ],
        default=1,
    )
    disposal_map = {
        1: ("sell_all", "true"),   # balanced: cook + collect + sell
        2: ("sell_all", "false"),  # sell all raw
        3: ("sell_all", "true"),   # cook first, sell remainder
        4: ("hold",     "false"),  # hold everything
    }
    fish_disposal, cook_before_sell = disposal_map[q3]
    update_config("FISH_DISPOSAL", fish_disposal)
    update_config("COOK_BEFORE_SELL", cook_before_sell)

    # ── Q4: Diving style ─────────────────────────────────────
    q4 = ask(
        "What is your diving style?\n"
        "  Finding coral in diving = rewards. Finding 2 whirlpools = death.",
        [
            ("Conservative",
             "Surface as soon as there is a sign of danger."),
            ("Moderate",
             "Balanced risk — push a bit but play it safe overall."),
            ("Aggressive",
             "Keep diving for maximum rewards."),
        ],
        default={"conservative": 1, "moderate": 2, "aggressive": 3}.get(strat["risk"], 2),
    )
    risk_map = {1: "conservative", 2: "moderate", 3: "aggressive"}
    update_config("DIVE_RISK", risk_map[q4])

    # ── Summary ──────────────────────────────────────────────
    disposal_labels = {1: "balanced (cook + collect + sell)", 2: "sell all", 3: "cook first", 4: "hold"}
    print()
    print("  ══════════════════════════════════════════")
    print(f"  ✅ Preferences saved to CONFIG.md")
    print()
    print(f"    Strategy:       {strategy}")
    print(f"    Fishing style:  {fishing_map[q2]}")
    print(f"    Fish disposal:  {disposal_labels[q3]}")
    print(f"    Dive risk:      {risk_map[q4]}")
    print()
    print("  You can edit CONFIG.md anytime to fine-tune these values.")
    print("  ══════════════════════════════════════════")
    print()


if __name__ == "__main__":
    main()
