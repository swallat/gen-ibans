"""
Method B7: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B7")
def validate_method_B7(blz: str, account: str) -> bool:
    """Validate account number for method B7.

    Currently not implemented.
    """
    raise NotImplementedError("Method B7 validator not yet implemented")
