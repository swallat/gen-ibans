"""
Method 14: Delegates to method 04 (simple Mod10 over first 9 digits).
Temporary alias until a dedicated specification is required.
"""
from . import register, register_generator
from .method_04 import validate_method_04, generate_account_method_04


@register("14")
def validate_method_14(blz: str, account: str) -> bool:
    """Validate account number for method 14 via method 04 rules."""
    return validate_method_04(blz, account)


@register_generator("14")
def generate_account_method_14(blz: str, rng: __import__("random").Random) -> str:
    return generate_account_method_04(blz, rng)
