"""
Method D5: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("D5")
def validate_method_D5(blz: str, account: str) -> bool:
    """Validate account number for method D5.

    Currently not implemented.
    """
    raise NotImplementedError("Method D5 validator not yet implemented")
