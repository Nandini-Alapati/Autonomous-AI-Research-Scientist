import streamlit as st
import os
from datetime import datetime

from components.paper_card import (
    render_paper_card
)


# =========================================
# GET PDF FILE DETAILS
# =========================================

def get_paper_details(
    paper_path
):

    file_stats = os.stat(
        paper_path
    )

    file_size_mb = round(
        file_stats.st_size / (1024 * 1024),
        2
    )

    upload_time = datetime.fromtimestamp(
        file_stats.st_ctime
    ).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "size_mb": file_size_mb,
        "upload_time": upload_time
    }


# =========================================
# PAPER LIBRARY UI
# =========================================

def render_paper_library(
    upload_dir="data/papers"
):

    st.header(
        "📚 Research Paper Library"
    )

    # =====================================
    # CHECK IF DIRECTORY EXISTS
    # =====================================

    if not os.path.exists(
        upload_dir
    ):

        st.warning(
            "Paper directory does not exist yet."
        )

        return

    # =====================================
    # GET ALL PDF FILES
    # =====================================

    paper_files = [
        file for file in os.listdir(
            upload_dir
        )
        if file.endswith(".pdf")
    ]

    # =====================================
    # NO PAPERS
    # =====================================

    if len(paper_files) == 0:

        st.info(
            "No research papers uploaded yet."
        )

        return

    # =====================================
    # SEARCH BAR
    # =====================================

    search_query = st.text_input(
        "🔍 Search Papers"
    )

    # =====================================
    # FILTER PAPERS
    # =====================================

    if search_query:

        paper_files = [
            paper for paper in paper_files
            if search_query.lower()
            in paper.lower()
        ]

    st.write(
        f"Total Papers: {len(paper_files)}"
    )

    st.divider()

    # =====================================
    # DISPLAY PAPERS
    # =====================================

    for idx, paper in enumerate(
        sorted(paper_files)
    ):

        paper_path = os.path.join(
            upload_dir,
            paper
        )

        details = get_paper_details(
            paper_path
        )

        with st.container(border=True):

            # ==============================
            # PAPER CARD
            # ==============================

            render_paper_card(
                paper_name=paper,
                chunks=0,
                status="Indexed"
            )

            # ==============================
            # PAPER DETAILS
            # ==============================

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"📦 Size: {details['size_mb']} MB"
                )

            with col2:

                st.write(
                    f"🕒 Uploaded: {details['upload_time']}"
                )

            # ==============================
            # PAPER ACTIONS
            # ==============================

            action_col1, action_col2 = st.columns(2)

            # VIEW PAPER
            with action_col1:

                with open(
                    paper_path,
                    "rb"
                ) as pdf_file:

                    st.download_button(
                        label="📥 Download Paper",
                        data=pdf_file,
                        file_name=paper,
                        mime="application/pdf",
                        key=f"download_{idx}"
                    )

            # DELETE PAPER
            with action_col2:

                if st.button(
                    "🗑 Delete Paper",
                    key=f"delete_paper_{idx}"
                ):

                    os.remove(
                        paper_path
                    )

                    st.success(
                        f"{paper} deleted successfully!"
                    )

                    st.rerun()

            st.divider()