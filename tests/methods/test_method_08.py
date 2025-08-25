# MIT License
#
# Tests for Bundesbank method 08: Modulus 10 like method 00, applied only for
# account numbers >= 60000. Below 60000 (ignoring leading zeros), no checksum is applied.

import random

from gen_ibans.methods.method_08 import validate_method_08
from gen_ibans.methods import generate_valid_account


def compute_check_mod10_w21(payload: str) -> int:
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        if (i % 2) == 0:
            prod = d * 2
            if prod >= 10:
                prod -= 9
        else:
            prod = d
        total += prod
    return (10 - (total % 10)) % 10




def _num(acc: str) -> int:
    return int(acc)


def test_method_08_threshold_behavior_and_validity():
    blz = "12345678"
    # Below threshold: numeric value < 60000 -> accept by format alone
    assert validate_method_08(blz, "0000000000") is True
    assert validate_method_08(blz, "0000000599") is True  # 599 < 60000
    assert validate_method_08(blz, "0000059999") is True  # 59999 < 60000

    # At or above threshold: checksum per Method 00 must hold
    p = "123456789"
    cd = compute_check_mod10_w21(p)
    assert validate_method_08(blz, p + str(cd)) is True
    wrong = (cd + 1) % 10
    assert validate_method_08(blz, p + str(wrong)) is False

    # Malformed
    assert validate_method_08(blz, "123456789") is False
    assert validate_method_08(blz, "12345678901") is False
    assert validate_method_08(blz, "123456789X") is False


def test_generate_valid_account_method_08():
    blz = "12345678"
    rng = random.Random(808)
    acc = generate_valid_account(blz, rng, "08")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_08(blz, acc) is True
    # Our generator aims to produce >= 60000 numbers
    assert int(acc) >= 60000
