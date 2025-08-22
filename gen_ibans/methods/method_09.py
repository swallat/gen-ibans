"""
Method 09: Modulus 11 with repeating weights 2..7 (right to left).

Assumed interpretation (common Bundesbank method):
- Use the first 9 digits as payload; the 10th digit is the check digit.
- Multiply payload digits (from right to left) by weights repeating [2, 3, 4, 5, 6, 7].
- Sum the products, take sum % 11.
- Compute check = 11 - (sum % 11); if check == 10 -> invalid; if check == 11 -> 0.
- Valid if last digit equals computed check.

Note: This replaces the prior permissive placeholder with a concrete, commonly used variant
of method 09. If your bank list uses a different 09 definition, adjust weights/rules accordingly.
"""
from . import register


def _compute_check_mod11_weights_2_to_7(payload: str) -> int | None:
    weights = [2, 3, 4, 5, 6, 7]
    total = 0
    # Apply from right to left across 9 payload digits
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i % len(weights)]
        total += d * w
    remainder = total % 11
    check = 11 - remainder
    if check == 10:
        return None  # invalid according to rule
    if check == 11:
        return 0
    return check


@register("09")
def validate_method_09(blz: str, account: str) -> bool:
    # Preconditions
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_digit_char = account[:9], account[9]
    expected = _compute_check_mod11_weights_2_to_7(payload)
    if expected is None:
        return False
    return (ord(check_digit_char) - 48) == expected
