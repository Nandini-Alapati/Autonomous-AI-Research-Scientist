from src.llm_engine import (
    generate_answer
)

# =========================================
# METHODOLOGY AGENT
# =========================================

class MethodologyAgent:

    def __init__(
        self,
        context_manager
    ):

        self.context_manager = (
            context_manager
        )

    # =====================================
    # GENERATE METHODOLOGY
    # =====================================

    def generate_methodology(
        self,
        research_problem
    ):

        active_papers = (
            self.context_manager
            .get_active_papers()
        )

        prompt = f"""
You are an expert AI Research Methodology Architect.

Research Problem:
{research_problem}

Active Research Papers:
{active_papers}

Generate a complete research methodology section.

Include:

1. Research Objective
2. System Architecture
3. Dataset Description
4. Data Preprocessing
5. Model Architecture
6. Training Strategy
7. Evaluation Metrics
8. Experimental Setup
9. Validation Strategy
10. Expected Outcomes

Generate in professional IEEE research style.
"""

        response = generate_answer(

            context="Research Methodology Generation",

            question=prompt
        )

        return response