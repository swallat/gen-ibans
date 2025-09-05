# Method A4 (Bundesbank): Composite method with four variants per specification.
# Summary of variants (10-digit account, last digit usually check digit except var.4 case a):
# - Variant 1: Modulus 11, weights 2,3,4,5,6,7 applied from right to left over positions 4..9.
#   Check digit at position 10. Calculation follows Method 06 rules (r in {0,1} -> 0 else 11-r).
# - Variant 2: Modulus 7, same positions/weights; check digit P = (7 - (sum % 7)) mod 7 (with 0 when remainder 0).
# - Variant 3: Only for accounts with "99" in positions 3 and 4. Modulus 11 over positions 5..9,
#   weights 2..6 (right-to-left), check at position 10; same Method 06 rules.
# - Variant 4: If variants above fail (or for XX99XXXXXX: after Var.3), apply the weighting and
#   calculation of Method 93 (without enforcing UU/AA segment constraints):
#   Case a) positions 1..5 payload (right-to-left weights 2..6), check at pos 6; Mod 11 then Mod 7.
#   Case b) positions 5..9 payload (right-to-left weights 2..6), check at pos 10; Mod 11 then Mod 7.
# Notes:
# - BLZ is not used by these variants.
# - Input must be exactly 10 ASCII digits.
from __future__ import annotations

from typing import Iterable
import random

from . import register, register_generator


def _sum_weighted_right_to_left(digits: Iterable[int], weights: tuple[int, ...]) -> int:
    # Sum of products applying weights from right to left over the provided digits.
    ws = weights
    total = 0
    for i, d in enumerate(reversed(list(digits))):
        total += d * ws[i % len(ws)]
    return total


def _check_digit_mod11_from_sum(total: int) -> int:
    # Method 06 style check digit from a sum for modulus 11.
    r = total % 11
    if r in (0, 1):
        return 0
    return 11 - r


def _check_digit_mod7_from_sum(total: int) -> int:
    r = total % 7
    if r == 0:
        return 0
    return 7 - r


def _digits10(acc: str) -> list[int]:
    return [ord(ch) - 48 for ch in acc]


def _variant1_valid(digs: list[int]) -> bool:
    # Positions 4..9 (1-based) => indices 3..8
    total = _sum_weighted_right_to_left(digs[3:9], (2, 3, 4, 5, 6, 7))
    expected = _check_digit_mod11_from_sum(total)
    return digs[9] == expected


def _variant2_valid(digs: list[int]) -> bool:
    total = _sum_weighted_right_to_left(digs[3:9], (2, 3, 4, 5, 6, 7))
    expected = _check_digit_mod7_from_sum(total)
    return digs[9] == expected


def _variant3_valid(digs: list[int]) -> bool:
    # Positions 5..9 => indices 4..8
    total = _sum_weighted_right_to_left(digs[4:9], (2, 3, 4, 5, 6))
    expected = _check_digit_mod11_from_sum(total)
    return digs[9] == expected


def _method93_case_a_valid(digs: list[int], use_mod7: bool = False) -> bool:
    # K = positions 1..5 (indices 0..4), P at pos 6 (index 5)
    total = _sum_weighted_right_to_left(digs[0:5], (2, 3, 4, 5, 6))
    expected = _check_digit_mod7_from_sum(total) if use_mod7 else _check_digit_mod11_from_sum(total)
    return digs[5] == expected


def _method93_case_b_valid(digs: list[int], use_mod7: bool = False) -> bool:
    # K = positions 5..9 (indices 4..8), P at pos 10 (index 9)
    total = _sum_weighted_right_to_left(digs[4:9], (2, 3, 4, 5, 6))
    expected = _check_digit_mod7_from_sum(total) if use_mod7 else _check_digit_mod11_from_sum(total)
    return digs[9] == expected


def _variant4_valid(digs: list[int]) -> bool:
    # Try Method 93 logic: Mod 11 first, then Mod 7; try both cases a and b.
    if _method93_case_a_valid(digs, use_mod7=False):
        return True
    if _method93_case_b_valid(digs, use_mod7=False):
        return True
    if _method93_case_a_valid(digs, use_mod7=True):
        return True
    if _method93_case_b_valid(digs, use_mod7=True):
        return True
    return False


@register("A4")
def validate_method_A4(blz: str, account: str) -> bool:
    # Validate a 10-digit account number according to Bundesbank Method A4.
    if len(account) != 10 or not account.isdigit():
        return False
    digs = _digits10(account)

    if account[2:4] == "99":
        if _variant3_valid(digs):
            return True
        return _variant4_valid(digs)
    else:
        if _variant1_valid(digs):
            return True
        if _variant2_valid(digs):
            return True
        return _variant4_valid(digs)


@register_generator("A4")
def generate_account_method_A4(blz: str, rng: random.Random) -> str:
    # Generate a valid 10-digit account number for Method A4 (variants 1 and 3)
    def _gen_variant1() -> str:
        # Build digits d1..d10; compute d10 as mod11(Method06) over d4..d9
        d = [0] * 10
        # Pick d1..d9 randomly, ensuring positions 3..4 are not '99' together
        d[0] = rng.randrange(10)
        d[1] = rng.randrange(10)
        while True:
            d[2] = rng.randrange(10)
            d[3] = rng.randrange(10)
            if not (d[2] == 9 and d[3] == 9):
                break
        for i in range(4, 9):
            d[i] = rng.randrange(10)
        total = _sum_weighted_right_to_left(d[3:9], (2, 3, 4, 5, 6, 7))
        d[9] = _check_digit_mod11_from_sum(total)
        return "".join(str(x) for x in d)

    def _gen_variant3() -> str:
        # Force positions 3..4 to '99'; compute P at pos 10 via mod11 over d5..d9
        d = [0] * 10
        d[0] = rng.randrange(10)
        d[1] = rng.randrange(10)
        d[2] = 9
        d[3] = 9
        for i in range(4, 9):
            d[i] = rng.randrange(10)
        total = _sum_weighted_right_to_left(d[4:9], (2, 3, 4, 5, 6))
        d[9] = _check_digit_mod11_from_sum(total)
        return "".join(str(x) for x in d)

    if rng.random() < 0.2:
        return _gen_variant3()
    return _gen_variant1()
