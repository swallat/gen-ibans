"""
Method E3: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("E3")
def validate_method_E3(blz: str, account: str) -> bool:
    """Validate account number for method E3.

    Currently not implemented.
    """
    raise NotImplementedError("Method E3 validator not yet implemented")
