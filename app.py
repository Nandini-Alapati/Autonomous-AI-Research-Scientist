import os
import streamlit as st

from src.pdf_processor import (
    extract_text_from_pdf
)

from src.chunking import (
    chunk_text
)

from src.embeddings import (
    create_embeddings
)

from src.vector_store import (
    store_chunks,
    paper_already_exists
)

from src.research_context import (
    ResearchContext
)

from agents.orchestrator import (
    AgentOrchestrator
)

from src.paper_comparator import (
    compare_papers
)

from src.literature_review_generator import (
    generate_literature_review
)

from src.future_work_generator import (
    generate_future_work
)

from src.memory_manager import (
    get_literature_reviews,
    get_research_gaps,
    get_future_work,
    get_notes,
    store_note,
    delete_note
)

from components.sidebar import (
    render_sidebar
)

from components.chat_message import (
    assistant_message,
    user_message
)

from components.paper_card import (
    render_paper_card
)

from components.memory_card import (
    render_memory_card
)

from components.action_buttons import (
    render_action_buttons
)

from components.research_tabs import (
    create_research_tabs
)

from components.research_tools_panel import (
    render_research_tools
)

from components.source_viewer import (
    render_sources
)

from components.paper_workspace import (
    render_paper_workspace
)

from components.paper_library import (
    render_paper_library
)

from components.research_dashboard import (
    render_research_dashboard
)

from components.export_workspace import (
    export_workspace
)

# =========================================
# CONFIG
# =========================================

UPLOAD_DIR = "data/papers"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

st.set_page_config(

    page_title="Autonomous AI Research Scientist",

    layout="wide"
)

st.title(
    "🧠 Autonomous AI Research Scientist"
)

# =========================================
# SESSION STATE
# =========================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []

if "current_sources" not in st.session_state:

    st.session_state.current_sources = []

if "selected_papers" not in st.session_state:

    st.session_state.selected_papers = []

if "research_context" not in st.session_state:

    st.session_state.research_context = (
        ResearchContext()
    )

if "orchestrator" not in st.session_state:

    st.session_state.orchestrator = (
        AgentOrchestrator(
            st.session_state.research_context
        )
    )

# =========================================
# SIDEBAR
# =========================================

uploaded_files, selected_papers = (
    render_sidebar()
)

st.session_state.selected_papers = (
    selected_papers
)

st.session_state.research_context.set_active_papers(
    selected_papers
)

# =========================================
# PROCESS PDFS
# =========================================

