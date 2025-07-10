import pytest
from definition_792711b30e4748caa228766d158bb0ea import calculate_simulated_metrics

@pytest.mark.parametrize("extracted_data, ground_truth, method_type, expected_accuracy, expected_info_not_found", [
    ({"question1": "answer1"}, {"question1": "answer1"}, "TalentMine", 1.0, 0.0),
    ({"question1": "answer1"}, {"question1": "answer2"}, "Textract", 0.0, 1.0),
    ({"question1": "answer1", "question2": "answer2"}, {"question1": "answer1", "question2": "answer3"}, "TalentMine", 0.5, 0.5),
    ({}, {"question1": "answer1"}, "TalentMine", 0.0, 1.0),
    ({"question1": "answer1"}, {}, "TalentMine", 1.0, 0.0)
])

def test_calculate_simulated_metrics(extracted_data, ground_truth, method_type, expected_accuracy, expected_info_not_found):
    result = calculate_simulated_metrics(extracted_data, ground_truth, method_type)
    assert isinstance(result, dict)
    assert "accuracy" in result
    assert "information_not_found" in result
    assert result["accuracy"] == expected_accuracy
    assert result["information_not_found"] == expected_info_not_found
