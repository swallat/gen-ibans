"""
Method 17: Modulus 10 (Luhn) on first 9 digits; 10th is check digit.

Notes:
- Several Bundesbank methods use Luhn; method 17 is implemented here as the
  standard Luhn variant (same computation as methods 05/13 in this codebase).
- Validate 10-digit numbers; compute check over the first 9 digits.
- Check digit = (10 - (sum % 10)) % 10, where sum uses doubled every second
  digit from the right (subtract 9 if doubling yields > 9).
"""
from . import register, register_generator


def _luhn_check_digit(payload: str) -> int:
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        if i % 2 == 0:
            total += d
        else:
            dd = d * 2
            if dd > 9:
                dd -= 9
            total += dd
    return (10 - (total % 10)) % 10


@register("17")
def validate_method_17(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, check_digit_char = account[:9], account[9]
    expected = _luhn_check_digit(payload)
    return (ord(check_digit_char) - 48) == expected


@register_generator("17")
def generate_account_method_17(blz: str, rng: __import__("random").Random) -> str:
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _luhn_check_digit(payload)
    return payload + str(cd)
