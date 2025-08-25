"""
Method C4: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("C4")
def validate_method_C4(blz: str, account: str) -> bool:
    """Validate account number for method C4.

    Currently not implemented.
    """
    raise NotImplementedError("Method C4 validator not yet implemented")
