from src.llm_engine import (
    generate_answer
)

# =========================================
# PLANNER AGENT
# =========================================

class PlannerAgent:

    def __init__(
        self,
        context_manager
    ):

        self.context_manager = (
            context_manager
        )

    # =====================================
    # GENERATE RESEARCH ROADMAP
    # =====================================

    def generate_research_plan(
        self,
        research_goal
    ):

        active_papers = (
            self.context_manager
            .get_active_papers()
        )

        prompt = f"""
You are an advanced AI Research Planner.

Research Goal:
{research_goal}

Active Papers:
{active_papers}

Generate a complete research roadmap including:

1. Problem Definition
2. Literature Review Strategy
3. Research Methodology
4. Experiment Pipeline
5. Dataset Collection
6. Model Development
7. Evaluation Process
8. Research Timeline
9. Publication Strategy
10. Future Extensions

Provide a detailed structured roadmap.
"""

        response = generate_answer(

            context="Research Planning",

            question=prompt
        )

        return response