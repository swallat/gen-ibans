"""
Method D6: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("D6")
def validate_method_D6(blz: str, account: str) -> bool:
    """Validate account number for method D6.

    Currently not implemented.
    """
    raise NotImplementedError("Method D6 validator not yet implemented")
