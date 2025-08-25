"""
Method 17 (Bundesbank): Modulus 11 with weights 1,2,1,2,1,2 applied to the 6-digit
Stammnummer (positions 2..7 in KSSSSSSPUU). The check digit P is at position 8.

Rules per spec:
- Account number has 10 digits: K S S S S S S P U U
- Relevant 6-digit Stammnummer S is at positions 2..7 (account[1:7]).
- Multiply S digits left-to-right with weights [1,2,1,2,1,2].
- For the positions with weight 2 (2nd, 4th, 6th), reduce any two-digit product
  by summing its digits (Quersumme).
- Sum all six contributions, subtract 1 from the sum.
- Divide by 11: let r = (sum_minus_1) % 11.
- If r == 0 -> check digit = 0; else check digit = 10 - r.
- Valid iff the 8th digit P equals the computed check digit.

Notes:
- BLZ is not used by this method.
- Leading zeros are allowed; the account must be exactly 10 digits.
"""
from . import register, register_generator


def _quersumme(n: int) -> int:
    """Digit sum of a non-negative integer n (n is small here)."""
    return (n // 10) + (n % 10)


def _compute_check_method_17_from_stamm(stamm6: str) -> int:
    """Compute the check digit P for the given 6-digit Stammnummer.

    Args:
        stamm6: exactly 6 ASCII digits representing positions 2..7.
    Returns:
        The check digit (0..9) per Method 17.
    """
    weights = (1, 2, 1, 2, 1, 2)
    total = 0
    for i, ch in enumerate(stamm6):
        d = ord(ch) - 48
        w = weights[i]
        prod = d * w
        if w == 2:
            # Apply Quersumme (digit sum) to possibly two-digit product
            prod = _quersumme(prod)
        total += prod
    total_minus_1 = total - 1
    r = total_minus_1 % 11
    if r == 0:
        return 0
    return 10 - r


@register("17")
def validate_method_17(blz: str, account: str) -> bool:
    if len(account) != 10 or not account.isdigit():
        return False
    # Positions: 0 1 2 3 4 5 6 7 8 9
    # Digits:    K S S S S S S P U U
    stamm = account[1:7]
    p_char = account[7]
    expected = _compute_check_method_17_from_stamm(stamm)
    return (ord(p_char) - 48) == expected


@register_generator("17")
def generate_account_method_17(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account for Method 17.

    We sample:
    - K: one digit 0..9
    - S: six digits (000000..999999)
    - Compute P from S per Method 17
    - U U: two digits 00..99
    """
    k = rng.randint(0, 9)
    stamm_num = rng.randint(0, 999_999)
    stamm = f"{stamm_num:06d}"
    p = _compute_check_method_17_from_stamm(stamm)
    uu = rng.randint(0, 99)
    account = f"{k:d}{stamm}{p:d}{uu:02d}"
    # Deterministic sanity check with our validator
    # (guards against implementation drift).
    # Not strictly necessary, but cheap and safe.
    # If this ever fails, it indicates a logic error above.
    assert validate_method_17(blz, account)
    return account
