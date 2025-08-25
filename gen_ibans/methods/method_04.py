"""
Method 04: Simple Modulus 10 checksum on the first 9 digits (same as method 10).

Rules:
- Digits 1..9 are payload; 10th is the check digit.
- Compute sum of the 9 payload digits; check digit = sum % 10.
- Valid if last digit equals computed check.
"""
from . import register, register_generator


@register("04")
def validate_method_04(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    payload, last = account[:9], account[9]
    total = sum(ord(ch) - 48 for ch in payload)
    expected = total % 10
    return (ord(last) - 48) == expected


@register_generator("04")
def generate_account_method_04(blz: str, rng: __import__("random").Random) -> str:
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    total = sum(ord(ch) - 48 for ch in payload)
    cd = total % 10
    return payload + str(cd)
