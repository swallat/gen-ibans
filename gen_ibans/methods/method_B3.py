"""
Method B3: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("B3")
def validate_method_B3(blz: str, account: str) -> bool:
    """Validate account number for method B3.

    Currently not implemented.
    """
    raise NotImplementedError("Method B3 validator not yet implemented")
