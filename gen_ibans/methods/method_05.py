"""
Method 05 (Bundesbank in this repository's tests): Luhn (Modulus 10) over the
first 9 digits; the 10th digit is the check digit.

Spec as per tests:
- Apply the Luhn doubling scheme to the 9 payload digits (positions 1..9):
  starting from the rightmost payload digit, double every second digit. If a
  doubled value exceeds 9, subtract 9. Sum all contributions.
- Prüfziffer (digit 10) = (10 - (sum % 10)) % 10.

Notes:
- BLZ is not used by this method.
- Leading zeros in the payload are allowed; account numbers are 10 digits overall.
- This matches tests/methods/test_method_05.py which defines the expected logic.
"""
from . import register, register_generator


def _compute_luhn_check_digit(payload9: str) -> int:
    """Compute the Luhn check digit for a 9-digit payload.

    Args:
        payload9: exactly 9 ASCII digits (0-9)
    Returns:
        The check digit (0..9).
    """
    total = 0
    for i, ch in enumerate(reversed(payload9)):
        d = ord(ch) - 48
        if i % 2 == 0:
            total += d
        else:
            dd = d * 2
            if dd > 9:
                dd -= 9
            total += dd
    return (10 - (total % 10)) % 10


@register("05")
def validate_method_05(blz: str, account: str) -> bool:
    """Validate a 10-digit account number according to Luhn over first 9 digits."""
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_char = account[:9], account[9]
    expected = _compute_luhn_check_digit(payload)
    return (ord(check_char) - 48) == expected


@register_generator("05")
def generate_account_method_05(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account for Method 05 (Luhn over first 9 digits).

    Draw a 9-digit payload uniformly (including leading zeros), compute the
    deterministic check digit, and append it.
    """
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _compute_luhn_check_digit(payload)
    return payload + str(cd)
