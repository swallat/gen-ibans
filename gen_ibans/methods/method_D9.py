"""
Method D9: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("D9")
def validate_method_D9(blz: str, account: str) -> bool:
    """Validate account number for method D9.

    Currently not implemented.
    """
    raise NotImplementedError("Method D9 validator not yet implemented")
