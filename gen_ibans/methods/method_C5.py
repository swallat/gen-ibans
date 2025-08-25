"""
Method C5: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("C5")
def validate_method_C5(blz: str, account: str) -> bool:
    """Validate account number for method C5.

    Currently not implemented.
    """
    raise NotImplementedError("Method C5 validator not yet implemented")
