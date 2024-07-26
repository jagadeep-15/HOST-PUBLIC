

import streamlit as st
import io
from PyPDF2 import PdfReader

def main():
    st.title("Invoice Upload and Separation")

    uploaded_file = st.file_uploader("Choose an invoice file", type=["pdf"])

    if uploaded_file is not None:
        try:
            # Display uploaded file details
            file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
            st.write(file_details)

            # Read the PDF file
            reader = PdfReader(uploaded_file)
            number_of_pages = len(reader.pages)
            st.write(f"Number of pages: {number_of_pages}")

            # Extract text from each page
            for page_num in range(number_of_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                st.write(f"Page {page_num + 1}")
                st.text(text)

                # Example: splitting invoice content
                lines = text.split("\n")
                invoice_details = [line for line in lines if "Invoice" in line]
                st.write(f"Invoice details from Page {page_num + 1}:")
                st.write(invoice_details)

        except Exception as e:
            st.error(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
