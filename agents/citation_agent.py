from src.llm_engine import (
    generate_answer
)

# =========================================
# CITATION AGENT
# =========================================

class CitationAgent:

    def __init__(
        self,
        context_manager
    ):

        self.context_manager = (
            context_manager
        )

    # =====================================
    # GENERATE CITATIONS
    # =====================================

    def generate_citations(
        self,
        research_topic
    ):

        active_papers = (
            self.context_manager
            .get_active_papers()
        )

        prompt = f"""
You are an expert academic citation assistant.

Research Topic:
{research_topic}

Active Papers:
{active_papers}

Generate:

1. IEEE style citations
2. APA style citations
3. BibTeX references
4. Suggested related references
5. Citation recommendations

Provide professional academic formatting.
"""

        response = generate_answer(

            context="Academic Citation Generation",

            question=prompt
        )

        return response