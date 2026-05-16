import streamlit as st

# =========================================
# SOURCE VIEWER
# =========================================

def render_sources(
    sources
):

    with st.expander(
        "📚 Retrieved Research Sources",
        expanded=True
    ):

        # =================================
        # NO SOURCES
        # =================================

        if (
            not sources
            or len(sources) == 0
        ):

            st.info(
                "No sources retrieved."
            )

            return

        # =================================
        # DISPLAY SOURCES
        # =================================

        for idx, source in enumerate(
            sources,
            start=1
        ):

            paper_name = source.get(
                "paper_name",
                "Unknown Paper"
            )

            chunk_id = source.get(
                "chunk_id",
                "N/A"
            )

            content = source.get(
                "content",
                ""
            )

            with st.container(
                border=True
            ):

                st.markdown(
                    f"### 📄 Source {idx}"
                )

                st.write(
                    f"**Paper:** {paper_name}"
                )

                st.write(
                    f"**Chunk ID:** {chunk_id}"
                )

                st.markdown(
                    "#### Extracted Content"
                )

                st.write(content)

                st.divider()