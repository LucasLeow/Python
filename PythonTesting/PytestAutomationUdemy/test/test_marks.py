import pytest
import sys


@pytest.mark.skip(reason="cannot test for now")
def test_case01():
    assert type(5) == float


@pytest.mark.skipif(pytest.__version__ < '5.5.0', reason="pytest version not up to date")
def test_case02():
    assert 'hi' == 32