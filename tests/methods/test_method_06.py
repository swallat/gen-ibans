# MIT License
#
# Tests for Bundesbank method 06: Mod11 with weights [2..10] over first 9 digits.

import random

from gen_ibans.methods.method_06 import validate_method_06
from gen_ibans.methods import generate_valid_account


def compute_check_mod11_w2_to_10(payload: str):
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i % len(weights)]
        total += d * w
    r = total % 11
    check = 11 - r
    if check == 10:
        return None
    if check == 11:
        return 0
    return check


def test_method_06_positive_cases():
    blz = "12345678"
    payloads = [
        "000000001",
        "123456789",
        "210987654",
        "001234567",
        "765432100",
    ]
    for p in payloads:
        p = p[-9:].zfill(9)
        cd = compute_check_mod11_w2_to_10(p)
        if cd is None:
            continue
        account = p + str(cd)
        assert validate_method_06(blz, account) is True


def test_method_06_invalid_and_negative():
    blz = "12345678"
    found = False
    for num in range(4000):
        p = f"{num:09d}"
        cd = compute_check_mod11_w2_to_10(p)
        if cd is None:
            found = True
            assert validate_method_06(blz, p + "0") is False
            break
    assert found

    p = "345678901"
    cd = compute_check_mod11_w2_to_10(p)
    if cd is None:
        p = "111111111"
        cd = compute_check_mod11_w2_to_10(p)
    assert cd is not None
    wrong = (cd + 1) % 10
    assert validate_method_06(blz, p + str(wrong)) is False

    # malformed
    assert validate_method_06(blz, "123456789") is False
    assert validate_method_06(blz, "12345678901") is False
    assert validate_method_06(blz, "123456789X") is False


def test_generate_valid_account_method_06():
    blz = "12345678"
    rng = random.Random(606)
    acc = generate_valid_account(blz, rng, "06")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_06(blz, acc) is True
