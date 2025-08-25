# MIT License
#
# Tests for Bundesbank method 03: Modulus 11 with repeating weights 2..7.

import random

from gen_ibans.methods.method_03 import validate_method_03
from gen_ibans.methods import generate_valid_account


def compute_check_mod11_w2_to_7(payload: str):
    weights = [2, 3, 4, 5, 6, 7]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i % len(weights)]
        total += d * w
    remainder = total % 11
    check = 11 - remainder
    if check == 10:
        return None
    if check == 11:
        return 0
    return check


def test_method_03_positive_cases():
    blz = "12345678"
    payloads = [
        "000000001",
        "123456789",
        "700000003",
        "001234567",
        "765432100",
    ]
    for p in payloads:
        p = p[-9:].zfill(9)
        cd = compute_check_mod11_w2_to_7(p)
        if cd is None:
            continue
        account = p + str(cd)
        assert validate_method_03(blz, account) is True


def test_method_03_negative_cases():
    blz = "12345678"
    p = "345678901"
    cd = compute_check_mod11_w2_to_7(p)
    if cd is None:
        p = "111111111"
        cd = compute_check_mod11_w2_to_7(p)
    assert cd is not None
    wrong_last = (cd + 1) % 10
    wrong_account = p + str(wrong_last)
    assert validate_method_03(blz, wrong_account) is False

    # malformed
    assert validate_method_03(blz, "123456789") is False
    assert validate_method_03(blz, "12345678901") is False
    assert validate_method_03(blz, "123456789X") is False


def test_method_03_invalid_when_check_equals_10():
    blz = "12345678"
    found = False
    for num in range(2000):
        p = f"{num:09d}"
        cd = compute_check_mod11_w2_to_7(p)
        if cd is None:
            found = True
            assert validate_method_03(blz, p + "0") is False
            break
    assert found


def test_generate_valid_account_method_03():
    blz = "12345678"
    rng = random.Random(3)
    acc = generate_valid_account(blz, rng, "03")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_03(blz, acc) is True
