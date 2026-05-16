import streamlit as st

from components.action_buttons import (
    render_action_buttons
)

# =========================================
# USER MESSAGE
# =========================================

def user_message(
    content
):

    with st.chat_message(
        "user"
    ):

        st.markdown(content)

# =========================================
# ASSISTANT MESSAGE
# =========================================

def assistant_message(
    content,
    key="message"
):

    with st.chat_message(
        "assistant"
    ):

        with st.container(
            border=True
        ):

            st.markdown(content)

            st.divider()

            render_action_buttons(
                content,
                key
            )