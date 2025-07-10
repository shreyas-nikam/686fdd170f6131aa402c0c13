id: 686fdd170f6131aa402c0c13_user_guide
summary: TalentMine User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# TalentMine: HR Document Table Extraction with LLMs

## Introduction to HR Document Processing with LLMs
Duration: 05:00

Welcome to this codelab on HR Document Table Extraction using Large Language Models (LLMs)! This application, called TalentMine, provides a simplified demonstration of how LLMs can be used to extract and understand tabular data from complex documents like those found in Human Resources.

<aside class="positive">
<b>Why is this important?</b> HR documents often contain critical information in tables (like benefits matrices or compensation data) that is difficult for traditional automated systems to accurately extract. Errors here can lead to costly mistakes, compliance issues, and inefficient processes.
</aside>

Traditional methods, primarily relying on Optical Character Recognition (OCR), often struggle with the varying layouts and intricate structures of these tables. They might extract text, but lose the crucial *context* and *relationships* within the table – for example, understanding that a specific number is the deductible for a particular health plan under individual coverage. This loss of **semantic information** is a major challenge.

This codelab explores how LLMs can overcome this by not just extracting text but also *understanding* its meaning and structure within the table. The application simulates key aspects of the TalentMine system's approach [1], demonstrating:
- The kind of raw output you might get from traditional OCR.
- The enriched, contextual output achievable with LLMs.
- Simulated performance comparisons highlighting the benefits of the LLM approach.

By working through this lab, you will gain an intuitive understanding of:
- The challenges of extracting structured data from complex documents.
- How LLMs can add semantic understanding to this process.
- The potential impact of LLM-based solutions on HR operations efficiency and accuracy.

This lab is designed for anyone interested in Document AI, LLMs, and their practical applications, particularly in fields like HR.

<aside class="positive">
Use the navigation options in the sidebar on the left (`Document & Method Selection`, `Extraction Output`, `Performance Metrics`) to move between the different sections of the application as guided by the steps in this codelab.
</aside>

## Selecting a Document and Extraction Method
Duration: 03:00

The first step in using the TalentMine simulator is to choose a synthetic HR document to process and select the method you want to simulate for extraction.

1.  Navigate to the **"Document & Method Selection"** page using the sidebar.

2.  Look at the sidebar under the "1. Select Document" heading.
    - **Document Type:** Use the dropdown to select a type of synthetic HR document. You can choose from options like "Benefits Plan", "Compensation Matrix", or "Performance Review". These represent common document types with tables found in HR.
    - **Document Complexity:** This dropdown allows you to select a complexity level for the chosen document type. The available options might change based on the document type selected, reflecting different table structures (e.g., "Simple" vs. "Hierarchical").

<aside class="positive">
These documents are synthetic, meaning they are simulated examples designed to demonstrate the concepts without using real sensitive data.
</aside>

3.  Once you've selected the document type and complexity, the main area of the page updates to show **"Loaded Synthetic HR Document"**.
    - This section displays the simulated data content of the document you selected. It provides an idea of the text and structure the extraction process will work with.
    - Below this, the **"Validate Dataset"** section performs a basic check to confirm the simulated document data is loaded and structured in a way the simulator can process. You should see a success message here if the document loaded correctly.

4.  Now, look at the sidebar under the "3. Select Extraction Method" heading.
    - **Simulated Extraction Method:** Use this dropdown to choose which method's performance you want to simulate and compare. Options include "Traditional OCR" and several LLM-based methods like "TalentMine (Claude v3 Haiku)", "AWS Textract", and "AWS Textract Visual Q&A". Each option simulates the typical outcome of using that method on HR documents.

Make your selections for Document Type, Complexity, and Simulated Extraction Method. These choices will determine what you see on the next pages.

## Examining Extraction Output
Duration: 04:00

Once you've selected a document and an extraction method, you can move to the next page to see the simulated results of the extraction process. This is where you'll see the difference between traditional and LLM-enhanced approaches.

1.  Navigate to the **"Extraction Output"** page using the sidebar.

2.  This page is titled **"Simulated Extraction Output"**. It displays the result of applying the selected extraction method to the document chosen on the previous page.

