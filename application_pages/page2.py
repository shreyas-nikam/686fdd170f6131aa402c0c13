
import streamlit as st

def run_page2():
    if 'document_data' not in st.session_state or 'extraction_method' not in st.session_state:
        st.warning("Please select a document and extraction method on the 'Document & Method Selection' page.")
        return

    document_data = st.session_state.document_data
    extraction_method = st.session_state.extraction_method

    def simulate_traditional_ocr_extraction(document_data):
        """Simulates traditional OCR extraction with potential errors."""
        if not document_data or "data" not in document_data:
            return ""
        
        text = ""
        # Simulate errors/poor structuring for OCR
        for item in document_data["data"]:
            text += item.replace(":", " ").replace("-", " ") + " " # Simulate losing structure
        return text.strip() + " (Simulated OCR errors may occur)"

    def simulate_llm_enhanced_extraction(document_data, llm_model_name):
        """Simulates LLM-based extraction, enriching data semantically."""
        if not document_data or not llm_model_name or "table" not in document_data:
            return "LLM extraction not applicable or data missing."

        # This is a highly simplified simulation. A real LLM would process the content.
        if "table" in document_data:
            return f"**LLM Model: {llm_model_name}**\n\nExtracted Semantically Enriched Table Data:\n\n```\n{document_data['table']}\n```\n(Simulated preservation of row-column relationships and contextual dependencies)"
        else:
            return "No tabular data found for LLM extraction."

    st.subheader("3. Simulated Extraction Output")
    if document_data:
        if extraction_method == "Traditional OCR":
            ocr_text = simulate_traditional_ocr_extraction(document_data)
            st.markdown("#### Raw OCR Output")
            st.code(ocr_text)
        else:
            # Simulate LLM extraction for TalentMine and other LLM-based methods
            llm_text = simulate_llm_enhanced_extraction(document_data, extraction_method)
            st.markdown(f"#### {extraction_method} Enhanced Semantic Output")
            st.markdown(llm_text)
            
        # Always show a comparison if possible
        if extraction_method != "Traditional OCR":
            st.markdown("#### Comparison with Traditional OCR")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("##### Raw OCR Output")
                st.code(simulate_traditional_ocr_extraction(document_data))
            with col2:
                st.markdown(f"##### {extraction_method} Enhanced Output")
                st.markdown(simulate_llm_enhanced_extraction(document_data, extraction_method))

    else:
        st.info("Please select a document to see extraction output.")
