"""
Method C2: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("C2")
def validate_method_C2(blz: str, account: str) -> bool:
    """Validate account number for method C2.

    Currently not implemented.
    """
    raise NotImplementedError("Method C2 validator not yet implemented")
