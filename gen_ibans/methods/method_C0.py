"""
Method C0: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("C0")
def validate_method_C0(blz: str, account: str) -> bool:
    """Validate account number for method C0.

    Currently not implemented.
    """
    raise NotImplementedError("Method C0 validator not yet implemented")
