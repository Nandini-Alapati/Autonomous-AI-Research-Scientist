import streamlit as st


def create_tabs():

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "💬 Chat",
            "📚 Papers",
            "🧠 Memory",
            "📊 Research Tools"
        ]
    )

    return tab1, tab2, tab3, tab4