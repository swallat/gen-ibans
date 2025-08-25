"""
Method E9: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("E9")
def validate_method_E9(blz: str, account: str) -> bool:
    """Validate account number for method E9.

    Currently not implemented.
    """
    raise NotImplementedError("Method E9 validator not yet implemented")
