import streamlit as st

from src.export_manager import (
    export_to_txt,
    export_to_docx,
    export_to_pdf
)


def render_export_menu(
    content,
    file_name="research_output"
):

    with st.popover("📤 Export"):

        txt_data = export_to_txt(content)

        st.download_button(
            label="📄 TXT",
            data=txt_data,
            file_name=f"{file_name}.txt",
            mime="text/plain",
            use_container_width=True
        )

        docx_data = export_to_docx(content)

        st.download_button(
            label="📝 DOCX",
            data=docx_data,
            file_name=f"{file_name}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True
        )

        pdf_data = export_to_pdf(content)

        st.download_button(
            label="📕 PDF",
            data=pdf_data,
            file_name=f"{file_name}.pdf",
            mime="application/pdf",
            use_container_width=True
        )