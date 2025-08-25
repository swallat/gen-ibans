"""
Method 03 (Bundesbank): Modulus 10 with alternating weights 2,1 applied right-to-left
over the first 9 digits; the 10th digit is the check digit.

Spec essentials ("Die Berechnung erfolgt wie bei Verfahren 01"):
- Weights from right to left over the payload (digits 1..9): 2,1,2,1,2,1,2,1,2.
- Compute the sum of products (no cross-sum of product digits; unlike Method 00).
- Prüfziffer = 10 minus the units digit of the sum; if that yields 10, the check digit is 0.
  Compactly: check = (10 - (sum % 10)) % 10.

Notes:
- BLZ is not used by this method.
- Leading zeros in the payload are allowed; account numbers are 10 digits overall.
"""
from . import register, register_generator


def _compute_check_mod10_w21_no_crosssum(payload9: str) -> int:
    """Compute Method 03 check digit for a 9-digit payload using weights 2,1 from right.

    Calculation follows Method 01 style: sum raw products, then (10 - (sum % 10)) % 10.
    No cross-sum reduction is applied to two-digit products.
    """
    total = 0
    # Apply weights from right to left: 2,1,2,1,... over 9 digits
    for i, ch in enumerate(reversed(payload9)):
        d = ord(ch) - 48
        if (i % 2) == 0:
            # weight 2 on the rightmost payload digit, then every other
            prod = d * 2
        else:
            # weight 1
            prod = d
        total += prod
    u = total % 10
    return (10 - u) % 10


@register("03")
def validate_method_03(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_char = account[:9], account[9]
    expected = _compute_check_mod10_w21_no_crosssum(payload)
    return (ord(check_char) - 48) == expected


@register_generator("03")
def generate_account_method_03(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account for Method 03 (Mod10 w/ weights 2,1; no cross-sum).

    Draw a 9-digit payload uniformly (including leading zeros), compute the
    deterministic check digit, and append it.
    """
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _compute_check_mod10_w21_no_crosssum(payload)
    return payload + str(cd)
