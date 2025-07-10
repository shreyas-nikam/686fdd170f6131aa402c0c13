import pytest
from definition_8d07b72f87874ec2a2db6bef81b2c66c import load_synthetic_hr_document

@pytest.mark.parametrize("document_type, complexity_level, expected_type", [
    ("Benefits Plan", "Simple", dict),
    ("Compensation Matrix", "Hierarchical", dict),
    ("Performance Review", 1, dict),
    ("Invalid Document", "Simple", None),
    ("Benefits Plan", "Invalid Complexity", None),
])

def test_load_synthetic_hr_document(document_type, complexity_level, expected_type):
    result = load_synthetic_hr_document(document_type, complexity_level)
    if expected_type is not None:
        assert isinstance(result, expected_type)
    else:
        assert result is None
