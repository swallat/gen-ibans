"""
Method B9: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B9")
def validate_method_B9(blz: str, account: str) -> bool:
    """Validate account number for method B9.

    Currently not implemented.
    """
    raise NotImplementedError("Method B9 validator not yet implemented")
