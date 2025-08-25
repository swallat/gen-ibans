import random
import pytest

from gen_ibans.methods.method_57 import validate_method_57, generate_account_method_57


@pytest.mark.parametrize(
    "account",
    [
        # From spec: Testkontonummern (richtig)
        "7500021766",
        "9400001734",
        "7800028282",
        "8100244186",
        "3251080371",
        "3891234567",
        "7777778800",  # variant 1 always valid exception range
        "5001050352",  # variant 3 (50 prefix)
        "5045090090",  # variant 3 (50 prefix)
        "1909700805",  # variant 4 range, structural
        "9322111030",  # variant 2 (93 prefix)
        "7400060823",
    ],
)
def test_method_57_examples_valid(account):
    assert validate_method_57("00000000", account) is True


@pytest.mark.parametrize(
    "account",
    [
        # From spec: Testkontonummern (falsch)
        "5302707782",
        "6412121212",
        "1813499124",
        "2206735010",
    ],
)
def test_method_57_examples_invalid(account):
    assert validate_method_57("00000000", account) is False


def test_method_57_general_rules_and_exceptions():
    # Global invalid: starts with 00
    assert validate_method_57("00000000", "0012345678") is False

    # Explicit exception in variant 4
    assert validate_method_57("00000000", "0185125434") is True

    # Variant 3 prefixes (40, 50, 91, 99) are accepted regardless of internal digits
    for pref in ("40", "50", "91", "99"):
        base = pref + "12345678"  # total 10 digits
        assert validate_method_57("00000000", base) is True

    # Variant 4 structural constraints: prefixes 01..31
    # Valid structure: MM between 01..12 and positions 7..9 < 500
    assert validate_method_57("00000000", "0112012340") is True  # mm=12, d7_9=234
    # Invalid month
    assert validate_method_57("00000000", "0185012340") is False  # mm=85
    # Invalid 7-9 >= 500
    assert validate_method_57("00000000", "0123999123") is False  # 999 >= 500


def test_method_57_variant2_payload_positions():
    # Pick a crafted variant-2 account: prefix 32..39 etc.
    # Use known-valid example 3251080371 from spec
    assert validate_method_57("00000000", "3251080371") is True


def test_method_57_generator_produces_valid_accounts():
    rng = random.Random(12345)
    for _ in range(200):
        acc = generate_account_method_57("00000000", rng)
        assert len(acc) == 10 and acc.isdigit()
        assert validate_method_57("00000000", acc) is True
