# MIT License
#
# Tests for Bundesbank method 09: Keine Prüfzifferberechnung (no check digit).

import random

from gen_ibans.methods.method_09 import validate_method_09
from gen_ibans.methods import generate_valid_account


def test_method_09_accepts_any_10_digit_numeric():
    blz = "12345678"
    valid_accounts = [
        "0000000000",
        "0000000001",
        "1234567890",
        "9999999999",
        "0012345678",
    ]
    for acc in valid_accounts:
        assert validate_method_09(blz, acc) is True


def test_method_09_rejects_wrong_length_or_nondigit():
    blz = "12345678"
    invalid_accounts = [
        "",  # empty
        "123456789",  # 9 digits
        "12345678901",  # 11 digits
        "123456789X",  # non-digit
        "abcdefghij",  # non-digits
    ]
    for acc in invalid_accounts:
        assert validate_method_09(blz, acc) is False


def test_generate_valid_account_method_09():
    blz = "12345678"
    rng = random.Random(9)
    acc = generate_valid_account(blz, rng, "09")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_09(blz, acc) is True
