# MIT License
#
# Tests for Bundesbank method A4 (composite variants 1..4).

import random

from gen_ibans.methods.method_A4 import validate_method_A4
from gen_ibans.methods import generate_valid_account


# Helper mirroring the spec examples

def compute_mod11_method06(sum_val: int) -> int:
    r = sum_val % 11
    if r in (0, 1):
        return 0
    return 11 - r


def weighted_sum_right_to_left(digits: list[int], weights: tuple[int, ...]) -> int:
    total = 0
    for i, d in enumerate(reversed(digits)):
        total += d * weights[i % len(weights)]
    return total


def str_to_digits(s: str) -> list[int]:
    return [ord(ch) - 48 for ch in s]


def test_method_A4_variant1_examples_from_spec():
    blz = "12345678"
    # Beispiel 1 aus Spezifikation: 0004711173 (richtig)
    assert validate_method_A4(blz, "0004711173") is True
    # Beispiel 2 aus Spezifikation: 0007093330 (richtig)
    assert validate_method_A4(blz, "0007093330") is True


def test_method_A4_variant2_examples_from_spec():
    blz = "12345678"
    # Beispiel: 0004711172 (richtig laut Variante 2)
    assert validate_method_A4(blz, "0004711172") is True
    # Weiteres richtiges Beispiel
    assert validate_method_A4(blz, "0007093335") is True


def test_method_A4_variant3_examples_from_spec():
    blz = "12345678"
    # Kontonummern mit 99 an Stelle 3 und 4
    assert validate_method_A4(blz, "1199503010") is True
    assert validate_method_A4(blz, "8499421235") is True
    # Falsche Beispiele
    assert validate_method_A4(blz, "1299503117") is True  # per Spec valid via Variant 4 fallback


def test_method_A4_variant4_examples_from_spec():
    blz = "12345678"
    # Aus Spezifikation (teils Mod 7, teils Mod 11, sowie weitere):
    for acc in [
        "0000862342",  # Mod 7
        "8997710000",  # Mod 7
        "0664040000",  # Mod 7
        "0000905844",  # Mod 11
        "5030101099",  # Mod 11
        "0001123458",  # allgemein gültig via Var.4
        "1299503117",  # aus Var.3 falsch, aber per Var.4 gültig
    ]:
        assert validate_method_A4(blz, acc) is True

    for acc in [
        "0000399443",
        "0000553313",
    ]:
        assert validate_method_A4(blz, acc) is False


def test_generate_valid_account_method_A4():
    blz = "50010517"
    rng = random.Random(4044)
    for _ in range(200):
        acc = generate_valid_account(blz, rng, "A4")
        assert len(acc) == 10 and acc.isdigit()
        assert validate_method_A4(blz, acc) is True