if uploaded_files:

    for uploaded_file in uploaded_files:

        if paper_already_exists(
            uploaded_file.name
        ):

            st.warning(
                f"{uploaded_file.name} already exists."
            )

            continue

        st.subheader(
            f"Processing: {uploaded_file.name}"
        )

        pdf_path = os.path.join(
            UPLOAD_DIR,
            uploaded_file.name
        )

        with open(
            pdf_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        st.success(
            f"{uploaded_file.name} uploaded successfully!"
        )

        # =================================
        # EXTRACT TEXT
        # =================================

        pdf_data = extract_text_from_pdf(
            pdf_path
        )

        full_text = pdf_data[
            "full_text"
        ]

        # =================================
        # CHUNKING
        # =================================

        chunks = chunk_text(
            full_text
        )

        # =================================
        # EMBEDDINGS
        # =================================

        embeddings = create_embeddings(
            chunks
        )

        # =================================
        # STORE CHUNKS
        # =================================

        store_chunks(

            chunks=chunks,

            embeddings=embeddings,

            paper_name=uploaded_file.name
        )

        st.success(
            f"{uploaded_file.name} indexed successfully!"
        )

        render_paper_card(

            uploaded_file.name,

            len(chunks),

            "Indexed"
        )

# =========================================
# CREATE TABS
# =========================================

(
    chat_tab,
    papers_tab,
    dashboard_tab,
    memory_tab,
    tools_tab
) = create_research_tabs()

# =========================================
# CHAT TAB
# =========================================

with chat_tab:

    st.header(
        "💬 Autonomous Research Workspace"
    )

    # =====================================
    # ACTIVE PAPERS
    # =====================================

    if (
        len(
            st.session_state.selected_papers
        ) > 0
    ):

        st.success(

            "Active Papers: "
            + ", ".join(
                st.session_state.selected_papers
            )
        )

    else:

        st.warning(
            "No active papers selected."
        )

    st.divider()

    # =====================================
    # AGENT SELECTION
    # =====================================

    agent_mode = st.selectbox(

        "Choose Research Agent",

        [
            "Research Assistant",
            "Reviewer Agent",
            "Experiment Agent",
            "Citation Agent",
            "Planner Agent",
            "Methodology Agent",
            "Autonomous Workflow"
        ]
    )

    st.divider()

    # =====================================
    # CHAT HISTORY
    # =====================================

    for idx, message in enumerate(
        st.session_state.chat_history
    ):

        if message["role"] == "user":

            user_message(
                message["content"]
            )

        else:

            assistant_message(

                message["content"],

                key=f"history_{idx}"
            )

    # =====================================
    # CHAT INPUT
    # =====================================

    question = st.chat_input(
        "Enter your research query..."
    )

    if question:

        st.session_state.chat_history.append({

            "role": "user",

            "content": question
        })

        user_message(question)

        # =================================
        # RESEARCH ASSISTANT
        # =================================

        if agent_mode == "Research Assistant":

            with st.spinner(
                "Research agent analyzing papers..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="research",

                        user_input=question
                    )
                )

            answer = response["answer"]

            sources = response["sources"]

            st.session_state.current_sources = (
                sources
            )

            st.session_state.chat_history.append({

                "role": "assistant",

                "content": answer
            })

            assistant_message(
                answer,
                key="research_answer"
            )

            render_sources(
                sources
            )

        # =================================
        # REVIEWER AGENT
        # =================================

        elif agent_mode == "Reviewer Agent":

            with st.spinner(
                "Reviewer agent analyzing..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(
                        task_type="review"
                    )
                )

            st.session_state.chat_history.append({

                "role": "assistant",

                "content": response
            })

            assistant_message(
                response,
                key="review_answer"
            )

        # =================================
        # EXPERIMENT AGENT
        # =================================

        elif agent_mode == "Experiment Agent":

            with st.spinner(
                "Designing experiment pipeline..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="experiment",

                        user_input=question
                    )
                )

            st.session_state.chat_history.append({

                "role": "assistant",

                "content": response
            })

            assistant_message(
                response,
                key="experiment_answer"
            )

        # =================================
        # CITATION AGENT
        # =================================

        elif agent_mode == "Citation Agent":

            with st.spinner(
                "Generating citations..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="citation",

                        user_input=question
                    )
                )

            st.session_state.chat_history.append({

                "role": "assistant",

                "content": response
            })

            assistant_message(
                response,
                key="citation_answer"
            )

        # =================================
        # PLANNER AGENT
        # =================================

        elif agent_mode == "Planner Agent":

            with st.spinner(
                "Generating research roadmap..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="planning",

                        user_input=question
                    )
                )

            st.session_state.chat_history.append({

                "role": "assistant",

                "content": response
            })

            assistant_message(
                response,
                key="planner_answer"
            )

        # =================================
        # METHODOLOGY AGENT
        # =================================

        elif agent_mode == "Methodology Agent":

            with st.spinner(
                "Generating methodology..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="methodology",

                        user_input=question
                    )
                )

            st.session_state.chat_history.append({

                "role": "assistant",

                "content": response
            })

            assistant_message(
                response,
                key="methodology_answer"
            )

        # =================================
        # AUTONOMOUS WORKFLOW
        # =================================

        elif agent_mode == "Autonomous Workflow":

            with st.spinner(
                "Running autonomous research workflow..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="autonomous",

                        user_input=question
                    )
                )

            st.session_state.chat_history.append({

                "role": "assistant",

                "content": response
            })

            assistant_message(
                response,
                key="autonomous_answer"
            )

# =========================================
# PAPERS TAB
# =========================================

with papers_tab:

    st.header(
        "📚 Research Paper Workspace"
    )

    workspace_tab, library_tab = (
        st.tabs([
            "Workspace",
            "Paper Library"
        ])
    )

    with workspace_tab:

        render_paper_workspace()

    with library_tab:

        render_paper_library()

# =========================================
# DASHBOARD TAB
# =========================================

with dashboard_tab:

    render_research_dashboard()

    st.divider()

    export_workspace()

# =========================================
# MEMORY TAB
# =========================================

