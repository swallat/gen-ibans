# MIT License
#
# Tests for Bundesbank method 24: Modulus 11 with weights [2,3,4,5,6,7,8,9,2].

import random

from gen_ibans.methods.method_24 import validate_method_24
from gen_ibans.methods import generate_valid_account


def compute_check_mod11_custom(payload: str):
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2]
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


def test_method_24_positive_cases_and_leading_zeros():
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
        cd = compute_check_mod11_custom(p)
        if cd is None:
            continue
        account = p + str(cd)
        assert validate_method_24(blz, account) is True


def test_method_24_negative_and_invalid_cases():
    blz = "12345678"
    # Find a payload that yields None (check==10 -> invalid)
    found = False
    for num in range(3000):
        p = f"{num:09d}"
        cd = compute_check_mod11_custom(p)
        if cd is None:
            found = True
            # No possible correct check digit; validator must return False
            assert validate_method_24(blz, p + "0") is False
            break
    assert found, "expected to find invalid (check==10) payload quickly"

    # Regular wrong-check mutation
    p = "345678901"
    cd = compute_check_mod11_custom(p)
    if cd is None:
        p = "111111111"
        cd = compute_check_mod11_custom(p)
    assert cd is not None
    wrong_last = (cd + 1) % 10
    wrong_account = p + str(wrong_last)
    assert validate_method_24(blz, wrong_account) is False

    # Non-digit / wrong length
    assert validate_method_24(blz, "123456789") is False
    assert validate_method_24(blz, "12345678901") is False
    assert validate_method_24(blz, "123456789X") is False


def test_generate_valid_account_method_24():
    blz = "12345678"
    rng = random.Random(24)
    acc = generate_valid_account(blz, rng, "24")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_24(blz, acc) is True