# MIT License
#
# Tests for Bundesbank method 10: Mod11 with weights [2..10] over first 9 digits (modified),
# like method 06 rules for r==0 and r==1 -> check digit 0.

import random

from gen_ibans.methods.method_10 import validate_method_10
from gen_ibans.methods import generate_valid_account


def compute_check_mod11_w2_to_10(payload: str) -> int:
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        total += d * weights[i]
    r = total % 11
    if r == 0:
        return 0
    if r == 1:
        return 0
    return 11 - r


def test_method_10_positive_cases():
    blz = "12345678"
    for p in ["000000000", "123456789", "987654321", "111111111", "555555555"]:
        p9 = p[-9:].zfill(9)
        cd = compute_check_mod11_w2_to_10(p9)
        account = p9 + str(cd)
        assert validate_method_10(blz, account) is True

    # Check given examples (interpreted as left-padded to 10 digits)
    assert validate_method_10(blz, "0012345008") is True
    assert validate_method_10(blz, "0087654008") is True


def test_method_10_negative_cases():
    blz = "12345678"
    p9 = "123456789"
    cd = compute_check_mod11_w2_to_10(p9)
    wrong = (cd + 1) % 10
    assert validate_method_10(blz, p9 + str(wrong)) is False

    # malformed
    assert validate_method_10(blz, "123456789") is False
    assert validate_method_10(blz, "12345678901") is False
    assert validate_method_10(blz, "123456789X") is False


def test_generate_valid_account_method_10():
    blz = "12345678"
    rng = random.Random(1000)
    acc = generate_valid_account(blz, rng, "10")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_10(blz, acc) is True
