"""
Method 12: Frei (unassigned) per Deutsche Bundesbank specification.

This method is intentionally not implemented. Any attempt to validate or
generate an account number using method code "12" will raise a
NotImplementedError.

Rationale:
- The official Bundesbank catalog marks method code 12 as "frei" (unassigned).
- To avoid silent acceptance or random generation of meaningless accounts, the
  API explicitly signals that this method is not available.
"""
from . import register, register_generator


@register("12")
def validate_method_12(blz: str, account: str) -> bool:
    """Validate account number for method 12 (not implemented; free code)."""
    raise NotImplementedError("Method 12 is unassigned per Bundesbank and not implemented")


@register_generator("12")
def generate_account_method_12(blz: str, rng: __import__("random").Random) -> str:
    """Generator for method 12 (not implemented; free code)."""
    raise NotImplementedError("Method 12 is unassigned per Bundesbank and not implementable")
