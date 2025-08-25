"""
Method 12: Frei (unassigned) per Deutsche Bundesbank specification.

This method is intentionally not implemented. Any attempt to validate an
account number using method code "12" will raise a NotImplementedError.
"""
from . import register


@register("12")
def validate_method_12(blz: str, account: str) -> bool:
    """Validate account number for method 12 (not implemented; free code)."""
    raise NotImplementedError("Method 12 is unassigned per Bundesbank and not implemented")
