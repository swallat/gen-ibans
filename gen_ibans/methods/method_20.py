"""
Method 20: Delegates to method 24 (Mod11 with weights [2,3,4,5,6,7,8,9,2]).
Temporary alias until a dedicated specification is required.
"""
from . import register, register_generator
from .method_24 import validate_method_24, generate_account_method_24


@register("20")
def validate_method_20(blz: str, account: str) -> bool:
    """Validate account number for method 20 via method 24 rules."""
    return validate_method_24(blz, account)


@register_generator("20")
def generate_account_method_20(blz: str, rng: __import__("random").Random) -> str:
    return generate_account_method_24(blz, rng)
