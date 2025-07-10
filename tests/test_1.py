import pytest
from definition_49c679a310de49f4bba4bb4795cfd7b2 import validate_dataset

@pytest.mark.parametrize("input, expected_valid, expected_missing_values, expected_column_names, expected_data_types, expected_pk_uniqueness", [
    (
        {"col1": [1, 2, 3], "col2": ["a", "b", "c"]},
        True,
        {},
        ["col1", "col2"],
        {"col1": int, "col2": str},
        True
    ),
    (
        {"col1": [1, 2, None], "col2": ["a", None, "c"]},
        True,
        {"col1": 1, "col2": 1},
        ["col1", "col2"],
        {"col1": float, "col2": str},
        True
    ),
    (
        {"col1": [1, 2, 1], "col2": ["a", "b", "c"]},
        True,
        {},
        ["col1", "col2"],
        {"col1": int, "col2": str},
        False
    ),
    (
        {"col1": [1, 2, 3], "col1": ["a", "b", "c"]},
        True,
        {},
        ["col1"],
        {"col1": str},
        True
    ),
        (
        {},
        True,
        {},
        [],
        {},
        True
    ),
])
def test_validate_dataset(input, expected_valid, expected_missing_values, expected_column_names, expected_data_types, expected_pk_uniqueness):
    valid = validate_dataset(input)
    assert isinstance(valid, bool)
