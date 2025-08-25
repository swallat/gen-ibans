"""
Method 57 (Bundesbank): Composite with four variants per leading digits.

Summary of spec (essentials, adapted for implementation):
- Account number is 10 digits including the check digit. For calculation, treat
  the account left-padded with zeros to 10 digits. In this project, we require
  the input to already be exactly 10 digits (as in other methods).
- Any account starting with "00" is invalid (across all variants).

Variants:
1) Variant 1 (Luhn/Method 00 style, check at position 10):
   - Applies to accounts starting with: 51, 55, 61, 64, 65, 66, 70, 73–82, 88, 94, 95.
   - Compute Modulus 10 with weights 1,2,1,2,1,2,1,2,1 from left on positions 1..9.
     This is equivalent to Method 00 (Luhn-like) on the 9-digit payload.
   - Position 10 is the check digit.
   - Exception: Accounts starting with 777777 or 888888 are always valid
     (Method 09 semantics for these prefixes).

2) Variant 2 (Luhn/Method 00 style, check at position 3):
   - Applies to accounts starting with: 32–39, 41–49, 52–54, 56–60, 62–63,
     67–69, 71–72, 83–87, 89, 90, 92, 93, 96–98.
   - Positions 1,2,4,5,6,7,8,9,10 are multiplied by weights 1,2,1,2,1,2,1,2,1 (from left),
     i.e., compute Method 00 (Luhn-like) over the 9-digit payload formed by
     concatenating positions 1,2,4,5,6,7,8,9,10. Position 3 is the check digit.

3) Variant 3 (Method 09 – no check) applies for prefixes: 40, 50, 91, 99.
   - In this project we still enforce the general rule that an account starting
     with "00" is invalid, but those do not collide with these prefixes anyway.

4) Variant 4 (structural-only rules) applies for prefixes 01–31:
   - Positions 3–4 form a number between 01 and 12 inclusive.
   - Positions 7–9 form a number strictly less than 500 (000–499).
   - Exception: The specific account 0185125434 is always valid.

The calculations "entsprechen der Methode 00" are implemented via the same
Luhn-like Modulus-10 logic used in method_00: sum with alternating 2/1 weights
from the right over 9 digits, two-digit products reduced by cross-sum, and
check digit (10 - (sum % 10)) % 10.
"""
from __future__ import annotations

from . import register, register_generator
import random as _random


def _luhn_mod10_check_digit(payload9: str) -> int:
    """Compute Method 00 (Luhn-like) check digit for a 9-digit payload.

    Args:
        payload9: exactly 9 ASCII digits.
    Returns:
        The check digit (0..9).
    """
    if len(payload9) != 9 or not payload9.isdigit():
        raise ValueError("payload9 must be 9 digits")
    total = 0
    # Apply weights from rightmost payload digit: 1,2,1,2,... (so left-to-right is 1,2,1,2,... for 9 digits)
    for i, ch in enumerate(reversed(payload9)):
        d = ord(ch) - 48
        if (i % 2) == 1:
            prod = d * 2
            if prod >= 10:
                prod -= 9
        else:
            prod = d
        total += prod
    return (10 - (total % 10)) % 10


# Prefix groupings as per spec
_VARIANT1_PREFIXES = {
    "51", "55", "61", "64", "65", "66", "70",
    "73", "74", "75", "76", "77", "78", "79", "80", "81", "82",
    "88", "94", "95",
}
_VARIANT2_PREFIXES = set()
# Ranges: 32–39, 41–49, 52–54, 56–60, 62–63, 67–69, 71–72, 83–87, 89, 90, 92, 93, 96–98
for a, b in [(32, 39), (41, 49), (52, 54), (56, 60), (62, 63), (67, 69), (71, 72), (83, 87), (96, 98)]:
    for p in range(a, b + 1):
        _VARIANT2_PREFIXES.add(f"{p:02d}")
# Singles
_VARIANT2_PREFIXES.update({"89", "90", "92", "93"})

_VARIANT3_PREFIXES = {"40", "50", "91", "99"}


