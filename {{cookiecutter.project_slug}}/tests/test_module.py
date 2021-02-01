"""Module unit tests."""

import numpy as np
import pytest

from {{ cookiecutter.project_slug }} import module


@pytest.fixture
def data():
    return {
        "a": np.array([1, 2, 3]),
        "b": np.array([2, 4, 6]),
        "result": np.array([2, 8, 18]),
    }


def test_get_result(data):
    actual = module.get_result(data["a"], data["b"])
    np.testing.assert_equal(actual, data["result"])
