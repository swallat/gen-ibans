"""
Method B4: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B4")
def validate_method_B4(blz: str, account: str) -> bool:
    """Validate account number for method B4.

    Currently not implemented.
    """
    raise NotImplementedError("Method B4 validator not yet implemented")
