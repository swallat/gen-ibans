"""
Method 11: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("11")
def validate_method_11(blz: str, account: str) -> bool:
    """Validate account number for method 11.

    Currently not implemented.
    """
    raise NotImplementedError("Method 11 validator not yet implemented")
