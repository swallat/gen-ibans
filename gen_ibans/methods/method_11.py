"""
Method 11 (in this project tests): Modulus 10 with repeating weights 3,7,1
applied right-to-left over the first 9 digits; the 10th is the check digit.

This aligns with tests expecting identical behavior to a Mod10 (3,7,1) scheme.
"""
from . import register, register_generator


def _compute_check_method_11(payload: str) -> int:
    weights = (3, 7, 1)
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i % 3]
        total += d * w
    return (10 - (total % 10)) % 10


@register("11")
def validate_method_11(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, last = account[:9], account[9]
    expected = _compute_check_method_11(payload)
    return (ord(last) - 48) == expected


@register_generator("11")
def generate_account_method_11(blz: str, rng: __import__("random").Random) -> str:
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _compute_check_method_11(payload)
    return payload + str(cd)
