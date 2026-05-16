from src.research_gap_detector import (
    detect_research_gaps
)

# =========================================
# REVIEWER AGENT
# =========================================

class ReviewerAgent:

    def __init__(
        self,
        context_manager
    ):

        self.context_manager = (
            context_manager
        )

    # =====================================
    # REVIEW PAPERS
    # =====================================

    def review_research(self):

        gap_analysis = (
            detect_research_gaps()
        )

        self.context_manager.add_gap(
            gap_analysis
        )

        return gap_analysis