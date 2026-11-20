"""Tuition fee calculation for the Student Services App."""

from dataclasses import dataclass
from enum import Enum

RATE_PER_HOUR = 350
HIGH_FEE_LIMIT = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_SURCHARGE = 150


class StudentType(Enum):
    """Kinds of student, with the numeric codes used by the legacy code."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


SHARE_OF_FEE = {
    StudentType.REGULAR: 1,
    StudentType.STAFF_CHILD: 0.5,
    StudentType.SCHOLARSHIP: 0,
}


@dataclass(frozen=True)
class Course:
    """One course, measured in credit hours."""

    hours: int


def tuition_fee(courses, kind, summer=False, discount=0, extras=()):
    """Return the tuition fee for one student."""
    total = sum(c.hours * RATE_PER_HOUR * SHARE_OF_FEE[kind] for c in courses)
    if total > HIGH_FEE_LIMIT:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_SURCHARGE
    return total - discount + sum(extras)


def fee_report(fee, kind):
    """Return report text instead of printing it."""
    lines = [f"{kind.name.title()} fee: {fee}"]
    if fee > HIGH_FEE_LIMIT:
        lines.append("High fee")
    return "\n".join(lines)


def process_all(students):
    """Return {name: fee} for every student, scholarship included."""
    return {
        st["name"]: tuition_fee(st["courses"], st["type"], st["summer"])
        for st in students
    }
