"""
Method 01 (Bundesbank): Modulus 10 with repeating weights 3,7,1 applied right-to-left over
the first 9 digits; the 10th digit is the check digit.

Spec essentials:
- Weights from right to left over the payload (digits 1..9): 3,7,1,3,7,1,3,7,1.
- Multiply each digit by its weight, sum the products; only the units digit of the sum matters.
- Prüfziffer = 10 minus the units digit; if that yields 10, the check digit is 0.
  Compactly: check = (10 - (sum % 10)) % 10.

Notes:
- BLZ is not used by this method.
- Leading zeros in the payload are allowed; account numbers are 10 digits overall.
"""
from . import register, register_generator


def _compute_check_mod10_w371(payload9: str) -> int:
    """Compute Method 01 check digit for a 9-digit payload using weights 3,7,1 (right-to-left).

    Args:
        payload9: exactly 9 ASCII digits (0-9)
    Returns:
        The check digit (0..9).
    """
    weights = (3, 7, 1)
    total = 0
    for i, ch in enumerate(reversed(payload9)):
        d = ord(ch) - 48
        w = weights[i % 3]
        total += d * w
    u = total % 10
    return (10 - u) % 10


@register("01")
def validate_method_01(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_char = account[:9], account[9]
    expected = _compute_check_mod10_w371(payload)
    return (ord(check_char) - 48) == expected


@register_generator("01")
def generate_account_method_01(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account for Method 01 (Mod10 w/ weights 3,7,1).

    Draw a 9-digit payload uniformly (including leading zeros), compute the
    deterministic check digit, and append it.
    """
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _compute_check_mod10_w371(payload)
    return payload + str(cd)
