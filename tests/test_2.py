import pytest
from definition_b0a79ea3574445a2b137026daf943031 import simulate_traditional_ocr_extraction

@pytest.mark.parametrize("document_data, expected_type", [
    ({"table": [["header1", "header2"], ["data1", "data2"]]}, str),
    ({}, str),
    ({"empty": []}, str),
    ({"numbers": [[1,2],[3,4]]}, str),
    ({"mixed": [["header"],[1]]}, str)
])

def test_simulate_traditional_ocr_extraction(document_data, expected_type):
    result = simulate_traditional_ocr_extraction(document_data)
    assert isinstance(result, expected_type)

