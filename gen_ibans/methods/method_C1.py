"""
Method C1 (Bundesbank): Two-variant Modulus 11 procedure.

Spec summary (per provided text):
- The account number is 10 digits including the check digit (P). For the
  calculation it must be represented as a 10-digit number by left-padding
  with zeros if necessary.
- Variant selection:
  * If the first digit (of the 10-digit representation) is not "5": use Variant 1.
  * If the first digit is "5": use Variant 2.

Variant 1:
- "Die Berechnung und mögliche Ergebnisse entsprechen der Methode 17."
  That is, the check digit P is computed exactly like Method 17:
  * Layout: K S S S S S S P U U (10 digits)
  * Take the 6-digit Stammnummer S at positions 2..7 (index 1..6 in 0-based)
  * Multiply left-to-right with weights [1,2,1,2,1,2]. For weight-2 positions,
    reduce two-digit products by digit sum (Quersumme).
  * Sum all six contributions, subtract 1, take modulo 11: r = (sum-1) % 11.
  * If r == 0 -> P = 0, else P = 10 - r.
  * Valid iff digit at position 8 (index 7) equals P.
  If the calculation does not match the given check digit, the account is invalid.

Variant 2 (first digit == '5'):
- Use the first 9 digits (positions 1..9) with weights 1,2,1,2,1,2,1,2,1 applied
  left-to-right. For the positions with weight 2 (2nd, 4th, 6th, 8th) reduce
  two-digit products by digit sum. Sum the contributions, subtract 1, divide by 11
  (i.e., r = (sum-1) % 11). If r == 0 -> P = 0, else P = 10 - r. Valid iff last
  digit equals P.

Notes:
- BLZ is not used for the calculation.
- We accept numeric input up to 10 digits and left-pad with zeros for the
  computation. The public API always returns/generates 10-digit account numbers.
"""
from . import register, register_generator


def _qsum(n: int) -> int:
    """Digit sum of a non-negative integer n (only up to 18 here)."""
    return (n // 10) + (n % 10)


def _compute_check_variant1_from_account10(a10: str) -> int:
    """Compute the Variant 1 (Method 17-equivalent) check digit P from a 10-digit account.

    Positions (0-based): 0 1 2 3 4 5 6 7 8 9
                         K S S S S S S P U U
    Weights over S(1..6): 1,2,1,2,1,2 with Quersumme for the weight-2 positions.
    """
    stamm6 = a10[1:7]
    weights = (1, 2, 1, 2, 1, 2)
    total = 0
    for ch, w in zip(stamm6, weights):
        d = ord(ch) - 48
        prod = d * w
        if w == 2:
            prod = _qsum(prod)
        total += prod
    r = (total - 1) % 11
    if r == 0:
        return 0
    return 10 - r


def _compute_check_variant2_from_payload9(payload9: str) -> int:
    """Compute the Variant 2 check digit from the 9-digit payload (positions 1..9).

    Weights left-to-right: 1,2,1,2,1,2,1,2,1; apply Quersumme on weight-2 positions.
    Then subtract 1, modulo 11; check digit = 0 if remainder 0 else 10 - remainder.
    """
    weights = (1, 2, 1, 2, 1, 2, 1, 2, 1)
    total = 0
    for ch, w in zip(payload9, weights):
        d = ord(ch) - 48
        prod = d * w
        if w == 2:
            prod = _qsum(prod)
        total += prod
    r = (total - 1) % 11
    if r == 0:
        return 0
    return 10 - r


@register("C1")
def validate_method_C1(blz: str, account: str) -> bool:
    """Validate an account number according to Bundesbank Method C1.

    Accept numeric strings of length 1..10, left-pad with zeros to 10 digits for
    the calculation. Return True iff the number satisfies the corresponding
    variant's check digit rule.
    """
    if not account or not account.isdigit() or len(account) > 10:
        return False
    a10 = account.zfill(10)
    if a10[0] == "5":
        # Variant 2 over positions 0..8 (1..9 human-readable)
        payload9 = a10[:9]
        expected = _compute_check_variant2_from_payload9(payload9)
        return (ord(a10[9]) - 48) == expected
    else:
        # Variant 1: Method 17-equivalent; check at position 7
        expected = _compute_check_variant1_from_account10(a10)
        return (ord(a10[7]) - 48) == expected


@register_generator("C1")
def generate_account_method_C1(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account number according to Method C1.

    We produce both variants:
    - With probability 1/2, Variant 2 (first digit '5'): construct payload9 and
      compute the check digit directly.
    - Otherwise, Variant 1 (first digit != '5'): construct a K!=5 and a 6-digit
      stamm, compute P per Method 17 equivalent, and append two trailing digits.
    """
    if rng.random() < 0.5:
        # Variant 2: first digit must be '5'
        k = 5
        mid = rng.randint(0, 99_999_99)  # next 8 digits for positions 2..9 overall
        payload9 = f"{k}{mid:08d}"
        p = _compute_check_variant2_from_payload9(payload9)
        return payload9 + str(p)
    else:
        # Variant 1: choose K in 0..9 except 5
        k = rng.choice([0, 1, 2, 3, 4, 6, 7, 8, 9])
        stamm_num = rng.randint(0, 999_999)
        stamm6 = f"{stamm_num:06d}"
        # Build temporary string to compute the check digit (we don't need U U yet)
        tmp = f"{k}{stamm6}0"  # placeholder P at pos 8
        # But _compute_check_variant1 works on full 10 digits; we can append UU=00 for calc
        a10_for_calc = tmp + "00"
        p = _compute_check_variant1_from_account10(a10_for_calc)
        uu = rng.randint(0, 99)
        account = f"{k}{stamm6}{p}{uu:02d}"
        # Defensive validation
        assert validate_method_C1(blz, account)
        return account
