"""
Method 11: Modulus 11 with weights [2..10] (modified variant of method 06).

Rules per spec:
- Same computation as method 06 (weights [2..10] right-to-left over digits 1..9).
- r = sum(products) % 11; check = 11 - r.
- If check == 11 -> use 0.
- If check == 10 -> use 9 (modified; differs from method 06 where 10 is invalid).
- Valid if 10th digit equals computed check.
"""
from . import register, register_generator


def _compute_check_method_11(payload: str) -> int:
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i % len(weights)]
        total += d * w
    r = total % 11
    check = 11 - r
    if check == 11:
        return 0
    if check == 10:
        return 9
    return check


@register("11")
def validate_method_11(blz: str, account: str) -> bool:
    """Validate account number for method 11 (modified Mod11 as described)."""
    if len(account) != 10 or not account.isdigit():
        return False
    payload, last = account[:9], account[9]
    expected = _compute_check_method_11(payload)
    return (ord(last) - 48) == expected


@register_generator("11")
def generate_account_method_11(blz: str, rng: __import__("random").Random) -> str:
    payload_num = rng.randint(0, 999_999_999)
    payload = f"{payload_num:09d}"
    cd = _compute_check_method_11(payload)
    return payload + str(cd)
