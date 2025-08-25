"""
Method C5 (Bundesbank): Variant-based procedure combining methods 75, 29, 00 and 09.

Spec summary (per provided text):
- Account numbers are 6- or 8- to 10-digit (including check digit). For the
  calculation, represent the account left-padded with zeros to 10 digits.
- The applicable variant is derived from the (padded) account number range:
  Variant 1 (like Method 75):
    a) 6-digit account; 5th digit in 1..8.
       Padded form: 0000 S(1-8) S S S S P  (check at pos 10),
       compute check over the five S digits with weights 2,1,2,1,2 using
       Modulus 10 with digit-sum (Method 00 rules).
    b) 9-digit account; 2nd digit in 1..8.
       Padded form: 0 S(1-8) S S S S P X X X (check at pos 7),
       compute check over positions 2..6 (five S digits) with weights 2,1,2,1,2.
  Variant 2 (like Method 29): 10-digit account; first digit in {1,4,5,6,9}.
       Modulus 10 with iterated transformation using the 4-row table.
  Variant 3 (like Method 00): 10-digit account; first digit = 3.
       Modulus 10 with alternating weights 2,1,... over the first 9 digits.
  Variant 4 (like Method 09): no check digit calculation for these ranges:
       - 8-digit accounts whose first digit is 3, 4, or 5 (padded range 0030000000..0059999999).
       - 10-digit accounts with first two digits 70 or 85.

Validation rule: If a number matches one of the specified ranges and the variant's
check calculation succeeds, it is valid; otherwise invalid.

Generator: Produces 10-digit accounts exclusively (padded representation) drawn
from the allowed ranges, computing check digits deterministically for variants 1–3
and directly sampling ranges for variant 4.
"""
from . import register, register_generator

# -----------------------------
# Helpers: common Mod10 (Method 00 style)
# -----------------------------

def _qsum_prod(d: int, weight: int) -> int:
    """Return digit-sum of d*weight where weight is 1 or 2 (Method 00 style)."""
    prod = d * weight
    if prod >= 10:
        return (prod // 10) + (prod % 10)
    return prod


def _compute_check_method00(payload9: str) -> int:
    """Compute Mod10 alternating 2,1 starting from the rightmost payload digit.

    This corresponds to Method 00 applied to the first 9 digits with
    weights (from left-to-right): 2,1,2,1,2,1,2,1,2.
    """
    assert len(payload9) == 9 and payload9.isdigit()
    total = 0
    # Right-to-left on the payload, starting with weight 2
    w = 2
    for ch in reversed(payload9):
        d = ord(ch) - 48
        total += _qsum_prod(d, w)
        w = 1 if w == 2 else 2
    return (10 - (total % 10)) % 10


# -----------------------------
# Helpers: Method 75 (weights over 5-digit Stammnummer S)
# -----------------------------

def _compute_check_method75_over_stamm5(stamm5: str) -> int:
    """Compute check digit per Method 75 rules over a 5-digit Stammnummer.

    Multiply the five S digits left-to-right by weights 2,1,2,1,2 (with digit-sum
    reduction for two-digit products), sum, and take Mod10 complement.
    """
    assert len(stamm5) == 5 and stamm5.isdigit()
    weights = (2, 1, 2, 1, 2)
    total = 0
    for ch, w in zip(stamm5, weights):
        total += _qsum_prod(ord(ch) - 48, w)
    return (10 - (total % 10)) % 10


# -----------------------------
# Helpers: Method 29 (iterated transformation)
# -----------------------------
_TRANS_ROWS = (
    # 1-based rows described in the spec; store 0-based tuple indices: row1..row4
    (0, 1, 5, 9, 3, 7, 4, 8, 2, 6),  # Row 1
    (0, 1, 7, 6, 9, 8, 3, 2, 5, 4),  # Row 2
    (0, 1, 8, 4, 6, 2, 9, 5, 7, 3),  # Row 3
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),  # Row 4
)


def _compute_check_method29(payload9: str) -> int:
    """Compute Method 29 check digit for a 9-digit payload using iterated transformation.

    Apply transformation from right to left with row sequence 1,2,3,4,1,2,3,4,1
    to the 9 payload digits, sum the transformed values, and compute
    (10 - (sum % 10)) % 10.
    """
    assert len(payload9) == 9 and payload9.isdigit()
    total = 0
    # Iterate right-to-left; for rightmost payload digit use row 1, then 2,3,4,1,...
    row_index = 0  # 0->row1,1->row2,2->row3,3->row4
    for ch in reversed(payload9):
        d = ord(ch) - 48
        mapped = _TRANS_ROWS[row_index][d]
        total += mapped
        row_index = (row_index + 1) % 4
    return (10 - (total % 10)) % 10


# -----------------------------
# Variant selection
# -----------------------------

