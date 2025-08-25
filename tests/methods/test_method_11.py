# MIT License
#
# Tests for Bundesbank method 11: Modulus 10 with weights 3,7,1 from right to left.

import random

from gen_ibans.methods.method_11 import validate_method_11
from gen_ibans.methods import generate_valid_account


def compute_check_method_11(payload: str) -> int:
    weights = [3, 7, 1]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i % 3]
        total += d * w
    # Units digit only, subtract from 10; if 10 -> 0
    return (10 - (total % 10)) % 10


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
