from src.rag_pipeline import (
    ask_question
)

# =========================================
# RESEARCHER AGENT
# =========================================

class ResearcherAgent:

    def __init__(
        self,
        context_manager
    ):

        self.context_manager = (
            context_manager
        )

    # =====================================
    # ANSWER RESEARCH QUESTION
    # =====================================

    def research_query(
        self,
        question
    ):

        active_papers = (
            self.context_manager
            .get_active_papers()
        )

        response = ask_question(

            question=question,

            selected_papers=active_papers
        )

        answer = response["answer"]

        sources = response["sources"]

        # Store sources
        self.context_manager.set_sources(
            sources
        )

        # Store conversation
        self.context_manager.add_chat_message(
            "user",
            question
        )

        self.context_manager.add_chat_message(
            "assistant",
            answer
        )

        return response