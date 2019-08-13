import numpy as np
import pytest

from edsger.sssp import convert_sorted_graph_to_csr, sssp_basic
from edsger.commons import INFINITY_PY


@pytest.fixture
def braess_network_01():
    csr_indices = np.array([1, 2, 2, 3, 3], dtype=np.uint32)
    csr_indptr = np.array([0, 2, 4, 5, 5], dtype=np.uint32)
    edge_weights = np.array([1.0, 2.0, 0.0, 2.0, 1.0], dtype=np.float)
    return csr_indices, csr_indptr, edge_weights


def test_convert_01():
    tail_nodes = np.array([0, 0, 1, 1, 2])
    head_nodes = np.array([1, 2, 2, 3, 3])

    indptr_ref = np.array([0, 2, 4, 5, 5], dtype=np.uint32)
    indptr = convert_sorted_graph_to_csr(tail_nodes, head_nodes, 4)

    assert isinstance(indptr, np.ndarray)
    np.testing.assert_array_equal(indptr_ref, indptr)
    assert np.issubdtype(indptr.dtype, np.integer)


def test_sssp_01(braess_network_01):
    csr_indices, csr_indptr, edge_weights = braess_network_01

    travel_time_ref = np.array([0.0, 1.0, 1.0, 2.0], dtype=np.float)
    travel_time = sssp_basic(csr_indices, csr_indptr, edge_weights, 0, 4)

    assert isinstance(travel_time, np.ndarray)
    np.testing.assert_array_equal(travel_time_ref, travel_time)
    assert np.issubdtype(travel_time.dtype, np.floating)


def test_sssp_02(braess_network_01):
    csr_indices, csr_indptr, edge_weights = braess_network_01

    travel_time_ref = np.ones(4, dtype=np.float)
    # travel_time = sssp_basic(csr_indices, csr_indptr, edge_weights, 4, 0)
    print(INFINITY_PY)
    # print(travel_time)
    # assert isinstance(travel_time, np.ndarray)
    # np.testing.assert_array_equal(travel_time_ref, travel_time)
    # assert np.issubdtype(travel_time.dtype, np.floating)
    assert True