"""Convert numeric scores to letter grades."""

MIN_SCORE = 0
MAX_SCORE = 100
GRADE_BOUNDARIES = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]


def letter_grade(score):
    """Return the letter grade for a score between 0 and 100."""
    if not MIN_SCORE <= score <= MAX_SCORE:
        raise ValueError(f"score must be between {MIN_SCORE} and {MAX_SCORE}")
    for minimum, letter in GRADE_BOUNDARIES:
        if score >= minimum:
            return letter
    return "F"