with memory_tab:

    st.header(
        "🧠 Research Memory"
    )

    memory_option = st.selectbox(

        "Select Memory Category",

        [
            "Literature Reviews",
            "Research Gaps",
            "Future Work",
            "Notes"
        ]
    )

    # =====================================
    # LITERATURE REVIEWS
    # =====================================

    if (
        memory_option
        == "Literature Reviews"
    ):

        reviews = (
            get_literature_reviews()
        )

        if len(reviews) == 0:

            st.info(
                "No literature reviews stored."
            )

        else:

            for idx, review in enumerate(
                reviews,
                start=1
            ):

                assistant_message(

                    review,

                    f"review_{idx}"
                )

    # =====================================
    # RESEARCH GAPS
    # =====================================

    elif (
        memory_option
        == "Research Gaps"
    ):

        gaps = get_research_gaps()

        if len(gaps) == 0:

            st.info(
                "No research gaps stored."
            )

        else:

            for idx, gap in enumerate(
                gaps,
                start=1
            ):

                assistant_message(

                    gap,

                    f"gap_{idx}"
                )

    # =====================================
    # FUTURE WORK
    # =====================================

    elif (
        memory_option
        == "Future Work"
    ):

        future_items = (
            get_future_work()
        )

        if len(future_items) == 0:

            st.info(
                "No future work stored."
            )

        else:

            for idx, item in enumerate(
                future_items,
                start=1
            ):

                assistant_message(

                    item,

                    f"future_{idx}"
                )

    # =====================================
    # NOTES
    # =====================================

    elif memory_option == "Notes":

        st.subheader(
            "Research Notes"
        )

        new_note = st.text_area(
            "Write a note"
        )

        if st.button(
            "Save Note"
        ):

            if new_note.strip() != "":

                store_note(
                    new_note
                )

                st.success(
                    "Note saved!"
                )

                st.rerun()

        st.divider()

        notes = get_notes()

        if len(notes) == 0:

            st.info(
                "No notes available."
            )

        else:

            for idx, note in enumerate(
                notes
            ):

                delete_clicked = (
                    render_memory_card(

                        f"Note {idx + 1}",

                        note,

                        key=idx
                    )
                )

                render_action_buttons(

                    note,

                    f"note_{idx}"
                )

                if delete_clicked:

                    delete_note(idx)

                    st.success(
                        "Note deleted."
                    )

                    st.rerun()

# =========================================
# TOOLS TAB
# =========================================

with tools_tab:

    st.header(
        "🛠 Advanced Research Tools"
    )

    selected_tool = (
        render_research_tools()
    )

    # =====================================
    # PAPER COMPARISON
    # =====================================

    if (
        selected_tool
        == "Paper Comparison"
    ):

        comparison_topic = st.text_input(
            "Enter comparison topic"
        )

        if comparison_topic:

            with st.spinner(
                "Comparing papers..."
            ):

                comparison_result = (
                    compare_papers(
                        comparison_topic
                    )
                )

            assistant_message(

                comparison_result,

                "comparison_result"
            )

    # =====================================
    # LITERATURE REVIEW
    # =====================================

    elif (
        selected_tool
        == "Literature Review Generator"
    ):

        if st.button(
            "Generate Literature Review"
        ):

            with st.spinner(
                "Generating literature review..."
            ):

                literature_review = (
                    generate_literature_review()
                )

            assistant_message(

                literature_review,

                "literature_review"
            )

    # =====================================
    # FUTURE WORK
    # =====================================

    elif (
        selected_tool
        == "Future Work Suggestions"
    ):

        if st.button(
            "Generate Future Work"
        ):

            with st.spinner(
                "Generating future work..."
            ):

                future_work = (
                    generate_future_work()
                )

            assistant_message(

                future_work,

                "future_work"
            )

    # =====================================
    # AUTONOMOUS WORKFLOW
    # =====================================

    elif (
        selected_tool
        == "Autonomous Workflow Generator"
    ):

        workflow_goal = st.text_input(
            "Enter research goal"
        )

        if workflow_goal:

            with st.spinner(
                "Running autonomous workflow..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="autonomous",

                        user_input=workflow_goal
                    )
                )

            assistant_message(
                response,
                key="workflow_output"
            )

    # =====================================
    # METHODOLOGY GENERATOR
    # =====================================

    elif (
        selected_tool
        == "Methodology Generator"
    ):

        methodology_topic = st.text_input(
            "Enter research problem"
        )

        if methodology_topic:

            with st.spinner(
                "Generating methodology..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="methodology",

                        user_input=methodology_topic
                    )
                )

            assistant_message(
                response,
                key="methodology_output"
            )

    # =====================================
    # EXPERIMENT PLANNER
    # =====================================

    elif (
        selected_tool
        == "Experiment Planner"
    ):

        experiment_topic = st.text_input(
            "Enter experiment topic"
        )

        if experiment_topic:

            with st.spinner(
                "Planning experiments..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="experiment",

                        user_input=experiment_topic
                    )
                )

            assistant_message(
                response,
                key="experiment_output"
            )

    # =====================================
    # CITATION GENERATOR
    # =====================================

    elif (
        selected_tool
        == "Citation Generator"
    ):

        citation_topic = st.text_input(
            "Enter citation topic"
        )

        if citation_topic:

            with st.spinner(
                "Generating citations..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="citation",

                        user_input=citation_topic
                    )
                )

            assistant_message(
                response,
                key="citation_output"
            )

    # =====================================
    # ROADMAP PLANNER
    # =====================================

    elif (
        selected_tool
        == "Research Roadmap Planner"
    ):

        roadmap_topic = st.text_input(
            "Enter research goal"
        )

        if roadmap_topic:

            with st.spinner(
                "Generating roadmap..."
            ):

                response = (
                    st.session_state.orchestrator
                    .handle_task(

                        task_type="planning",

                        user_input=roadmap_topic
                    )
                )

            assistant_message(
                response,
                key="roadmap_output"
            )