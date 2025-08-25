"""
Method D2: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("D2")
def validate_method_D2(blz: str, account: str) -> bool:
    """Validate account number for method D2.

    Currently not implemented.
    """
    raise NotImplementedError("Method D2 validator not yet implemented")
