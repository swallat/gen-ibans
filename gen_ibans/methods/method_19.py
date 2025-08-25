"""
Method 19: Delegates to method 09 (Mod11 with repeating weights [2..7]).
Temporary alias until a dedicated specification is required.
"""
from . import register, register_generator
from .method_09 import validate_method_09, generate_account_method_09


@register("19")
def validate_method_19(blz: str, account: str) -> bool:
    """Validate account number for method 19 via method 09 rules."""
    return validate_method_09(blz, account)


@register_generator("19")
def generate_account_method_19(blz: str, rng: __import__("random").Random) -> str:
    return generate_account_method_09(blz, rng)
