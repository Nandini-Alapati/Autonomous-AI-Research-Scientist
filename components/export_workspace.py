import streamlit as st
import json

# =========================================
# EXPORT RESEARCH WORKSPACE
# =========================================

def export_workspace():

    export_data = {

        "chat_history":
        st.session_state.chat_history,

        "selected_papers":
        st.session_state.selected_papers,

        "sources":
        st.session_state.current_sources
    }

    json_data = json.dumps(
        export_data,
        indent=4
    )

    st.download_button(

        label="📥 Export Research Session",

        data=json_data,

        file_name="research_workspace.json",

        mime="application/json"
    )