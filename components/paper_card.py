import streamlit as st


def render_paper_card(
    paper_name,
    chunks=0,
    status="Indexed"
):

    with st.container(border=True):

        st.subheader(
            f"📄 {paper_name}"
        )

        st.write(
            f"📚 Chunks: {chunks}"
        )

        if status == "Indexed":

            st.success(status)

        else:

            st.warning(status)