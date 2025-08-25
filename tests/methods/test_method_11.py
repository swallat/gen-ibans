# MIT License
#
# Tests for Bundesbank method 11: Modulus 11 with weights 2..10 (right-to-left, modified like method 06)

import random

from gen_ibans.methods.method_11 import validate_method_11
from gen_ibans.methods import generate_valid_account


def compute_check_method_11(payload: str) -> int:
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i]  # i in 0..8
        total += d * w
    r = total % 11
    if r == 0:
        return 0
    if r == 1:
        return 9
    return 11 - r


def test_method_11_positive_cases():
    blz = "10000000"
    samples = [
        "000000000",  # yields check 0
        "000000001",  # easy manual check
        "123456789",
        "210987654",
        "001234567",
        "765432100",
    ]
    for p in samples:
        p = p[-9:].zfill(9)
        cd = compute_check_method_11(p)
        acc = p + str(cd)
        assert validate_method_11(blz, acc) is True


def test_method_11_rejects_wrong_lengths_and_non_digits():
    blz = "10000000"
    assert validate_method_11(blz, "123456789") is False
    assert validate_method_11(blz, "12345678901") is False
    assert validate_method_11(blz, "123456789X") is False


def test_generate_valid_account_method_11_smoke():
    # Direct generator exists and must produce valid accounts deterministically
    rng = random.Random(111)
    acc = generate_valid_account("10000000", rng, "11")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_11("10000000", acc) is True
