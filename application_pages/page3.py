
import streamlit as st
import pandas as pd
import plotly.express as px

def run_page3():
    if 'document_data' not in st.session_state:
        st.warning("Please select a document on the 'Document & Method Selection' page.")
        return

    document_data = st.session_state.document_data
    document_type = st.session_state.get('document_type', "Benefits Plan")
    extraction_method = st.session_state.get('extraction_method', "TalentMine (Claude v3 Haiku)")


    def calculate_simulated_metrics(extracted_data_key, ground_truth_data, method_type):
        """Computes simulated accuracy and information not found rate based on predefined tables."""
        # Ground truth for Benefits Plan (from Tables 2 & 5 concepts, simplified)
        if ground_truth_data == "Benefits Plan Data":
            if method_type == "TalentMine (Claude v3 Haiku)":
                return {"accuracy": 0.90, "information_not_found": 0.00} # Based on Table 1 & 5
            elif method_type == "AWS Textract":
                return {"accuracy": 0.00, "information_not_found": 1.00} # Based on Table 2
            elif method_type == "AWS Textract Visual Q&A":
                return {"accuracy": 0.40, "information_not_found": 0.60} # Based on Table 2
            elif method_type == "Traditional OCR":
                return {"accuracy": 0.00, "information_not_found": 1.00}
            # Add other Claude models from Table 1 and 5
            elif method_type == "Claude Instant": return {"accuracy": 0.70, "information_not_found": 0.00}
            elif method_type == "Claude v2": return {"accuracy": 0.60, "information_not_found": 0.30}
            elif method_type == "Claude v2.1": return {"accuracy": 0.70, "information_not_found": 0.20}
            elif method_type == "Claude v3 Sonnet": return {"accuracy": 1.00, "information_not_found": 0.00}
            elif method_type == "Claude v3 Opus": return {"accuracy": 0.90, "information_not_found": 0.00}
            elif method_type == "Claude v3.5 Haiku": return {"accuracy": 0.80, "information_not_found": 0.00}
            elif method_type == "Claude v3.5 Sonnet v1/v2": return {"accuracy": 1.00, "information_not_found": 0.00}
            elif method_type == "Claude v3.7 Sonnet": return {"accuracy": 1.00, "information_not_found": 0.00}
            elif method_type == "Claude v4 Sonnet": return {"accuracy": 1.00, "information_not_found": 0.00}
            elif method_type == "Claude v4 Opus": return {"accuracy": 1.00, "information_not_found": 0.00}
        
        # Placeholder for other document types if needed, or default to generic
        return {"accuracy": 0.0, "information_not_found": 0.0} # Default for unknown cases

    st.subheader("4. Simulated Performance Metrics")

    if document_data:
        st.markdown("### Calculate Simulated Metrics")
        st.markdown(r"Accuracy is defined as $\frac{\text{number of correct answers}}{\text{total number of questions}}$, and Information Not Found rate is defined as $\frac{\text{number of missing answers}}{\text{total number of questions}}$.")
        
        # Simulate a ground truth for the selected document type
        ground_truth_for_metrics = None
        if document_type == "Benefits Plan":
            ground_truth_for_metrics = "Benefits Plan Data" # A simplified key to look up metrics

        if ground_truth_for_metrics:
            # Compile data for visualization from the paper's tables
            performance_data = {
                "Method": [],
                "Accuracy": [],
                "Information Not Found": []
            }
            
            methods_to_compare = [
                "Traditional OCR",
                "AWS Textract",
                "AWS Textract Visual Q&A",
                "TalentMine (Claude v3 Haiku)",
                "Claude Instant", "Claude v2", "Claude v2.1", "Claude v3 Sonnet", 
                "Claude v3 Opus", "Claude v3.5 Haiku", "Claude v3.5 Sonnet v1/v2",
                "Claude v3.7 Sonnet", "Claude v4 Sonnet", "Claude v4 Opus"
            ]

            for method in methods_to_compare:
                metrics = calculate_simulated_metrics(document_data.get("table", ""), ground_truth_for_metrics, method)
                performance_data["Method"].append(method)
                performance_data["Accuracy"].append(metrics["accuracy"])
                performance_data["Information Not Found"].append(metrics["information_not_found"])

            df_metrics = pd.DataFrame(performance_data)
            
            st.dataframe(df_metrics.set_index("Method"))

            # Plotting the metrics
            fig_accuracy = px.bar(
                df_metrics,
                x="Method",
                y="Accuracy",
                title="Simulated Accuracy by Extraction Method",
                color_discrete_sequence=px.colors.qualitative.Pastel,
                text_auto=True
            )
            fig_accuracy.update_layout(xaxis_title="Extraction Method", yaxis_title="Accuracy", font=dict(size=12))
            st.plotly_chart(fig_accuracy, use_container_width=True)

            fig_info_not_found = px.bar(
                df_metrics,
                x="Method",
                y="Information Not Found",
                title="Simulated Information Not Found Rate by Extraction Method",
                color_discrete_sequence=px.colors.qualitative.Pastel,
                text_auto=True
            )
            fig_info_not_found.update_layout(xaxis_title="Extraction Method", yaxis_title="Information Not Found Rate", font=dict(size=12))
            st.plotly_chart(fig_info_not_found, use_container_width=True)

        else:
            st.info("Metrics calculation is currently supported for 'Benefits Plan' document type only.")
    else:
        st.info("Please select a document to see simulated metrics.")

    st.markdown("## Conclusion")
    st.markdown("This notebook demonstrates the core functionality of the TalentMine system's 'Offline Preprocessing' by simulating how LLMs extract and semantically enrich tabular data from HR documents. By comparing the outputs of traditional OCR methods and LLM-enhanced extraction, users can gain an intuitive understanding of the benefits of LLM-based document processing for HR operations. The simulated metrics provide a quantitative measure of the improvements gained by using LLMs, demonstrating the ROI of investing in these technologies.")
    st.markdown("---")
    st.markdown("## QuantUniversity License")
    st.markdown("© QuantUniversity 2025")
    st.markdown("This notebook was created for **educational purposes only** and is **not intended for commercial use**.")
    st.markdown("- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.")
    st.markdown("- You **may not delete or modify this license cell** without authorization.")
    st.markdown("- This notebook was generated using **QuCreate**, an AI-powered assistant.")
    st.markdown("- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.")
    st.markdown("All rights reserved. For permissions or commercial licensing, contact: [info@quantuniversity.com](mailto:info@quantuniversity.com)")
