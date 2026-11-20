import pytest

from grades import letter_grade


def test_ninety_is_an_a():
    assert letter_grade(90) == "A"


def test_eighty_nine_is_a_b():
    assert letter_grade(89) == "B"


def test_below_sixty_fails():
    assert letter_grade(59) == "F"


def test_score_above_100_is_rejected():
    with pytest.raises(ValueError):
        letter_grade(101)


@pytest.mark.parametrize(
    "score, expected",
    [(0, "F"), (100, "A"), (60, "D"), (69, "D"), (70, "C")],
)
def test_boundaries(score, expected):
    assert letter_grade(score) == expected


def test_negative_score_is_rejected():
    with pytest.raises(ValueError):
        letter_grade(-1)
