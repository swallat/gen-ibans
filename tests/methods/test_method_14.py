# MIT License
#
# Tests for Bundesbank method 14: Modulus 11 with weights [2,3,4,5,6,7]
# applied to positions 4..9; positions 2..3 (Kontoart) excluded; pos10 is check digit.

import random

from gen_ibans.methods.method_14 import validate_method_14
from gen_ibans.methods import generate_valid_account


def compute_check_mod11_m14(grund: str):
    """Compute check digit for method 14 from the 6-digit Grundnummer.

    Returns int 0..9 or None if result would be 10 (invalid per spec).
    """
    weights = [2, 3, 4, 5, 6, 7]
    total = 0
    for i, ch in enumerate(reversed(grund)):
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


def test_method_14_positive_cases():
    blz = "10000000"
    # Build accounts: P1 KA1 KA2 G1..G6 C
    bases = [
        "000000",
        "123456",
        "654321",
        "102938",
        "999999",
    ]
    for p1 in ["0", "4", "9"]:
        for ka in ["00", "12", "99"]:
            for grund in bases:
                cd = compute_check_mod11_m14(grund)
                if cd is None:
                    continue
                acc = p1 + ka + grund + str(cd)
                assert len(acc) == 10 and acc.isdigit()
                assert validate_method_14(blz, acc) is True


def test_method_14_negative_and_format_cases():
    blz = "10000000"
    # Find a grund that yields invalid (cd == 10) and ensure validator rejects
    found = False
    for num in range(20000):
        grund = f"{num:06d}"
        cd = compute_check_mod11_m14(grund)
        if cd is None:
            # Any check digit in last place should be rejected for this grund
            acc = "1" + "23" + grund + "0"
            assert validate_method_14(blz, acc) is False
            found = True
            break
    assert found

    # Wrong check mutation
    grund = "345678"
    cd = compute_check_mod11_m14(grund)
    if cd is None:
        grund = "111111"
        cd = compute_check_mod11_m14(grund)
    assert cd is not None
    wrong = (cd + 1) % 10
    acc_wrong = "8" + "45" + grund + str(wrong)
    assert validate_method_14(blz, acc_wrong) is False

    # Format errors
    assert validate_method_14(blz, "123456789") is False  # 9 digits
    assert validate_method_14(blz, "12345678901") is False  # 11 digits
    assert validate_method_14(blz, "12345678X0") is False  # non-digit


def test_generate_valid_account_method_14():
    blz = "28020050"
    rng = random.Random(14)
    acc = generate_valid_account(blz, rng, "14")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_14(blz, acc) is True
