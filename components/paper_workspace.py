import streamlit as st
import os

# =========================================
# PAPER WORKSPACE
# =========================================

def render_paper_workspace():

    st.subheader(
        "📚 Active Research Workspace"
    )

    paper_dir = "data/papers"

    # =====================================
    # CHECK DIRECTORY
    # =====================================

    if not os.path.exists(
        paper_dir
    ):

        st.info(
            "No papers uploaded yet."
        )

        return

    papers = [

        paper for paper in os.listdir(
            paper_dir
        )

        if paper.endswith(".pdf")
    ]

    # =====================================
    # EMPTY WORKSPACE
    # =====================================

    if len(papers) == 0:

        st.info(
            "No research papers available."
        )

        return

    # =====================================
    # WORKSPACE OVERVIEW
    # =====================================

    st.markdown(
        f"### Indexed Papers: {len(papers)}"
    )

    st.divider()

    # =====================================
    # DISPLAY PAPERS
    # =====================================

    for idx, paper in enumerate(
        sorted(papers)
    ):

        with st.container(
            border=True
        ):

            col1, col2 = st.columns(
                [6, 2]
            )

            with col1:

                st.markdown(
                    f"📄 {paper}"
                )

            with col2:

                if (
                    "selected_papers"
                    not in st.session_state
                ):

                    st.session_state[
                        "selected_papers"
                    ] = []

                already_selected = (
                    paper in
                    st.session_state[
                        "selected_papers"
                    ]
                )

                button_label = (
                    "✅ Active"
                    if already_selected
                    else "➕ Select"
                )

                if st.button(
                    button_label,
                    key=f"paper_{idx}"
                ):

                    if not already_selected:

                        st.session_state[
                            "selected_papers"
                        ].append(paper)

                    st.rerun()