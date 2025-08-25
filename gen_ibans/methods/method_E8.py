"""
Method E8: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("E8")
def validate_method_E8(blz: str, account: str) -> bool:
    """Validate account number for method E8.

    Currently not implemented.
    """
    raise NotImplementedError("Method E8 validator not yet implemented")
