"""
Method 22: Delegates to method 06 (Mod11 with weights [2..10]).
Temporary alias until a dedicated specification is required.
"""
from . import register, register_generator
from .method_06 import validate_method_06, generate_account_method_06


@register("22")
def validate_method_22(blz: str, account: str) -> bool:
    """Validate account number for method 22 via method 06 rules."""
    return validate_method_06(blz, account)


@register_generator("22")
def generate_account_method_22(blz: str, rng: __import__("random").Random) -> str:
    return generate_account_method_06(blz, rng)
