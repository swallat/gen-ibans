"""
Method D0: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("D0")
def validate_method_D0(blz: str, account: str) -> bool:
    """Validate account number for method D0.

    Currently not implemented.
    """
    raise NotImplementedError("Method D0 validator not yet implemented")
