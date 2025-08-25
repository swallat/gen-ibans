"""
Method D4: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("D4")
def validate_method_D4(blz: str, account: str) -> bool:
    """Validate account number for method D4.

    Currently not implemented.
    """
    raise NotImplementedError("Method D4 validator not yet implemented")