def _starts_with_any(s: str, prefixes: set[str]) -> bool:
    return s[:2] in prefixes


def _is_always_valid_exception(account: str) -> bool:
    # Variant 1 exception: starts with 777777 or 888888 always valid
    if account.startswith("777777") or account.startswith("888888"):
        return True
    # Variant 4 explicit exception
    if account == "0185125434":
        return True
    return False


@register("57")
def validate_method_57(blz: str, account: str) -> bool:
    """Validate a 10-digit account according to Bundesbank Method 57.

    Deterministic, BLZ-independent as per spec.
    """
    if len(account) != 10 or not account.isdigit():
        return False

    # General rule: accounts starting with 00 are always invalid
    if account.startswith("00"):
        return False

    # Global allowed exceptions
    if _is_always_valid_exception(account):
        return True

    prefix2 = account[:2]

    # Variant 3: method 09 (no check) for certain prefixes
    if prefix2 in _VARIANT3_PREFIXES:
        return True

    # Variant 4: structural-only rules for prefixes 01–31
    if 1 <= int(prefix2) <= 31:
        # Apply structural constraints
        # 3rd-4th positions form 01..12
        mm = int(account[2:4])
        if not (1 <= mm <= 12):
            return False
        # 7th-9th positions form 000..499
        block_7_9 = int(account[6:9])
        if block_7_9 >= 500:
            return False
        return True

    # Variant 1: method 00 with check at position 10
    if prefix2 in _VARIANT1_PREFIXES:
        payload9 = account[:9]
        expected = _luhn_mod10_check_digit(payload9)
        return (ord(account[9]) - 48) == expected

    # Variant 2: method 00 with check at position 3
    if prefix2 in _VARIANT2_PREFIXES:
        # Build 9-digit payload from positions 1,2,4,5,6,7,8,9,10
        payload9 = account[:2] + account[3:]
        expected = _luhn_mod10_check_digit(payload9)
        return (ord(account[2]) - 48) == expected

    # If no variant applies, treat as invalid per spec
    return False


@register_generator("57")
def generate_account_method_57(blz: str, rng: _random.Random) -> str:
    """Generate a valid account according to Method 57.

    Strategy: Prefer Variant 1 (deterministic check digit) for simplicity and
    efficiency. We pick a valid Variant-1 prefix, sample the remaining digits,
    compute the Luhn/Method-00 check digit at position 10.

    With small probability, generate a Variant 4 structural account as well to
    diversify outputs while keeping it direct and efficient.
    """
    # 80/20 split between Variant 1 and Variant 4
    if rng.random() < 0.8:
        prefix = rng.choice(sorted(_VARIANT1_PREFIXES))
        mid_num = rng.randint(0, 9_999_99)  # 6 digits for positions 3..8, then one more for pos9
        # We'll generate positions 3..9 as 7 digits
        mid = f"{mid_num:07d}"
        payload9 = prefix + mid  # positions 1..9
        cd = _luhn_mod10_check_digit(payload9)
        account = payload9 + str(cd)
        # Guard against global invalid rule
        if account.startswith("00"):
            # Extremely unlikely since prefix is variant1; resample recursively
            return generate_account_method_57(blz, rng)
        # Defensive validation
        assert validate_method_57(blz, account)
        return account
    else:
        # Variant 4 structural generator
        # Prefix 01..31 but not 00
        p = rng.randint(1, 31)
        prefix = f"{p:02d}"
        # Positions 3-4: 01..12
        mm = rng.randint(1, 12)
        # Positions 5-6: free two digits
        d56 = rng.randint(0, 99)
        # Positions 7-9: 000..499
        d7_9 = rng.randint(0, 499)
        # Position 10: free digit
        d10 = rng.randint(0, 9)
        account = f"{prefix}{mm:02d}{d56:02d}{d7_9:03d}{d10:d}"
        # Enforce not starting with 00 (not possible here) and structural validity
        if not validate_method_57(blz, account):
            # In the extremely unlikely case structural combination is rejected
            # (should not happen), fallback to Variant 1
            return generate_account_method_57(blz, rng)
        return account
