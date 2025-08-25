"""
Method 18: Delegates to method 03 (Mod11 with weights [2..7]).
Temporary alias until a dedicated specification is required.
"""
from . import register, register_generator
from .method_03 import validate_method_03, generate_account_method_03


@register("18")
def validate_method_18(blz: str, account: str) -> bool:
    """Validate account number for method 18 via method 03 rules."""
    return validate_method_03(blz, account)


@register_generator("18")
def generate_account_method_18(blz: str, rng: __import__("random").Random) -> str:
    return generate_account_method_03(blz, rng)
