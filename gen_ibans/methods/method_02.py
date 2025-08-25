"""
Method 02: Modulus 11 with weights [2,3,4,5,6,7,8,9,2] applied right-to-left over 9 payload digits.

Rules (same as method 24 variant):
- Digits 1..9 are payload; 10th is check.
- Weights repeating sequence: [2,3,4,5,6,7,8,9,2] from right to left.
- Sum S of digit*weight; r = S % 11.
- Check = 11 - r; if check == 10 -> invalid; if check == 11 -> 0.
- Valid if last digit equals computed check.
"""
from . import register, register_generator


def _compute_check_mod11_m02(payload: str) -> int | None:
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2]
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


@register("02")
def validate_method_02(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_digit_char = account[:9], account[9]
    expected = _compute_check_mod11_m02(payload)
    if expected is None:
        return False
    return (ord(check_digit_char) - 48) == expected


@register_generator("02")
def generate_account_method_02(blz: str, rng: __import__("random").Random) -> str:
    for _ in range(1000):
        payload_num = rng.randint(0, 999_999_999)
        payload = f"{payload_num:09d}"
        cd = _compute_check_mod11_m02(payload)
        if cd is not None:
            return payload + str(cd)
    return "0000000001"
