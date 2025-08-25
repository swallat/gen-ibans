"""
Method D8: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("D8")
def validate_method_D8(blz: str, account: str) -> bool:
    """Validate account number for method D8.

    Currently not implemented.
    """
    raise NotImplementedError("Method D8 validator not yet implemented")
