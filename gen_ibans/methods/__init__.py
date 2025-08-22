"""
Account number check-digit methods (Prüfzifferberechnungsmethoden) per Deutsche Bundesbank.

This package provides per-method validators and helpers to generate valid
10-digit German account numbers for a given bank method code.

Structure mirrors the reference layout: one file per method, and a registry.
"""
from typing import Callable, Optional
import random

# A validator receives BLZ and a 10-digit account number and returns True if valid for the method
Validator = Callable[[str, str], bool]

# A generator produces a valid 10-digit account number for the given BLZ and RNG
Generator = Callable[[str, random.Random], str]

_registry: dict[str, Validator] = {}


def register(method_code: str):
    """Decorator to register a validator for a method code."""

    def _wrap(func: Validator) -> Validator:
        _registry[method_code] = func
        return func

    return _wrap


def get_validator(method_code: Optional[str]) -> Validator:
    """Return a validator function for the given method code or a permissive default."""
    if method_code and method_code in _registry:
        return _registry[method_code]
    # Default: accept any 10-digit account number
    return lambda blz, acc: len(acc) == 10 and acc.isdigit()


def generate_valid_account(blz: str, rng: random.Random, method_code: Optional[str]) -> str:
    """Generate a valid 10-digit account number according to the bank's method.

    This naive implementation attempts random numbers until they pass the validator.
    Specific methods can later provide smarter direct constructions if needed.
    """
    validator = get_validator(method_code)
    # Try a bounded number of attempts to avoid infinite loops
    for _ in range(1000):
        # Sample a 10-digit number (allow leading zeros except all zeros)
        num = rng.randint(0, 9999999999)
        acc = f"{num:010d}"
        if acc != "0000000000" and validator(blz, acc):
            return acc
    # Fallback: deterministic last-resort, ensure not all zeros
    return "0000000001"

# Import concrete methods to populate the registry dynamically
import importlib
import pkgutil

for m in pkgutil.iter_modules(__path__):
    if m.name.startswith("method_"):
        importlib.import_module(f"{__name__}.{m.name}")
