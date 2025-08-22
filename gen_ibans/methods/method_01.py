"""
Method 01: Modulus 11 with weights [2..10] applied right-to-left over 9 payload digits.

Rules:
- Digits 1..9 are payload; 10th is the check digit.
- Weights sequence from right to left: [2,3,4,5,6,7,8,9,10].
- Sum products, r = sum % 11; check = 11 - r; if check == 10 -> invalid; if check == 11 -> 0.
- Valid if last digit equals computed check.
"""
from . import register


def _compute_check_mod11_w2_to_10(payload: str) -> int | None:
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i % len(weights)]
        total += d * w
    r = total % 11
    check = 11 - r
    if check == 10:
        return None
    if check == 11:
        return 0
    return check


@register("01")
def validate_method_01(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, last = account[:9], account[9]
    expected = _compute_check_mod11_w2_to_10(payload)
    if expected is None:
        return False
    return (ord(last) - 48) == expected
