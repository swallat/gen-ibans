"""
Method 13: Modulus 10 with weights [2,1,2,1,2,1] over base number in positions 2..7.

Spec highlights:
- Relevant six-digit base number is in positions 2 to 7 (1-based indexing from the left).
- The check digit is at position 8.
- The two-digit subaccount (positions 9 and 10) is not part of the calculation.
- If the first calculation yields an error (i.e., does not match the given check digit),
  it is recommended to repeat the calculation by assuming the subaccount is "00":
  shift the existing account number two positions to the left (discarding former pos 9 and 10)
  and set positions 9 and 10 to "00"; then repeat the same calculation.

Computation:
- Apply weights [2,1,2,1,2,1] left-to-right on digits at positions 2..7.
- For each product d*w, if product >= 10, sum its digits (equiv. product - 9 for w=2 cases).
- Sum S; computed check digit = (10 - (S % 10)) % 10.
- Valid if computed check digit equals digit at position 8.
"""
from . import register, register_generator


def _mod10_weighted_2_1(digits: str) -> int:
    """Compute Mod10 check digit for a 6-digit string using weights [2,1,2,1,2,1] left-to-right."""
    weights = [2, 1, 2, 1, 2, 1]
    total = 0
    for ch, w in zip(digits, weights):
        d = ord(ch) - 48
        prod = d * w
        if prod >= 10:
            prod = (prod // 10) + (prod % 10)  # sum digits
        total += prod
    return (10 - (total % 10)) % 10


def _calc_on_account(acc: str) -> int:
    base = acc[1:7]  # positions 2..7
    return _mod10_weighted_2_1(base)


@register("13")
def validate_method_13(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    # First calculation on given layout
    expected = _calc_on_account(account)
    if (ord(account[7]) - 48) == expected:
        return True
    # Fallback attempt: shift two left and set subaccount to "00"
    shifted = account[2:10] + "00"
    expected2 = _calc_on_account(shifted)
    return (ord(shifted[7]) - 48) == expected2


@register_generator("13")
def generate_account_method_13(blz: str, rng: __import__("random").Random) -> str:
    # Choose arbitrary first digit (position 1) and two-digit subaccount
    a1 = rng.randint(0, 9)
    base_num = rng.randint(0, 999_999)
    base = f"{base_num:06d}"
    c = _mod10_weighted_2_1(base)
    sub_num = rng.randint(0, 99)
    sub = f"{sub_num:02d}"
    return f"{a1}{base}{c}{sub}"
