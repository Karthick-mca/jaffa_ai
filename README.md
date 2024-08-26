File Upload: The app allows users to upload an Excel file (uploaded_file). The file is read into a DataFrame using pandas.

Data Display and Column Selection: The DataFrame is displayed, and users can select columns for the X-axis and Y-axis from dropdowns (selectbox).

Plot Generation: Once the columns are selected, clicking the "Generate Plot" button creates a plot using matplotlib. The plot is also displayed within the Streamlit app.

Saving and Embedding Plot in Excel: The plot is saved to a buffer and then embedded into a new sheet of the uploaded Excel file. The original data is preserved in its own sheet.

Download the Modified Excel File: Finally, the modified Excel file with the embedded plot is provided as a downloadable link.
