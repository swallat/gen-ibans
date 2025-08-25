"""
Method 11 (Bundesbank): Modulus 11 with weights 2..10 (right-to-left, modified),
over the first 9 digits; the 10th digit is the check digit.

The calculation proceeds like Method 06 (modified Mod11), but with weights
2,3,4,5,6,7,8,9,10 applied from right to left across the 9-digit payload. The
special rule is adjusted per spec: when the computed result would be 10 (i.e.,
remainder r == 1 so 11 - r == 10), use 9 instead of 0.

Rules summary:
- Compute total = sum(d_i * w_i) with weights 2..10 right-to-left over payload.
- r = total % 11
- If r == 0 -> check digit = 0
- If r == 1 -> check digit = 9  (modified compared to Method 06/10)
- Else -> check digit = 11 - r

Notes:
- BLZ is not used by this method.
- Leading zeros are allowed; account numbers are exactly 10 digits, with last digit as check digit.
"""
from . import register, register_generator


def _compute_check_method_11_mod11_w2to10(payload9: str) -> int:
    """Compute Method 11 check digit for a 9-digit payload using weights 2..10.

    Args:
        payload9: exactly 9 ASCII digits (0-9)
    Returns:
        The check digit (0..9) according to modified Mod11 where r==1 -> 9.
    """
    weights = (2, 3, 4, 5, 6, 7, 8, 9, 10)
    total = 0
    for i, ch in enumerate(reversed(payload9)):
        d = ord(ch) - 48
        w = weights[i]  # i ranges 0..8
        total += d * w
    r = total % 11
    if r == 0:
        return 0
    if r == 1:
        return 9  # Modified: when 11 - r would be 10, use 9 instead of 0
    return 11 - r


@register("11")
def validate_method_11(blz: str, account: str) -> bool:
    """Validate a 10-digit account number according to Bundesbank Method 11.

    Args:
        blz: Bankleitzahl (unused for this method).
        account: 10-digit account string, the 10th digit is the check digit.
    Returns:
        True iff the account conforms to Method 11.
    """
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_char = account[:9], account[9]
    expected = _compute_check_method_11_mod11_w2to10(payload)
    return (ord(check_char) - 48) == expected


@register_generator("11")
def generate_account_method_11(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account number for Method 11.

    Strategy: sample a 9-digit payload uniformly (including leading zeros),
    compute the deterministic check digit per Method 11, and append it.
    """
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _compute_check_method_11_mod11_w2to10(payload)
    acc = payload + str(cd)
    # Defensive check to ensure generator complies with validator
    assert validate_method_11(blz, acc)
    return acc
