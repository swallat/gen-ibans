"""
Method B0: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B0")
def validate_method_B0(blz: str, account: str) -> bool:
    """Validate account number for method B0.

    Currently not implemented.
    """
    raise NotImplementedError("Method B0 validator not yet implemented")
