from dataclasses import dataclass

SIBLING_DISCOUNT_RATE = 0.10
TAX_RATE = 0.14


@dataclass
class SiblingPolicy:
    has_sibling_discount: bool = False

    def apply(self, amount: float) -> float:
        if not self.has_sibling_discount:
            return amount
        return round(amount * (1 - SIBLING_DISCOUNT_RATE), 2)


def calculate_subtotal(items: list[tuple[str, float, int]]) -> float:
    return sum(price * qty for _, price, qty in items)


def generate_invoice(items: list[tuple[str, float, int]], sibling_policy: SiblingPolicy | None = None) -> dict:
    policy = sibling_policy or SiblingPolicy()
    subtotal = calculate_subtotal(items)
    after_policy = policy.apply(subtotal)
    tax = round(after_policy * TAX_RATE, 2)
    total = round(after_policy + tax, 2)
    return {
        "subtotal": subtotal,
        "after_policy": after_policy,
        "tax": tax,
        "total": total,
    }
