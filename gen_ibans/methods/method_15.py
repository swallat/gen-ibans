"""
Method 15: Delegates to method 05 (Luhn/Mod10 over first 9 digits).
Temporary alias until a dedicated specification is required.
"""
from . import register, register_generator
from .method_05 import validate_method_05, generate_account_method_05


@register("15")
def validate_method_15(blz: str, account: str) -> bool:
    """Validate account number for method 15 via method 05 rules."""
    return validate_method_05(blz, account)


@register_generator("15")
def generate_account_method_15(blz: str, rng: __import__("random").Random) -> str:
    return generate_account_method_05(blz, rng)
