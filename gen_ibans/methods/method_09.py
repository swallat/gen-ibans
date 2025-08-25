"""
Method 09 (Bundesbank): Keine Prüfzifferberechnung (no check digit calculation).

Spec essentials:
- There is no computational check digit. The method does not define a validation
  algorithm beyond basic format.
- In this project, we interpret this as: any 10-digit numeric account number is
  considered valid for Method 09. BLZ is not used.

Notes:
- Leading zeros are allowed. The account must be exactly 10 digits (0-9).
- This replaces a previous Mod11 interpretation to comply with the provided spec
  "Keine Prüfzifferberechnung" for Method 09.
"""
from . import register, register_generator


@register("09")
def validate_method_09(blz: str, account: str) -> bool:
    """Validate according to Method 09: accept any 10-digit numeric string.

    Args:
        blz: Bankleitzahl (unused for this method).
        account: Account number string.
    Returns:
        True iff account is exactly 10 ASCII digits.
    """
    return len(account) == 10 and account.isdigit()


@register_generator("09")
def generate_account_method_09(blz: str, rng: __import__("random").Random) -> str:
    """Generate a 10-digit numeric account number valid for Method 09.

    We sample a 10-digit number uniformly (including leading zeros). To avoid
    the degenerate all-zero value, we replace it with "0000000001" for
    compatibility with broader project generation behavior.
    """
    num = rng.randint(0, 9_999_999_999)
    acc = f"{num:010d}"
    if acc == "0000000000":
        acc = "0000000001"
    # Defensive check
    assert validate_method_09(blz, acc)
    return acc
