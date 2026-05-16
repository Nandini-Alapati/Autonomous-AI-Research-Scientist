# =========================================
# RESEARCH CONTEXT MANAGER
# =========================================

class ResearchContext:

    def __init__(self):

        self.active_papers = []

        self.chat_history = []

        self.retrieved_sources = []

        self.notes = []

        self.generated_reviews = []

        self.research_gaps = []

        self.future_work = []

    # =====================================
    # ACTIVE PAPERS
    # =====================================

    def set_active_papers(
        self,
        papers
    ):

        self.active_papers = papers

    def get_active_papers(self):

        return self.active_papers

    # =====================================
    # CHAT HISTORY
    # =====================================

    def add_chat_message(
        self,
        role,
        content
    ):

        self.chat_history.append({

            "role": role,

            "content": content
        })

    def get_chat_history(self):

        return self.chat_history

    # =====================================
    # SOURCES
    # =====================================

    def set_sources(
        self,
        sources
    ):

        self.retrieved_sources = sources

    def get_sources(self):

        return self.retrieved_sources

    # =====================================
    # NOTES
    # =====================================

    def add_note(
        self,
        note
    ):

        self.notes.append(note)

    def get_notes(self):

        return self.notes

    # =====================================
    # LITERATURE REVIEWS
    # =====================================

    def add_review(
        self,
        review
    ):

        self.generated_reviews.append(
            review
        )

    def get_reviews(self):

        return self.generated_reviews

    # =====================================
    # RESEARCH GAPS
    # =====================================

    def add_gap(
        self,
        gap
    ):

        self.research_gaps.append(
            gap
        )

    def get_gaps(self):

        return self.research_gaps

    # =====================================
    # FUTURE WORK
    # =====================================

    def add_future_work(
        self,
        item
    ):

        self.future_work.append(
            item
        )

    def get_future_work(self):

        return self.future_work