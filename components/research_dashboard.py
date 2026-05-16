import streamlit as st

# =========================================
# RESEARCH DASHBOARD
# =========================================

def render_research_dashboard():

    st.subheader(
        "📊 Research Workspace Dashboard"
    )

    # =====================================
    # SESSION METRICS
    # =====================================

    total_messages = len(
        st.session_state.chat_history
    )

    total_papers = len(
        st.session_state.selected_papers
    )

    total_sources = len(
        st.session_state.current_sources
    )

    # =====================================
    # METRIC CARDS
    # =====================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Research Messages",
            total_messages
        )

    with col2:

        st.metric(
            "Active Papers",
            total_papers
        )

    with col3:

        st.metric(
            "Retrieved Sources",
            total_sources
        )

    st.divider()

    # =====================================
    # ACTIVE PAPERS
    # =====================================

    st.markdown(
        "### 📚 Active Research Papers"
    )

    if total_papers == 0:

        st.info(
            "No papers selected."
        )

    else:

        for paper in (
            st.session_state.selected_papers
        ):

            st.success(f"📄 {paper}")

    st.divider()

    # =====================================
    # RECENT SOURCES
    # =====================================

    st.markdown(
        "### 🔍 Latest Retrieved Sources"
    )

    if total_sources == 0:

        st.info(
            "No retrieved sources yet."
        )

    else:

        for source in (
            st.session_state.current_sources[:3]
        ):

            st.write(
                f"📄 {source['paper_name']} "
                f"(Chunk {source['chunk_id']})"
            )