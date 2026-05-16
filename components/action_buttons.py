import streamlit as st
import pyperclip

from components.export_menu import (
    render_export_menu
)


def render_action_buttons(
    content,
    key="default"
):

    col1, col2 = st.columns(2)

    with col1:

        render_export_menu(
            content,
            f"output_{key}"
        )

    with col2:

        if st.button(
            "📋 Copy",
            key=f"copy_{key}"
        ):

            pyperclip.copy(content)

            st.toast(
                "Copied to clipboard!"
            )