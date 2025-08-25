"""
Method 21: Delegates to method 05 (Luhn/Mod10 over first 9 digits).
Temporary alias until a dedicated specification is required.
"""
from . import register, register_generator
from .method_05 import validate_method_05, generate_account_method_05


@register("21")
def validate_method_21(blz: str, account: str) -> bool:
    """Validate account number for method 21 via method 05 rules."""
    return validate_method_05(blz, account)


@register_generator("21")
def generate_account_method_21(blz: str, rng: __import__("random").Random) -> str:
    return generate_account_method_05(blz, rng)
