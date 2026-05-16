import streamlit as st

from src.vector_store import (
    get_all_papers
)

# =========================================
# SIDEBAR
# =========================================

def render_sidebar():

    with st.sidebar:

        st.title(
            "🧠 AI Research Scientist"
        )

        st.divider()

        # =================================
        # FILE UPLOAD
        # =================================

        st.subheader(
            "📄 Upload Research Papers"
        )

        uploaded_files = st.file_uploader(

            "Upload PDFs",

            type=["pdf"],

            accept_multiple_files=True
        )

        st.divider()

        # =================================
        # PAPER SELECTION
        # =================================

        st.subheader(
            "📚 Active Research Papers"
        )

        all_papers = get_all_papers()

        if len(all_papers) == 0:

            st.info(
                "No indexed papers yet."
            )

            selected_papers = []

        else:

            selected_papers = st.multiselect(

                "Select Papers",

                options=all_papers,

                default=all_papers
            )

        st.divider()

        # =================================
        # WORKSPACE STATS
        # =================================

        st.subheader(
            "📊 Workspace Stats"
        )

        st.write(
            f"Indexed Papers: {len(all_papers)}"
        )

        st.write(
            f"Active Papers: {len(selected_papers)}"
        )

        # =================================
        # SESSION INFO
        # =================================

        if (
            "chat_history"
            in st.session_state
        ):

            st.write(

                "Messages:",

                len(
                    st.session_state.chat_history
                )
            )

        st.divider()

        # =================================
        # CLEAR CHAT
        # =================================

        if st.button(
            "🗑 Clear Chat History"
        ):

            st.session_state.chat_history = []

            st.session_state.current_sources = []

            st.rerun()

        return (
            uploaded_files,
            selected_papers
        )