"""
Method B1: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B1")
def validate_method_B1(blz: str, account: str) -> bool:
    """Validate account number for method B1.

    Currently not implemented.
    """
    raise NotImplementedError("Method B1 validator not yet implemented")
