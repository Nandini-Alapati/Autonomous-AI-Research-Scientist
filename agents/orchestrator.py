from agents.researcher_agent import (
    ResearcherAgent
)

from agents.reviewer_agent import (
    ReviewerAgent
)

from agents.experiment_agent import (
    ExperimentAgent
)

# =========================================
# AGENT ORCHESTRATOR
# =========================================

class AgentOrchestrator:

    def __init__(
        self,
        context_manager
    ):

        self.context_manager = (
            context_manager
        )

        self.researcher_agent = (
            ResearcherAgent(
                context_manager
            )
        )

        self.reviewer_agent = (
            ReviewerAgent(
                context_manager
            )
        )

        self.experiment_agent = (
            ExperimentAgent(
                context_manager
            )
        )

    # =====================================
    # TASK HANDLER
    # =====================================

    def handle_task(
        self,
        task_type,
        user_input=None
    ):

        # =================================
        # RESEARCH
        # =================================

        if task_type == "research":

            return (
                self.researcher_agent
                .research_query(
                    user_input
                )
            )

        # =================================
        # REVIEW
        # =================================

        elif task_type == "review":

            return (
                self.reviewer_agent
                .review_research()
            )

        # =================================
        # EXPERIMENT
        # =================================

        elif task_type == "experiment":

            return (
                self.experiment_agent
                .generate_experiment_plan(
                    user_input
                )
            )

        return "Unknown task type."