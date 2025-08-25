"""
Method B8: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B8")
def validate_method_B8(blz: str, account: str) -> bool:
    """Validate account number for method B8.

    Currently not implemented.
    """
    raise NotImplementedError("Method B8 validator not yet implemented")
