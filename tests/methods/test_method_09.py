# MIT License
#
# Tests for Bundesbank method 09: Modulus 11 with repeating weights 2..7 (right-to-left).

import random

from gen_ibans.methods.method_09 import validate_method_09
from gen_ibans.methods import generate_valid_account


def compute_check_mod11_weights_2_to_7(payload: str):
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


def test_method_09_positive_cases_and_leading_zeros():
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
        cd = compute_check_mod11_weights_2_to_7(p)
        # skip payloads where rule yields None (invalid, check==10)
        if cd is None:
            continue
        account = p + str(cd)
        assert validate_method_09(blz, account) is True


def test_method_09_negative_cases():
    blz = "12345678"
    p = "345678901"
    cd = compute_check_mod11_weights_2_to_7(p)
    if cd is None:
        # If this particular payload yields None, pick another simple one
        p = "111111111"
        cd = compute_check_mod11_weights_2_to_7(p)
    assert cd is not None
    account = p + str(cd)
    # mutate last digit to be wrong
    wrong_last = (cd + 1) % 10
    wrong_account = p + str(wrong_last)
    assert validate_method_09(blz, wrong_account) is False

    # non-digits / wrong length
    assert validate_method_09(blz, "123456789") is False
    assert validate_method_09(blz, "12345678901") is False
    assert validate_method_09(blz, "123456789X") is False


def test_method_09_invalid_when_check_equals_10():
    blz = "12345678"
    # Try to find a payload that yields check==10 (invalid)
    # Brute-force small search to keep test simple and fast
    found = False
    for num in range(2000):
        p = f"{num:09d}"
        cd = compute_check_mod11_weights_2_to_7(p)
        if cd is None:  # means check==10 per rule
            found = True
            # Any last digit won't make it valid; try with '0'
            assert validate_method_09(blz, p + "0") is False
            break
    assert found, "expected to find a payload with check==10 within small search"


def test_generate_valid_account_method_09():
    blz = "12345678"
    rng = random.Random(9)
    acc = generate_valid_account(blz, rng, "09")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_09(blz, acc) is True
