"""
Method E5: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("E5")
def validate_method_E5(blz: str, account: str) -> bool:
    """Validate account number for method E5.

    Currently not implemented.
    """
    raise NotImplementedError("Method E5 validator not yet implemented")
