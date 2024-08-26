import openpyxl
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from io import BytesIO

st.title("Excel Plotting Agent")
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Data from Excel:")
    st.write(df)

    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis column", columns)
    y_axis = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        fig, ax = plt.subplots()
        ax.plot(df[x_axis], df[y_axis], marker='o')
        ax.set_title(f'{y_axis} vs {x_axis}')
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)

        st.pyplot(fig)

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        with BytesIO() as output:
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Data', index=False)
                workbook = writer.book
                worksheet = workbook.create_sheet(title='Plot')
                img = openpyxl.drawing.image.Image(buffer)
                worksheet.add_image(img, 'B2')
            output.seek(0)

            st.download_button(
                label="Download Excel with Plot",
                data=output,
                file_name="output_with_plot.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
