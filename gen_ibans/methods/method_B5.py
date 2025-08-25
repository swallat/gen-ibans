"""
Method B5: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B5")
def validate_method_B5(blz: str, account: str) -> bool:
    """Validate account number for method B5.

    Currently not implemented.
    """
    raise NotImplementedError("Method B5 validator not yet implemented")
