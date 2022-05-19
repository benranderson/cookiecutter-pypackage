"""Module unit tests."""

import numpy as np
import pytest

from {{ cookiecutter.project_slug }} import module


@pytest.fixture(scope="module")
def data():
    return {
        "a": np.array([1, 2, 3]),
        "b": np.array([2, 4, 6]),
        "c": np.array([1, 1, 1]),
        "result_1": np.array([2, 8, 18]),
        "result_2": np.array([3, 9, 19]),
    }


@pytest.fixture(scope="module")
def results(data):
    return module.main(data["a"], data["b"], data["c"])


@pytest.mark.parametrize("param", ["result_1", "result_2"])
def test_get_result(param, data, results):
    np.testing.assert_equal(results[param], data[param])
