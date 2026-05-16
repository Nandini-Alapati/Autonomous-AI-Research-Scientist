import streamlit as st

# =========================================
# RESEARCH TOOLS PANEL
# =========================================

def render_research_tools():

    st.subheader(
        "🛠 Autonomous Research Tools"
    )

    tool = st.selectbox(

        "Select Research Tool",

        [
            "Paper Comparison",
            "Literature Review Generator",
            "Future Work Suggestions",
            "Autonomous Workflow Generator",
            "Methodology Generator",
            "Experiment Planner",
            "Citation Generator",
            "Research Roadmap Planner"
        ]
    )

    return tool