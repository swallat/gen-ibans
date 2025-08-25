"""
Method 00 (Bundesbank): Modulus 10 with alternating weights 2,1 applied right-to-left over the
first 9 digits; the 10th digit is the check digit (Luhn-like method).

Spec (essentials):
- Weights from right to left over the payload (digits 1..9): 2,1,2,1,2,1,2,1,2.
- For each product >= 10, take the cross sum (equivalently: product - 9 for 2*d when d>=5).
- Sum all, take the units digit (sum % 10). The check digit is 10 minus the units digit.
- If the subtraction yields 10, the check digit is 0. Compactly: check = (10 - (sum % 10)) % 10.

Examples (left-padded to 10 digits as per usual Bundesbank convention):
- 9290701  -> 0009290701 (payload 000929070) -> check 1.
- 539290858 -> 0539290858 (payload 053929085) -> check 8.
"""
from . import register, register_generator


def _compute_check_mod10_w21(payload9: str) -> int:
    """Compute Method 00 check digit for 9-digit payload using weights 2,1 from right.

    Args:
        payload9: exactly 9 ASCII digits (0-9)
    Returns:
        The check digit (0..9).
    """
    total = 0
    # Apply weights from right to left: 2,1,2,1,... over 9 digits
    for i, ch in enumerate(reversed(payload9)):
        d = ord(ch) - 48
        if (i % 2) == 0:
            # weight 2 on the rightmost payload digit, then every other
            prod = d * 2
            # Cross sum for two-digit products (equivalent to subtracting 9 when >=10)
            if prod >= 10:
                prod -= 9
        else:
            # weight 1
            prod = d
        total += prod
    # Units digit
    u = total % 10
    # Prüfziffer: 10 - u, but 10 -> 0
    return (10 - u) % 10


@register("00")
def validate_method_00(blz: str, account: str) -> bool:
    """Validate a 10-digit account number using Bundesbank Method 00.

    The BLZ is not used by this method; validation depends only on the account digits.
    """
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_char = account[:9], account[9]
    expected = _compute_check_mod10_w21(payload)
    return (ord(check_char) - 48) == expected


@register_generator("00")
def generate_account_method_00(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account for Method 00.

    - Draw a 9-digit payload uniformly (including leading zeros).
    - Compute the deterministic check digit and append.
    """
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _compute_check_mod10_w21(payload)
    return payload + str(cd)
