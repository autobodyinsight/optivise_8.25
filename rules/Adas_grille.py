import re
from utils import normalize, suggest_if_missing

def rule_grille_adas(lines: list[str], seen: set[str]) -> tuple[str, list[str]] | None:
    """
    If any line mentions R&I or Replace + grille/grill, suggest ADAS calibrations.
    """
    action_keywords = ["r&i", "remove / install", "replace", "repl", "remove/replace"]
    grille_keywords = ["grille", "grill", "upper", "lower", "center"]

    for line in lines:
        norm = normalize(line)

        if any(kw in norm for kw in action_keywords) and any(part in norm for part in grille_keywords):
            suggestions = suggest_if_missing(
                lines,
                [
                    "360 camera calibration (if equipped)",
                    "adaptive cruise control calibration (if equipped)"
                ],
                seen
            )
            if suggestions:
                print(f"[ADAS GRILLE] ✅ Match on line: {line}")
                return ("ADAS GRILLE CHECK", suggestions)

    return None

def register():
    return [rule_grille_adas]