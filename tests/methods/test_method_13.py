# MIT License
#
# Tests for Bundesbank method 13 per supplied spec:
# - Base digits at positions 2..7 (6 digits)
# - Check digit at position 8
# - Positions 9..10 (subaccount) are excluded
# - If initial calc fails, retry after shifting two left and setting subaccount to "00"

from gen_ibans.methods.method_13 import validate_method_13


def compute_check_base_2_1(base6: str) -> int:
    weights = [2, 1, 2, 1, 2, 1]
    total = 0
    for ch, w in zip(base6, weights):
        d = ord(ch) - 48
        prod = d * w
        if prod >= 10:
            prod = (prod // 10) + (prod % 10)
        total += prod
    return (10 - (total % 10)) % 10


def test_method_13_positive_cases_direct_layout():
    # Build accounts: A1 B1 B2 B3 B4 B5 B6 C S1 S2
    # where B1..B6 is base, C is check (computed), and S1 S2 are ignored subaccount (random)
    base_cases = ["000000", "123456", "987654", "555555", "102938"]
    for a1 in ["0", "1", "9"]:
        for base in base_cases:
            c = compute_check_base_2_1(base)
            acc = a1 + base + str(c) + "12"  # subaccount arbitrary
            assert len(acc) == 10 and acc.isdigit()
            assert validate_method_13("10000000", acc) is True


def test_method_13_positive_cases_via_fallback_shift():
    # Create a valid shifted account S, then derive input I by moving S two to the right: I = "00" + S[:8]
    # The validator should fail initial calc on I but pass via fallback (which recreates S by shifting left)
    base = "246810"
    c = compute_check_base_2_1(base)
    S = "3" + base + str(c) + "00"  # a1=3, subaccount 00
    assert len(S) == 10
    I = "00" + S[:8]  # move two to right
    assert len(I) == 10
    # Sanity: initial layout likely fails but fallback should pass
    assert validate_method_13("10000000", I) is True


def test_method_13_negative_and_format_cases():
    # Wrong check digit should fail (without and with fallback)
    base = "135791"
    c = compute_check_base_2_1(base)
    acc = "4" + base + str((c + 1) % 10) + "99"
    assert validate_method_13("10000000", acc) is False

    # Non-digit and wrong lengths
    assert validate_method_13("10000000", "123456789") is False
    assert validate_method_13("10000000", "12345678901") is False
    assert validate_method_13("10000000", "12345678X0") is False
