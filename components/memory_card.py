import streamlit as st


def render_memory_card(
    title,
    content,
    key="memory"
):

    with st.container(border=True):

        st.subheader(
            f"🧠 {title}"
        )

        st.write(content)

        if st.button(
            "🗑 Delete",
            key=f"delete_{key}"
        ):

            return True

    return False