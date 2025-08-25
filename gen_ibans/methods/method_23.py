"""
Method 23: Delegates to method 07 (Mod11 with repeating weights [2..7]).
Temporary alias until a dedicated specification is required.
"""
from . import register, register_generator
from .method_07 import validate_method_07, generate_account_method_07


@register("23")
def validate_method_23(blz: str, account: str) -> bool:
    """Validate account number for method 23 via method 07 rules."""
    return validate_method_07(blz, account)


@register_generator("23")
def generate_account_method_23(blz: str, rng: __import__("random").Random) -> str:
    return generate_account_method_07(blz, rng)
