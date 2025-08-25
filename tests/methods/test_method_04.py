# MIT License
#
# Tests for Bundesbank method 04: Modulus 11 with weights [2,3,4,5,6,7,2,3,4]
# applied right-to-left over the 9 payload digits (calculation as in Method 02).

import random

from gen_ibans.methods.method_04 import validate_method_04
from gen_ibans.methods import generate_valid_account


def compute_check_mod11_m04(payload: str):
    weights = [2, 3, 4, 5, 6, 7, 2, 3, 4]
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = ord(ch) - 48
        w = weights[i]
        total += d * w
    r = total % 11
    c = 11 - r
    if c == 10:
        return None
    if c == 11:
        return 0
    return c


essential_payloads = [
    "000000001",
    "123456789",
    "210987654",
    "001234567",
    "765432100",
]


def test_method_04_positive_cases():
    blz = "12345678"
    for p in essential_payloads:
        p9 = p[-9:].zfill(9)
        cd = compute_check_mod11_m04(p9)
        if cd is None:
            continue
        account = p9 + str(cd)
        assert validate_method_04(blz, account) is True


def test_method_04_negative_cases():
    blz = "12345678"
    # Ensure a payload that yields invalid cd (10) is treated as invalid for any digit
    found = False
    for num in range(4000):
        p9 = f"{num:09d}"
        cd = compute_check_mod11_m04(p9)
        if cd is None:
            found = True
            assert validate_method_04(blz, p9 + "0") is False
            break
    assert found

    # Regular wrong-check mutation
    p9 = "345678901"
    cd = compute_check_mod11_m04(p9)
    if cd is None:
        p9 = "111111111"
        cd = compute_check_mod11_m04(p9)
    assert cd is not None
    wrong = (cd + 1) % 10
    assert validate_method_04(blz, p9 + str(wrong)) is False

    # malformed
    assert validate_method_04(blz, "123456789") is False
    assert validate_method_04(blz, "12345678901") is False
    assert validate_method_04(blz, "123456789X") is False


def test_generate_valid_account_method_04():
    blz = "12345678"
    rng = random.Random(4004)
    acc = generate_valid_account(blz, rng, "04")
    assert len(acc) == 10 and acc.isdigit()
    assert validate_method_04(blz, acc) is True
