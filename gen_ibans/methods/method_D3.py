"""
Method D3: Placeholder stub.
TODO: Implement per Bundesbank specification.
"""
from . import register


@register("D3")
def validate_method_D3(blz: str, account: str) -> bool:
    """Validate account number for method D3.

    Currently not implemented.
    """
    raise NotImplementedError("Method D3 validator not yet implemented")
