import os
import json

# =========================================
# MEMORY SETUP
# =========================================

MEMORY_DIR = "data/memory"

os.makedirs(MEMORY_DIR, exist_ok=True)

MEMORY_FILE = os.path.join(
    MEMORY_DIR,
    "research_memory.json"
)

# =========================================
# INITIALIZE MEMORY
# =========================================

def initialize_memory():

    if not os.path.exists(MEMORY_FILE):

        initial_data = {
            "literature_reviews": [],
            "research_gaps": [],
            "future_work": [],
            "notes": []
        }

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                initial_data,
                f,
                indent=4
            )

# =========================================
# LOAD MEMORY
# =========================================

def load_memory():

    initialize_memory()

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        memory = json.load(f)

    return memory

# =========================================
# SAVE MEMORY
# =========================================

def save_memory(memory):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memory,
            f,
            indent=4
        )

# =========================================
# STORE LITERATURE REVIEW
# =========================================

def store_literature_review(review_text):

    memory = load_memory()

    memory["literature_reviews"].append(
        review_text
    )

    save_memory(memory)

# =========================================
# STORE RESEARCH GAP
# =========================================

def store_research_gap(gap_text):

    memory = load_memory()

    memory["research_gaps"].append(
        gap_text
    )

    save_memory(memory)

# =========================================
# STORE FUTURE WORK
# =========================================

def store_future_work(future_text):

    memory = load_memory()

    memory["future_work"].append(
        future_text
    )

    save_memory(memory)

# =========================================
# STORE NOTE
# =========================================

def store_note(note):

    memory = load_memory()

    memory["notes"].append(
        note
    )

    save_memory(memory)

# =========================================
# GET MEMORY SECTIONS
# =========================================

def get_literature_reviews():

    memory = load_memory()

    return memory["literature_reviews"]

def get_research_gaps():

    memory = load_memory()

    return memory["research_gaps"]

def get_future_work():

    memory = load_memory()

    return memory["future_work"]

def get_notes():

    memory = load_memory()

    return memory["notes"]

# =========================================
# DELETE NOTE
# =========================================

def delete_note(note_index):

    memory = load_memory()

    if 0 <= note_index < len(
        memory["notes"]
    ):

        memory["notes"].pop(
            note_index
        )

        save_memory(memory)