# MIT License
#
# Tests for Bundesbank method 17 per spec (Modulus 11 over positions 2..7 with
# weights 1,2,1,2,1,2; subtract 1 before modulus; P at position 8).

import random

from gen_ibans.methods.method_17 import validate_method_17
from gen_ibans.methods import generate_valid_account


def _quersumme(n: int) -> int:
    return (n // 10) + (n % 10)


def compute_check_method_17_from_stamm(stamm6: str) -> int:
    weights = (1, 2, 1, 2, 1, 2)
    total = 0
    for i, ch in enumerate(stamm6):
        d = ord(ch) - 48
        w = weights[i]
        prod = d * w
        if w == 2:
            prod = _quersumme(prod)
        total += prod
    r = (total - 1) % 11
    if r == 0:
        return 0
    return 10 - r


def test_method_17_positive_cases_example():
    blz = "87654321"
    # Provided example from spec: 0446786040 must be valid
    assert validate_method_17(blz, "0446786040") is True


def test_method_17_negative_cases_mutation_and_format():
    blz = "87654321"
    # Take the example and mutate the check digit
    acc = "0446786040"
    wrong = acc[:7] + ("1" if acc[7] != "1" else "2") + acc[8:]
    assert validate_method_17(blz, wrong) is False

    # non-digits and wrong length should fail
    assert validate_method_17(blz, "123456789") is False
    assert validate_method_17(blz, "12345678901") is False
    assert validate_method_17(blz, "123456789X") is False


def test_generate_valid_account_method_17():
    blz = "87654321"
    rng = random.Random(2025)
    acc = generate_valid_account(blz, rng, "17")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_17(blz, acc) is True
