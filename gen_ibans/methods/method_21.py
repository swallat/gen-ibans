"""
Method 21: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("21")
def validate_method_21(blz: str, account: str) -> bool:
    """Validate account number for method 21.

    Currently not implemented.
    """
    raise NotImplementedError("Method 21 validator not yet implemented")
