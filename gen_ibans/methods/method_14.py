"""
Method 14: Modulus 11 with weights [2,3,4,5,6,7] applied right-to-left to positions 4–9;
positions 2–3 are the account type (Kontoart) and are not included in the calculation;
position 10 is the check digit.

Spec (per Deutsche Bundesbank; calculation like Method 02, but excluding Kontoart):
- Account number is 10 digits.
- Positions: 1 = unused for calculation; 2–3 = Kontoart (excluded); 4–9 = Grundnummer; 10 = check digit.
- Apply weights right-to-left on digits at positions 4..9: [2,3,4,5,6,7].
- Sum S = Σ(d_i * w_i). Let r = S % 11. Check digit c = 11 - r.
  * If c == 10 -> invalid (no valid check digit).
  * If c == 11 -> use 0 as check digit.
- Valid iff digit at position 10 equals computed check digit.

Notes:
- BLZ is not part of the calculation.
- Leading zeros are allowed in all segments.
"""
from . import register, register_generator


def _compute_check_mod11_m14(grundnummer: str) -> int | None:
    """Compute the Method 14 check digit from the 6-digit Grundnummer (positions 4–9).

    Returns an int 0..9 if valid; returns None if the result would be 10 (invalid per spec).
    """
    weights = [2, 3, 4, 5, 6, 7]
    total = 0
    for i, ch in enumerate(reversed(grundnummer)):
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


@register("14")
def validate_method_14(blz: str, account: str) -> bool:
    """Validate account number for Method 14 per Bundesbank spec.

    Expect a 10-digit account string. Use positions 4..9 to compute Mod11 check with
    weights [2..7]; compare against digit at position 10.
    """
    if len(account) != 10 or not account.isdigit():
        return False
    grund = account[3:9]  # positions 4..9 (0-based slicing: [3..8])
    expected = _compute_check_mod11_m14(grund)
    if expected is None:
        return False
    return (ord(account[9]) - 48) == expected


@register_generator("14")
def generate_account_method_14(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account number for Method 14.

    Strategy:
    - Sample leading digit (pos 1) and Kontoart (pos 2–3) uniformly.
    - Sample Grundnummer (pos 4–9) uniformly; compute check digit.
      If the result would be 10 (invalid), resample Grundnummer.
    - Expected rejection ≈ 1/11; loop bounded with a deterministic fallback.
    """
    # Sample pos1 and Kontoart first (do not affect check digit)
    pos1 = rng.randint(0, 9)
    kontoart = rng.randint(0, 99)

    for _ in range(1000):
        grund_num = rng.randint(0, 999_999)
        grund = f"{grund_num:06d}"
        cd = _compute_check_mod11_m14(grund)
        if cd is not None:
            account = f"{pos1:d}{kontoart:02d}{grund}{cd:d}"
            assert validate_method_14(blz, account)
            return account

    # Deterministic guaranteed-valid fallback: Grundnummer all zeros -> c = 0
    grund = "000000"
    cd = _compute_check_mod11_m14(grund)
    account = f"{pos1:d}{kontoart:02d}{grund}{cd:d}"
    assert validate_method_14(blz, account)
    return account
