"""
Method E0: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("E0")
def validate_method_E0(blz: str, account: str) -> bool:
    """Validate account number for method E0.

    Currently not implemented.
    """
    raise NotImplementedError("Method E0 validator not yet implemented")
