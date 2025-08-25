"""
Method 10 (Bundesbank): Modulus 11 with weights 2..10 (right-to-left, modified),
over the first 9 digits; the 10th digit is the check digit. The calculation
proceeds like Method 06, but with weights 2,3,4,5,6,7,8,9,10 (no repetition),
applied from right to left to the 9-digit payload.

Spec essentials (translated/condensed):
- Multiply the digits of the account number from right to left with weights
  2,3,4,5,6,7,8,9,10 across the payload (digits 1..9).
- Sum the products, divide by 11; take the remainder r.
- The check digit is 11 - r. Modified Mod11 special rules as in Method 06:
  - If r == 1, the result 10 contributes only its ones place -> check digit = 0.
  - If r == 0 (no remainder), the check digit is also 0.
- Position 10 is the check digit.

Notes:
- BLZ is not used by this method.
- Leading zeros in the payload are allowed; account numbers are exactly 10 digits.
- Example test account numbers from prompt (interpreted with left-padding to
  10 digits): 0012345008, 0087654008 both validate under this method.
"""
from . import register, register_generator


def _compute_check_mod11_w2to10(payload9: str) -> int:
    """Compute Method 10 check digit for a 9-digit payload using weights 2..10.

    Args:
        payload9: exactly 9 ASCII digits (0-9)
    Returns:
        The check digit (0..9) according to the modified Mod11 rule (like Method 06).
    """
    # Weights for the 9 payload digits, applied from right to left
    weights = (2, 3, 4, 5, 6, 7, 8, 9, 10)
    total = 0
    # Apply weights from right to left over the 9 payload digits
    for i, ch in enumerate(reversed(payload9)):
        d = ord(ch) - 48
        w = weights[i]  # i ranges 0..8
        total += d * w
    r = total % 11
    if r == 0:
        return 0
    if r == 1:
        # 11 - 1 = 10; per spec only the ones digit (0) is used
        return 0
    return 11 - r


@register("10")
def validate_method_10(blz: str, account: str) -> bool:
    """Validate a 10-digit account number according to Bundesbank Method 10.

    Args:
        blz: Bankleitzahl (unused for this method).
        account: 10-digit account string, the 10th digit is the check digit.
    Returns:
        True iff the account conforms to Method 10.
    """
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_char = account[:9], account[9]
    expected = _compute_check_mod11_w2to10(payload)
    return (ord(check_char) - 48) == expected


@register_generator("10")
def generate_account_method_10(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account number for Method 10.

    Strategy: sample a 9-digit payload uniformly (including leading zeros),
    compute the deterministic check digit per Method 10, and append it.
    """
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _compute_check_mod11_w2to10(payload)
    acc = payload + str(cd)
    # Defensive check to ensure generator complies with validator
    assert validate_method_10(blz, acc)
    return acc
