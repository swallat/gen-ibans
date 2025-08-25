"""
Method 06 (Bundesbank): Modulus 11 with repeating weights 2,3,4,5,6,7 (right-to-left),
over the first 9 digits; the 10th digit is the check digit.

Spec essentials (translated/condensed):
- Multiply the digits of the account number from right to left with weights
  2,3,4,5,6,7,2,3,... (i.e., repeating 2..7) across the payload (digits 1..9).
- Sum the products, divide by 11; take the remainder r.
- The check digit is 11 - r. Special rules:
  - If r == 1, the result 10 contributes only its ones place, i.e., check digit = 0.
  - If r == 0 (no remainder), the check digit is also 0.
- Position 10 is the check digit.

Notes:
- BLZ is not used by this method.
- Leading zeros in the payload are allowed; account numbers are exactly 10 digits.

Examples from spec: 94012341, 5073321010 (note: examples may be shown without left-padding;
this implementation expects 10 digits overall with the last digit as the check digit).
"""
from . import register, register_generator


def _compute_check_mod11_w2to7(payload9: str) -> int:
    """Compute Method 06 check digit for a 9-digit payload using weights 2..7 (right-to-left).

    Args:
        payload9: exactly 9 ASCII digits (0-9)
    Returns:
        The check digit (0..9) according to the modified Mod11 rule.
    """
    weights = (2, 3, 4, 5, 6, 7)
    total = 0
    # Apply weights from right to left over the 9 payload digits
    for i, ch in enumerate(reversed(payload9)):
        d = ord(ch) - 48
        w = weights[i % 6]
        total += d * w
    r = total % 11
    if r == 0:
        return 0
    if r == 1:
        # 11 - 1 = 10; per spec only the ones digit (0) is used
        return 0
    return 11 - r


@register("06")
def validate_method_06(blz: str, account: str) -> bool:
    """Validate a 10-digit account number according to Bundesbank Method 06.

    Args:
        blz: Bankleitzahl (unused for this method).
        account: 10-digit account string, the 10th digit is the check digit.
    Returns:
        True iff the account conforms to Method 06.
    """
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_char = account[:9], account[9]
    expected = _compute_check_mod11_w2to7(payload)
    return (ord(check_char) - 48) == expected


@register_generator("06")
def generate_account_method_06(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account number for Method 06.

    Strategy: sample a 9-digit payload uniformly (including leading zeros),
    compute the deterministic check digit per Method 06, and append it.
    """
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _compute_check_mod11_w2to7(payload)
    return payload + str(cd)