def _select_variant_and_compute(blz: str, account: str) -> bool:
    """Validate a given account according to C5, selecting the appropriate variant.

    Returns True if valid; False otherwise.
    """
    if not account.isdigit():
        return False
    n = len(account)
    if n not in (6, 8, 9, 10):
        return False
    a10 = account.zfill(10)

    # Variant 4: no check for specific ranges
    #  - 8-digit accounts with first digit 3,4,5 (padded range 0030000000..0059999999)
    if n == 8 and account[0] in "345":
        return True
    #  - 10-digit accounts starting with 003, 004, 005
    if n == 10 and (a10.startswith("003") or a10.startswith("004") or a10.startswith("005")):
        return True
    #  - 10-digit accounts starting with 70 or 85
    if n == 10 and (a10.startswith("70") or a10.startswith("85")):
        return True

    # Variant 1a: 6-digit accounts OR 10-digit padded form 0000S....; 5th digit in 1..8
    if (n == 6 and a10[4] in "12345678") or (n == 10 and a10.startswith("0000") and a10[4] in "12345678"):
        stamm5 = a10[4:9]
        p = ord(a10[9]) - 48
        expected = _compute_check_method75_over_stamm5(stamm5)
        return p == expected

    # Variant 1b: 9-digit accounts OR 10-digit padded form 0S....; 2nd digit in 1..8
    if (n == 9 and a10[1] in "12345678") or (n == 10 and a10[0] == "0" and a10[1] in "12345678"):
        stamm5 = a10[1:6]
        p = ord(a10[6]) - 48
        expected = _compute_check_method75_over_stamm5(stamm5)
        return p == expected

    # Variant 2: 10-digit; first digit in {1,4,5,6,9}
    if n == 10 and a10[0] in "14569":
        payload9, p_char = a10[:9], a10[9]
        expected = _compute_check_method29(payload9)
        return (ord(p_char) - 48) == expected

    # Variant 3: 10-digit; first digit == 3
    if n == 10 and a10[0] == "3":
        payload9, p_char = a10[:9], a10[9]
        expected = _compute_check_method00(payload9)
        return (ord(p_char) - 48) == expected

    return False


@register("C5")
def validate_method_C5(blz: str, account: str) -> bool:
    return _select_variant_and_compute(blz, account)


# -----------------------------
# Generator
# -----------------------------

@register_generator("C5")
def generate_account_method_C5(blz: str, rng: __import__("random").Random) -> str:
    """Generate a valid 10-digit account number according to method C5.

    We always return a 10-digit padded representation. We sample among
    the following variant families and construct deterministically:
      - V1a (6-digit form -> 10-digit padded 0000 S S S S S P)
      - V1b (9-digit form -> 10-digit padded 0 S S S S S P X X X)
      - V2 (10-digit starting with 1,4,5,6,9; check by Method 29)
      - V3 (10-digit starting with 3; check by Method 00)
      - V4 (10-digit starting with 003/004/005 or 70/85; no check)
    """
    choice = rng.randint(0, 4)

    if choice == 0:
        # Variant 1a: build 0000 S S S S S P, with S1 in 1..8
        s1 = rng.randint(1, 8)
        s_rest = rng.randint(0, 9999)
        stamm5 = f"{s1:d}{s_rest:04d}"
        p = _compute_check_method75_over_stamm5(stamm5)
        return f"0000{stamm5}{p:d}"

    if choice == 1:
        # Variant 1b: 0 S S S S S P X X X, with S1 in 1..8
        s1 = rng.randint(1, 8)
        s_rest = rng.randint(0, 9999)
        stamm5 = f"{s1:d}{s_rest:04d}"
        p = _compute_check_method75_over_stamm5(stamm5)
        xxx = rng.randint(0, 999)
        return f"0{stamm5}{p:d}{xxx:03d}"

    if choice == 2:
        # Variant 2: 10-digit; first digit in {1,4,5,6,9}
        first = rng.choice(["1", "4", "5", "6", "9"])
        mid = rng.randint(0, 999_999_99)  # next 8 digits (pos 2..9 overall)
        payload9 = f"{first}{mid:08d}"
        p = _compute_check_method29(payload9)
        return payload9 + str(p)

    if choice == 3:
        # Variant 3: 10-digit; first digit = 3
        first = "3"
        mid = rng.randint(0, 999_999_99)
        payload9 = f"{first}{mid:08d}"
        p = _compute_check_method00(payload9)
        return payload9 + str(p)

    # choice == 4 -> Variant 4 (no check). Two sub-ranges.
    if rng.random() < 0.5:
        # 003/004/005xxxxxxxx
        prefix = rng.choice(["003", "004", "005"])
        rest = rng.randint(0, 9_999_999)  # remaining 7 digits
        return f"{prefix}{rest:07d}"
    else:
        # 70xxxxxxxx or 85xxxxxxxx
        prefix = rng.choice(["70", "85"])
        rest = rng.randint(0, 99_999_999)
        return f"{prefix}{rest:08d}"
