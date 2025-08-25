"""
Method D7: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("D7")
def validate_method_D7(blz: str, account: str) -> bool:
    """Validate account number for method D7.

    Currently not implemented.
    """
    raise NotImplementedError("Method D7 validator not yet implemented")
