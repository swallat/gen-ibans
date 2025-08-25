# MIT License
#
# Tests for Bundesbank method 03: Modulus 10 with alternating weights 2,1 (no cross-sum),
# calculation as in method 01.

import random

from gen_ibans.methods.method_03 import validate_method_03
from gen_ibans.methods import generate_valid_account


def compute_check_mod10_w21_no_crosssum(payload: str):
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        if (i % 2) == 0:
            prod = d * 2  # weight 2 on rightmost payload digit
        else:
            prod = d      # weight 1
        total += prod
    return (10 - (total % 10)) % 10


def test_method_03_positive_cases():
    blz = "12345678"
    payloads = [
        "000000001",
        "123456789",
        "700000003",
        "001234567",
        "765432100",
    ]
    for p in payloads:
        p = p[-9:].zfill(9)
        cd = compute_check_mod10_w21_no_crosssum(p)
        account = p + str(cd)
        assert validate_method_03(blz, account) is True


def test_method_03_negative_cases():
    blz = "12345678"
    p = "345678901"
    cd = compute_check_mod10_w21_no_crosssum(p)
    wrong_last = (cd + 1) % 10
    wrong_account = p + str(wrong_last)
    assert validate_method_03(blz, wrong_account) is False

    # malformed
    assert validate_method_03(blz, "123456789") is False
    assert validate_method_03(blz, "12345678901") is False
    assert validate_method_03(blz, "123456789X") is False


def test_generate_valid_account_method_03():
    blz = "12345678"
    rng = random.Random(3)
    acc = generate_valid_account(blz, rng, "03")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_03(blz, acc) is True
