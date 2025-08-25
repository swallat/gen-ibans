"""
Method 08 (Bundesbank): Modulus 10 with alternating weights 2,1 applied right-to-left over the
first 9 digits; the 10th digit is the check digit. Calculation like Method 00, but only for
account numbers from 60 000 upwards (threshold rule).

Spec essentials (derived from Bundesbank text):
- Same computation as Method 00 (Luhn-like): weights from right to left over digits 1..9 are
  2,1,2,1,2,1,2,1,2. For products >= 10, take cross-sum (equivalently: subtract 9 when doubling
  digits 5..9). Sum, take units digit u = sum % 10. Check digit = (10 - u) % 10.
- Threshold rule: "Die Berechnung erfolgt wie bei Verfahren 00, jedoch erst ab der Kontonummer 60 000."
  Interpretation used here (common in Bundesbank specs): If the 10-digit account number interpreted
  as an integer (ignoring leading zeros) is less than 60000, the checksum is not applied and such
  accounts are considered valid by format alone. From 60000 upwards, the checksum per Method 00 must
  match.

Notes:
- BLZ is not used by this method.
- Account numbers are exactly 10 digits (ASCII '0'..'9'). Leading zeros allowed.
"""
from . import register, register_generator


def _compute_check_mod10_w21(payload9: str) -> int:
    """Compute Method 00-style check digit for 9-digit payload using weights 2,1 from right.

    Args:
        payload9: exactly 9 ASCII digits (0-9)
    Returns:
        The check digit (0..9).
    """
    total = 0
    for i, ch in enumerate(reversed(payload9)):
        d = ord(ch) - 48
        if (i % 2) == 0:
            prod = d * 2
            if prod >= 10:
                prod -= 9
        else:
            prod = d
        total += prod
    return (10 - (total % 10)) % 10


def _numeric_value(acc: str) -> int:
    """Return integer value of an account string ignoring leading zeros."""
    # Safe because caller ensures digits
    i = 0
    n = 0
    # Manual to avoid int() overhead; but int(acc.lstrip('0') or '0') would also work.
    while i < len(acc) and acc[i] == '0':
        i += 1
    for j in range(i, len(acc)):
        n = n * 10 + (ord(acc[j]) - 48)
    return n


@register("08")
def validate_method_08(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    # Threshold check on the full 10-digit account number value
    if _numeric_value(account) < 60000:
        return True
    payload, check_char = account[:9], account[9]
    expected = _compute_check_mod10_w21(payload)
    return (ord(check_char) - 48) == expected


@register_generator("08")
def generate_account_method_08(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid account for Method 08.

    We prefer generating numbers >= 60000 (where checksum applies) to ensure meaningful
    check-digit construction. We draw a 9-digit payload uniformly, compute the check digit,
    and if the resulting 10-digit value is below 60000, we retry.
    """
    for _ in range(1000):
        payload_num = rng.randint(0, 999_999_999)
        payload = f"{payload_num:09d}"
        cd = _compute_check_mod10_w21(payload)
        account = payload + str(cd)
        if _numeric_value(account) >= 60000:
            assert validate_method_08(blz, account)
            return account
    # Fallback: construct a deterministic account >= 60000
    payload = "000006000"
    cd = _compute_check_mod10_w21(payload)
    account = payload + str(cd)
    # Ensure it's >= 60000 (it is) and valid
    assert validate_method_08(blz, account)
    return account
