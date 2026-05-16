from src.literature_review_generator import (
    generate_literature_review
)

# =========================================
# LITERATURE AGENT
# =========================================

class LiteratureAgent:

    def __init__(
        self,
        context_manager
    ):

        self.context_manager = (
            context_manager
        )

    # =====================================
    # GENERATE LITERATURE REVIEW
    # =====================================

    def generate_review(self):

        review = (
            generate_literature_review()
        )

        self.context_manager.add_review(
            review
        )

        return review