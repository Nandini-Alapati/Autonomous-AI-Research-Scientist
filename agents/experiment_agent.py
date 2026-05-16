# =========================================
# EXPERIMENT AGENT
# =========================================

class ExperimentAgent:

    def __init__(
        self,
        context_manager
    ):

        self.context_manager = (
            context_manager
        )

    # =====================================
    # GENERATE EXPERIMENT PLAN
    # =====================================

    def generate_experiment_plan(
        self,
        research_topic
    ):

        if not research_topic:

            return """
No research topic provided.
"""

        return f"""

# Experiment Plan

## Research Topic
{research_topic}

---

## Proposed Experimental Steps

1. Collect relevant datasets

2. Perform preprocessing and cleaning

3. Split dataset into train/test sets

4. Train baseline models

5. Evaluate performance metrics

6. Compare results with existing methods

7. Analyze limitations and future improvements

---

## Suggested Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

---

## Expected Outcome

A structured experimental pipeline for validating
the proposed research methodology.

"""