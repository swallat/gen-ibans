# MIT License
#
# Tests for Bundesbank method 00 (Mod 10 with alternating weights 2,1 over 9 digits).

import random

from gen_ibans.methods.method_00 import validate_method_00
from gen_ibans.methods import generate_valid_account


def test_method_00_examples_and_basic_validity():
    blz = "12345678"
    # Provided examples (left-padded to 10):
    assert validate_method_00(blz, "0009290701") is True
    assert validate_method_00(blz, "0539290858") is True
    # Classic sequence payload 123456789 -> check 7
    assert validate_method_00(blz, "1234567897") is True
    # All zeros are valid (check 0)
    assert validate_method_00(blz, "0000000000") is True
    # Negative example
    assert validate_method_00(blz, "1234567890") is False


def test_method_00_rejects_non_digits_or_wrong_length():
    blz = "12345678"
    assert validate_method_00(blz, "") is False
    assert validate_method_00(blz, "123456789") is False  # 9 digits
    assert validate_method_00(blz, "12345678901") is False  # 11 digits
    assert validate_method_00(blz, "12345678A0") is False  # non-digit


def test_generate_valid_account_method_00():
    blz = "12345678"
    rng = random.Random(42)
    acc = generate_valid_account(blz, rng, "00")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_00(blz, acc) is True
