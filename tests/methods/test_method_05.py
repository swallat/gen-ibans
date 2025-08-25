# MIT License
#
# Tests for Bundesbank method 05: Luhn (Modulus 10) over first 9 digits.

import random

from gen_ibans.methods.method_05 import validate_method_05
from gen_ibans.methods import generate_valid_account


def luhn_check_digit(payload: str) -> int:
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        if i % 2 == 0:
            total += d
        else:
            dd = d * 2
            if dd > 9:
                dd -= 9
            total += dd
    return (10 - (total % 10)) % 10


def test_method_05_positive_cases():
    blz = "12345678"
    payloads = [
        "000000001",
        "123456789",
        "987654321",
        "500000000",
        "001234567",
    ]
    for p in payloads:
        p = p[-9:].zfill(9)
        cd = luhn_check_digit(p)
        account = p + str(cd)
        assert validate_method_05(blz, account) is True


def test_method_05_negative_cases_mutation():
    blz = "12345678"
    p = "123456789"
    cd = luhn_check_digit(p)
    account = p + str(cd)
    wrong_last = (cd + 1) % 10
    wrong_account = p + str(wrong_last)
    assert validate_method_05(blz, wrong_account) is False

    # malformed
    assert validate_method_05(blz, "123456789") is False
    assert validate_method_05(blz, "12345678901") is False
    assert validate_method_05(blz, "123456789X") is False


def test_generate_valid_account_method_05():
    blz = "12345678"
    rng = random.Random(5005)
    acc = generate_valid_account(blz, rng, "05")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_05(blz, acc) is True
