"""
Method C9: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("C9")
def validate_method_C9(blz: str, account: str) -> bool:
    """Validate account number for method C9.

    Currently not implemented.
    """
    raise NotImplementedError("Method C9 validator not yet implemented")
