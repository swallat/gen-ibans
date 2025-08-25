"""
Method 99: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("99")
def validate_method_99(blz: str, account: str) -> bool:
    """Validate account number for method 99.

    Currently not implemented.
    """
    raise NotImplementedError("Method 99 validator not yet implemented")
