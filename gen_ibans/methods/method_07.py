"""
Method 07: Modulus 11 with repeating weights 2..7 (right to left) over first 9 digits.

Rules (same as method 02 regarding remainder handling):
- First 9 digits are payload; 10th is check digit.
- Apply weights [2,3,4,5,6,7] from right-to-left, repeating.
- Sum products; r = sum % 11; check = 11 - r.
- If check == 10 -> invalid; if check == 11 -> 0. Valid if equals last digit.
"""
from . import register, register_generator


def _compute_check_mod11_w2_to_7(payload: str) -> int | None:
    weights = [2, 3, 4, 5, 6, 7]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i % len(weights)]
        total += d * w
    r = total % 11
    check = 11 - r
    if check == 10:
        return None
    if check == 11:
        return 0
    return check


@register("07")
def validate_method_07(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_digit_char = account[:9], account[9]
    expected = _compute_check_mod11_w2_to_7(payload)
    if expected is None:
        return False
    return (ord(check_digit_char) - 48) == expected


@register_generator("07")
def generate_account_method_07(blz: str, rng: __import__("random").Random) -> str:
    for _ in range(1000):
        payload_num = rng.randint(0, 999_999_999)
        payload = f"{payload_num:09d}"
        cd = _compute_check_mod11_w2_to_7(payload)
        if cd is not None:
            account = payload + str(cd)
            assert validate_method_07(blz, account)
            return account
    # Fallback: choose a deterministic payload that yields valid cd
    payload = "000000000"
    cd = _compute_check_mod11_w2_to_7(payload)
    account = payload + str(cd)
    assert validate_method_07(blz, account)
    return account
