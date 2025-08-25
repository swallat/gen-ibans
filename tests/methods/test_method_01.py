# MIT License
#
# Tests for Bundesbank method 01: Mod10 with repeating weights 3,7,1 over first 9 digits.

import random

from gen_ibans.methods.method_01 import validate_method_01
from gen_ibans.methods import generate_valid_account


def compute_check_mod10_w371(payload: str) -> int:
    weights = (3, 7, 1)
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        total += d * weights[i % 3]
    return (10 - (total % 10)) % 10


def test_method_01_positive_cases():
    blz = "12345678"
    payloads = [
        "000000001",
        "123456789",
        "210987654",
        "001234567",
        "765432100",
        "000000000",  # all-zero payload -> check 0
    ]
    for p in payloads:
        p = p[-9:].zfill(9)
        cd = compute_check_mod10_w371(p)
        account = p + str(cd)
        assert validate_method_01(blz, account) is True


def test_method_01_negative_and_input_errors():
    blz = "12345678"
    p = "345678901"
    cd = compute_check_mod10_w371(p)
    wrong = (cd + 1) % 10
    assert validate_method_01(blz, p + str(wrong)) is False

    # non-digit / wrong length
    assert validate_method_01(blz, "123456789") is False
    assert validate_method_01(blz, "12345678901") is False
    assert validate_method_01(blz, "123456789X") is False


def test_generate_valid_account_method_01():
    blz = "12345678"
    rng = random.Random(101)
    acc = generate_valid_account(blz, rng, "01")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_01(blz, acc) is True
