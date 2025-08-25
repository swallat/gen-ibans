"""
Method C8: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("C8")
def validate_method_C8(blz: str, account: str) -> bool:
    """Validate account number for method C8.

    Currently not implemented.
    """
    raise NotImplementedError("Method C8 validator not yet implemented")