3.  Depending on the "Simulated Extraction Method" you chose:
    - If you selected **"Traditional OCR"**, you will see a section titled **"Raw OCR Output"**. This block of text simulates the kind of output you might get from a standard OCR system. Notice how the structure of the original document (especially tables) might be lost, and text might be jumbled or lack clear relationships between pieces of information. This illustrates the problem of *semantic information loss*.
    - If you selected any of the LLM-based methods (like "TalentMine (Claude v3 Haiku)", "AWS Textract", etc.), you will see a section titled **"{Method Name} Enhanced Semantic Output"**. This output simulates how an LLM process attempts to preserve the structure and relationships within the data. It aims to present the information in a more structured, semantically meaningful way, often resembling a table format.

4.  Scroll down to the **"Comparison with Traditional OCR"** section. This section is particularly helpful for understanding the value of the LLM approach. It presents the simulated "Raw OCR Output" side-by-side with the selected "Enhanced Output".

<aside class="positive">
Compare the two outputs. How much easier is it to understand the table data in the "Enhanced Output"? Does it clearly show which piece of information belongs to which column or row? This visual comparison highlights how LLMs can preserve crucial contextual dependencies and row-column relationships that OCR often misses.
</aside>

This page demonstrates *how* the different methods process the document, showing the qualitative difference in the output's structure and semantic richness.

## Analyzing Performance Metrics
Duration: 06:00

Beyond the qualitative difference in output, it's valuable to understand the quantitative performance of different extraction methods. The final page provides simulated metrics based on research findings [1] to compare accuracy and information loss.

1.  Navigate to the **"Performance Metrics"** page using the sidebar.

2.  This page is titled **"Simulated Performance Metrics"**. It presents data comparing the effectiveness of various extraction methods.

3.  Look at the **"Calculate Simulated Metrics"** section.
    - The page defines the key metrics used for comparison:
        - **Accuracy**: Defined as the ratio of correct answers to the total number of questions that could be asked about the document's data. $$ \text{Accuracy} = \frac{\text{number of correct answers}}{\text{total number of questions}} $$
        - **Information Not Found**: Defined as the ratio of missing answers (data that couldn't be extracted) to the total number of questions. $$ \text{Information Not Found} = \frac{\text{number of missing answers}}{\text{total number of questions}} $$

<aside class="positive">
These metrics are simulated based on the performance data presented in the referenced paper [1], particularly Tables 1, 2, and 5. They represent typical performance observed on HR documents like the Benefits Plan example.
</aside>

4.  Below the definitions, you will see a table showing the simulated "Accuracy" and "Information Not Found" rates for a range of methods, including "Traditional OCR", "AWS Textract", and various simulated Claude and TalentMine (Claude v3 Haiku) configurations.

5.  The data from the table is also visualized in two bar charts:
    - **Simulated Accuracy by Extraction Method**: Compare the heights of the bars. Which methods achieve higher accuracy? Notice how the LLM-based methods, especially TalentMine (Claude v3 Haiku) and certain Claude versions, often show significantly higher simulated accuracy than traditional methods for this type of task.
    - **Simulated Information Not Found Rate by Extraction Method**: Compare the heights here. Lower is better. LLM-based methods typically result in less information being lost during extraction compared to Traditional OCR or some non-LLM approaches.

<aside class="negative">
Currently, the detailed performance metrics are primarily displayed for the "Benefits Plan" document type simulation. Selecting other document types on the first page might not change the metric values shown on this page, as the metrics are hardcoded based on the paper's findings for specific document types.
</aside>

By examining these metrics and charts, you can see the quantitative advantage that LLM-based approaches offer in accurately extracting structured data from complex HR documents and reducing data loss. This underscores the **business value** highlighted in the introduction.

## Conclusion and Licensing

This codelab demonstrated the core concepts behind TalentMine's LLM-based approach to extracting and semantically enriching tabular data from HR documents. You've seen the limitations of traditional methods and how LLMs can provide more accurate and contextually rich results, leading to improved performance metrics.

The application simulates this process by allowing you to choose synthetic documents and extraction methods, view the simulated outputs side-by-side, and analyze quantitative performance metrics.

This intuitive comparison helps illustrate why LLMs are a powerful tool for handling complex document processing tasks and the potential return on investment they offer for applications in areas like HR.



## QuantUniversity License

© QuantUniversity 2025

This notebook was created for **educational purposes only** and is **not intended for commercial use**.

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.
- You **may not delete or modify this license cell** without authorization.
- This notebook was generated using **QuCreate**, an AI-powered assistant.
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.

All rights reserved. For permissions or commercial licensing, contact: [info@quantuniversity.com](mailto:info@quantuniversity.com)
