"""
Method C3: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("C3")
def validate_method_C3(blz: str, account: str) -> bool:
    """Validate account number for method C3.

    Currently not implemented.
    """
    raise NotImplementedError("Method C3 validator not yet implemented")
