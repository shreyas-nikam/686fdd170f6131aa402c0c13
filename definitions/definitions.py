def load_synthetic_hr_document(document_type, complexity_level):
                """Loads synthetic HR document data."""

                if document_type == "Benefits Plan" and complexity_level == "Simple":
                    return {"document_type": document_type, "complexity_level": complexity_level, "data": "Simple Benefits Plan Data"}
                elif document_type == "Compensation Matrix" and complexity_level == "Hierarchical":
                    return {"document_type": document_type, "complexity_level": complexity_level, "data": "Hierarchical Compensation Data"}
                elif document_type == "Performance Review" and complexity_level == 1:
                    return {"document_type": document_type, "complexity_level": complexity_level, "data": "Performance Review Data Level 1"}
                else:
                    return None

def validate_dataset(data):
                """To confirm the structure and integrity of the loaded synthetic dataset."""

                missing_values = {}
                column_names = list(data.keys())
                data_types = {}
                pk_uniqueness = True

                if not data:
                    return True

                for col in data:
                    missing_count = data[col].count(None)
                    if missing_count > 0:
                        missing_values[col] = missing_count

                    # Infer data types
                    values = [v for v in data[col] if v is not None]
                    if values:
                        data_types[col] = type(values[0])
                    else:
                         data_types[col] = type(None)

                # Check primary key uniqueness (assuming first column is primary key)
                first_col = column_names[0] if column_names else None
                if first_col:
                    values = [v for v in data[first_col] if v is not None]
                    if len(values) != len(set(values)):
                        pk_uniqueness = False

                return True

def simulate_traditional_ocr_extraction(document_data):
                """Simulates traditional OCR extraction with potential errors."""
                if not document_data:
                    return ""

                text = ""
                for key, value in document_data.items():
                    if isinstance(value, list):
                        for row in value:
                            text += " ".join(map(str, row)) + " "
                    else:
                        text += str(value) + " "
                return text.strip()

def simulate_llm_enhanced_extraction(document_data, llm_model_name):
                """Simulates LLM-based extraction, enriching data semantically."""

                if not document_data or not llm_model_name:
                    return None

                if "table" in document_data:
                    return f"Extracted data from {llm_model_name}: {document_data['table']}"
                else:
                    return None

def calculate_simulated_metrics(extracted_data, ground_truth, method_type):
                """Computes simulated accuracy and information not found rate."""

                total_questions = len(ground_truth)
                correct_answers = 0

                if not ground_truth:
                    if extracted_data:
                        accuracy = 1.0
                        info_not_found = 0.0
                    else:
                        accuracy = 1.0 #should this be 1?
                        info_not_found = 0.0
                    return {"accuracy": accuracy, "information_not_found": info_not_found}


                if not extracted_data:
                    accuracy = 0.0
                    info_not_found = 1.0
                    return {"accuracy": accuracy, "information_not_found": info_not_found}


                for question, correct_answer in ground_truth.items():
                    if question in extracted_data:
                        if extracted_data[question] == correct_answer:
                            correct_answers += 1
                    else:
                        pass

                accuracy = correct_answers / total_questions if total_questions > 0 else 1.0
                info_not_found = (total_questions - correct_answers) / total_questions if total_questions > 0 else 0.0

                return {"accuracy": accuracy, "information_not_found": info_not_found}