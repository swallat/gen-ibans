"""
Method 13: Modulus 10 (Luhn) on first 9 digits, last is check digit.

Assumed interpretation (common in Bundesbank set):
- Validate 10-digit account numbers.
- Compute Luhn sum on the first 9 digits (right to left, double every second digit; if >9, subtract 9).
- Check digit = (10 - (sum % 10)) % 10. Valid if it equals the 10th digit.
"""
from . import register, register_generator


def _luhn_check_digit(payload: str) -> int:
    total = 0
    # Starting from rightmost payload digit, double every second
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        if i % 2 == 0:
            # first from right (position 1) not doubled; double every second digit
            total += d
        else:
            dd = d * 2
            if dd > 9:
                dd -= 9
            total += dd
    return (10 - (total % 10)) % 10


@register("13")
def validate_method_13(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_digit_char = account[:9], account[9]
    expected = _luhn_check_digit(payload)
    return (ord(check_digit_char) - 48) == expected


@register_generator("13")
def generate_account_method_13(blz: str, rng: __import__("random").Random) -> str:
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _luhn_check_digit(payload)
    return payload + str(cd)
