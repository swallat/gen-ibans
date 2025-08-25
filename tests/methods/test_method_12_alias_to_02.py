# MIT License
#
# Tests for Bundesbank method 12: method code is marked as "frei" (unassigned).
# Therefore, the validator must raise NotImplementedError when invoked.

import pytest

from gen_ibans.methods.method_12 import validate_method_12


def test_method_12_raises_not_implemented_error():
    blz = "10000000"
    # Try a few sample inputs; all should raise NotImplementedError
    samples = [
        "0000000000",
        "1234567890",
        "9999999999",
    ]
    for acc in samples:
        with pytest.raises(NotImplementedError):
            validate_method_12(blz, acc)
