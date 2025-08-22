"""
Method 02: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("02")
def validate_method_02(blz: str, account: str) -> bool:
    """Validate account number for method 02.

    Currently not implemented.
    """
    raise NotImplementedError("Method 02 validator not yet implemented")
