from src.embeddings import create_query_embedding
from src.vector_store import search_chunks
from src.llm_engine import generate_answer

from src.memory_manager import (
    store_research_gap
)

def detect_research_gaps():

    # Generic query focused on limitations
    query = """
    limitations weaknesses challenges future work
    unexplored problems research gaps
    """

    # Create embedding
    query_embedding = create_query_embedding(
        query
    )

    # Retrieve more context
    results = search_chunks(
        query_embedding,
        n_results=12
    )

    retrieved_chunks = results["documents"][0]

    retrieved_metadata = results["metadatas"][0]

    # Build context
    context_parts = []

    sources = []

    for chunk, metadata in zip(
        retrieved_chunks,
        retrieved_metadata
    ):

        paper_name = metadata["paper_name"]

        chunk_id = metadata["chunk_id"]

        formatted_chunk = f"""
Paper Name: {paper_name}

Chunk ID: {chunk_id}

Content:
{chunk}
"""

        context_parts.append(
            formatted_chunk
        )

        sources.append(
            f"{paper_name} (Chunk {chunk_id})"
        )

    # Combined context
    context = "\n\n".join(
        context_parts
    )

    # Research gap analysis question
    question = """
Analyze the research papers and identify:

1. Common limitations
2. Unsolved problems
3. Weaknesses in current approaches
4. Missing research directions
5. Potential future improvements
6. Novel research opportunities

Provide detailed academic analysis.
"""

    # Generate response
    answer = generate_answer(
        context=context,
        question=question
    )

    # Final response
    final_response = f"""
{answer}

Sources:
""" + "\n".join(
        [f"- {source}" for source in sources]
    )

    # =========================================
    # STORE IN MEMORY
    # =========================================

    store_research_gap(
        final_response
    )

    return final_response