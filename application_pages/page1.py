
import streamlit as st

def run_page1():
    st.sidebar.subheader("1. Select Document")
    document_type = st.sidebar.selectbox(
        "Document Type",
        ["Benefits Plan", "Compensation Matrix", "Performance Review"],
        help="Choose a synthetic HR document type."
    )

    complexity_options = {
        "Benefits Plan": ["Simple"],
        "Compensation Matrix": ["Hierarchical"],
        "Performance Review": [1] # Assuming Level 1 is the only option based on notebook
    }
    complexity_level = st.sidebar.selectbox(
        "Document Complexity",
        complexity_options[document_type],
        help="Select the complexity level of the document."
    )

    st.session_state.document_type = document_type
    st.session_state.complexity_level = complexity_level

    def load_synthetic_hr_document(document_type, complexity_level):
        """Loads synthetic HR document data."""
        # This dictionary simulates different document content for demonstration
        synthetic_data = {
            ("Benefits Plan", "Simple"): {"document_type": document_type, "complexity_level": complexity_level, "data": ["PlanName: HealthPlus", "Coverage: Individual, Family", "Deductible: $500", "Premium: $100/month"], "table": "PlanName | Coverage | Deductible | Premium\nHealthPlus | Individual, Family | $500 | $100/month"},
            ("Compensation Matrix", "Hierarchical"): {"document_type": document_type, "complexity_level": complexity_level, "data": ["Role: Software Engineer L5", "SalaryRange: $120k-$180k", "BonusTarget: 15%", "EquityGrant: 500 units"], "table": "Role | Salary Range | Bonus Target | Equity Grant\nSoftware Engineer L5 | $120k-$180k | 15% | 500 units"},
            ("Performance Review", 1): {"document_type": document_type, "complexity_level": complexity_level, "data": ["Employee: Jane Doe", "Rating: Exceeds Expectations", "Comments: Strong leadership, met all goals.", "Goals: Lead new project by Q3"], "table": "Employee | Rating | Comments | Goals\nJane Doe | Exceeds Expectations | Strong leadership, met all goals. | Lead new project by Q3"}
        }
        return synthetic_data.get((document_type, complexity_level), None)

    document_data = load_synthetic_hr_document(document_type, complexity_level)
    st.session_state.document_data = document_data

    st.subheader("2. Loaded Synthetic HR Document")
    if document_data:
        st.write("Simulated Document Data:")
        st.json(document_data["data"]) # Displaying a simplified version of data
    else:
        st.warning("No synthetic document data available for the selected type and complexity.")

    def validate_dataset(data):
        """To confirm the structure and integrity of the loaded synthetic dataset."""
        if not data:
            return False # Data is empty, considered invalid for extraction purposes

        # For this synthetic example, we'll assume a basic structure check
        # In a real scenario, this would involve more robust checks on actual tabular data.
        if "data" in data and isinstance(data["data"], list) and len(data["data"]) > 0:
            return True
        return False

    if document_data:
        is_valid = validate_dataset(document_data)
        st.markdown("### Validate Dataset")
        if is_valid:
            st.success(f"Dataset is valid for processing: {is_valid}")
        else:
            st.error(f"Dataset validation failed: {is_valid}. Data might be missing or malformed.")
    else:
        st.info("No document loaded to validate.")

    st.sidebar.subheader("3. Select Extraction Method")
    extraction_method = st.sidebar.selectbox(
        "Simulated Extraction Method",
        ["Traditional OCR", "TalentMine (Claude v3 Haiku)", "AWS Textract", "AWS Textract Visual Q&A"], # Simplified for demo, could expand with all Claude models
        help="Choose an extraction method to simulate its output."
    )
    st.session_state.extraction_method = extraction_method
