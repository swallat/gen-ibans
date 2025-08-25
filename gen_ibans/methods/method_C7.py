"""
Method C7: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("C7")
def validate_method_C7(blz: str, account: str) -> bool:
    """Validate account number for method C7.

    Currently not implemented.
    """
    raise NotImplementedError("Method C7 validator not yet implemented")
