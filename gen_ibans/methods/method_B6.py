"""
Method B6: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B6")
def validate_method_B6(blz: str, account: str) -> bool:
    """Validate account number for method B6.

    Currently not implemented.
    """
    raise NotImplementedError("Method B6 validator not yet implemented")
