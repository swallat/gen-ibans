# MIT License
#
# Tests for Bundesbank method C5.

import random

from gen_ibans.methods.method_C5 import validate_method_C5
from gen_ibans.methods import generate_valid_account


def test_variant1_examples_6_digit_right_and_wrong():
    blz = "12345678"
    # Right examples from spec
    assert validate_method_C5(blz, "0000301168") is True
    assert validate_method_C5(blz, "0000302554") is True
    # Wrong examples from spec
    assert validate_method_C5(blz, "0000302589") is False
    assert validate_method_C5(blz, "0000507336") is False


def test_variant1_examples_9_digit_right_and_wrong():
    blz = "12345678"
    assert validate_method_C5(blz, "0300020050") is True
    assert validate_method_C5(blz, "0300566000") is True
    assert validate_method_C5(blz, "0302555000") is False
    assert validate_method_C5(blz, "0302589000") is False


def test_variant2_examples_right_and_wrong():
    blz = "12345678"
    rights = [
        "1000061378",
        "1000061412",
        "4450164064",
        "4863476104",
        "5000000028",
        "5000000391",
        "6450008149",
        "6800001016",
        "9000100012",
        "9000210017",
    ]
    wrongs = [
        "1000061457",
        "1000061498",
        "4864446015",
        "4865038012",
        "5000001028",
        "5000001075",
        "6450008150",
        "6542812818",
        "9000110012",
        "9000300310",
    ]
    for acc in rights:
        assert validate_method_C5(blz, acc) is True
    for acc in wrongs:
        assert validate_method_C5(blz, acc) is False


def test_variant3_examples_right_and_wrong():
    blz = "12345678"
    assert validate_method_C5(blz, "3060188103") is True
    assert validate_method_C5(blz, "3070402023") is True
    assert validate_method_C5(blz, "3081000783") is False
    assert validate_method_C5(blz, "3081308871") is False


essential_v4 = [
    # Variant 4 ranges: 0030000000..0059999999 (10-digit padded form), 70xxxxxxxx, 85xxxxxxxx
    "0030000000",
    "0041234567",
    "0059999999",
    "7000000000",
    "8599999999",
]


def test_variant4_ranges_are_accepted():
    blz = "12345678"
    for acc in essential_v4:
        assert validate_method_C5(blz, acc) is True


def test_generator_produces_valid_10_digit():
    blz = "12345678"
    rng = random.Random(12345)
    for _ in range(50):
        acc = generate_valid_account(blz, rng, "C5")
        assert len(acc) == 10 and acc.isdigit()
        assert validate_method_C5(blz, acc) is True
