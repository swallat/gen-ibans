"""
Method B2: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B2")
def validate_method_B2(blz: str, account: str) -> bool:
    """Validate account number for method B2.

    Currently not implemented.
    """
    raise NotImplementedError("Method B2 validator not yet implemented")
