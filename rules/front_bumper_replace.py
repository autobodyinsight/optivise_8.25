import re
from utils import normalize, suggest_if_missing

REPLACE_PHRASES = [
    "repl bumper", "replace bumper",
    "repl bumper cover", "replace bumper cover",
    "repl fascia", "replace fascia",
    "repl bumper cover assy", "replace bumper cover assy",
    "repl bumper cover assembly", "replace bumper cover assembly"
]

SUGGESTIONS = [
    "flex additive",
    "adhesion promoter",
    "static neutralization",
    "mask for texture",
    "mask for two tone",
    "ADD for parking sensors",
    "ADD for auto park",
    "ADD if required - transfer parking sensor brackets",
    "IF LKQ ADD DETRIM TO ALL BUMPER COMPONENTS"
]

def front_bumper_replace_rule(lines, seen):
    print("🚀 front_bumper_replace_rule fired")
    bumper_context_detected = False
    phrase_detected = False
    section_lines = []

    for line in lines:
        norm = normalize(line)
        section_lines.append(line)
        print(f"[FRONT BUMPER REPLACE RULE] Scanning line: {norm}")

        # ✅ Looser context detection: any line mentioning "front bumper"
        if "front bumper" in norm:
            bumper_context_detected = True
            print("[FRONT BUMPER REPLACE RULE] ✅ Context match: front bumper")

        # ✅ Phrase-level detection
        for phrase in REPLACE_PHRASES:
            if phrase in norm:
                phrase_detected = True
                print(f"[FRONT BUMPER REPLACE RULE] ✅ Phrase detected: {phrase}")

    if bumper_context_detected and phrase_detected:
        missing = suggest_if_missing(section_lines, SUGGESTIONS, seen)
        if missing:
            print(f"[FRONT BUMPER REPLACE RULE] 🎯 Suggestions returned: {missing}")
            return ("FRONT BUMPER REPLACEMENT CHECK", missing)

    return None

def register():
    print("✅ front_bumper_replace_rule registered")
    return [front_bumper_replace_rule]