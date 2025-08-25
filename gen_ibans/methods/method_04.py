"""
Method 04: Modulus 11 with weights [2,3,4,5,6,7,2,3,4] applied right-to-left over 9 payload digits.

Spec (per Bundesbank; calculation like Method 02):
- Account number is 10 digits: first 9 are payload, 10th is the check digit.
- Apply weights right-to-left on the 9 payload digits: 2,3,4,5,6,7,2,3,4.
- Sum S = Σ(d_i * w_i). Let r = S % 11.
- Check digit c = 11 - r.
  * If c == 10 -> invalid (no valid check digit).
  * If c == 11 -> use 0 as check digit.
- Valid iff last digit equals computed check digit.

Notes:
- BLZ is not part of the calculation for this method.
"""
from . import register, register_generator


def _compute_check_mod11_m04(payload: str) -> int | None:
    """Compute check digit for Method 04 from a 9-digit payload.

    Returns an int 0..9 if valid; returns None if the result would be 10 (invalid per spec).
    """
    weights = [2, 3, 4, 5, 6, 7, 2, 3, 4]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i]
        total += d * w
    r = total % 11
    c = 11 - r
    if c == 10:
        return None
    if c == 11:
        return 0
    return c


@register("04")
def validate_method_04(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_digit_char = account[:9], account[9]
    expected = _compute_check_mod11_m04(payload)
    if expected is None:
        return False
    return (ord(check_digit_char) - 48) == expected


@register_generator("04")
def generate_account_method_04(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account for Method 04.

    Strategy: uniformly sample a 9-digit payload (including leading zeros),
    compute the check digit. If the calculation yields the invalid value 10,
    resample. Probability of rejection is 1/11, so expected retries ~1.1.

    Includes a deterministic fallback that always yields a valid number.
    """
    for _ in range(1000):
        payload_num = rng.randint(0, 999_999_999)
        payload = f"{payload_num:09d}"
        cd = _compute_check_mod11_m04(payload)
        if cd is not None:
            account = payload + str(cd)
            assert validate_method_04(blz, account)
            return account
    # Fallback: payload all zeros -> S=0 => r=0 => c=11->0
    payload = "000000000"
    cd = _compute_check_mod11_m04(payload)
    account = payload + str(cd)
    assert validate_method_04(blz, account)
    return account
