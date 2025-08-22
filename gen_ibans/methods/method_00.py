"""
Method 00: No check digit (or not validated) — accepts any 10-digit account number.
Reference: Some banks specify method 00 meaning no check is applied.
"""
from . import register


@register("00")
def validate_method_00(blz: str, account: str) -> bool:
    return len(account) == 10 and account.isdigit()
