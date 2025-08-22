# MIT License
#
# Tests for Bundesbank method 10: Simple Mod10 checksum over first 9 digits.

import random

from gen_ibans.methods.method_10 import validate_method_10
from gen_ibans.methods import generate_valid_account


def simple_mod10(payload: str) -> int:
    total = sum(ord(ch) - 48 for ch in payload)
    return total % 10


def test_method_10_positive_cases():
    blz = "12345678"
    for p in ["000000000", "123456789", "987654321", "111111111", "555555555"]:
        p9 = p[-9:].zfill(9)
        cd = simple_mod10(p9)
        account = p9 + str(cd)
        assert validate_method_10(blz, account) is True


def test_method_10_negative_cases():
    blz = "12345678"
    p9 = "123456789"
    cd = simple_mod10(p9)
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
