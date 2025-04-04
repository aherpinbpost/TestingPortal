import streamlit as st

# Page configuration
st.set_page_config(page_title="Excel Data Validation and Transfer", layout="wide")

def main():
    st.title("Excel file validation and transfer")
    st.write(
        "This application allows you to upload a multi-sheet Excel file, validate the data, and transfer it to a database."
    )

    st.subheader("Upload your template")
    template_type = st.selectbox("Select a template type", ["Social", "Environment"])
    uploaded_file = st.file_uploader("Upload your Excel file here", type=["xlsx", "xls"])

if __name__ == "__main__":
    main()
