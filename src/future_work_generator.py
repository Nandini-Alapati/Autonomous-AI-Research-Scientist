from src.embeddings import create_query_embedding
from src.vector_store import search_chunks
from src.llm_engine import generate_answer

from src.memory_manager import (
    store_future_work
)

def generate_future_work():

    # Future-work focused retrieval query
    future_query = """
    future work limitations improvements
    challenges optimization unexplored directions
    """

    # Create embedding
    query_embedding = create_query_embedding(
        future_query
    )

    # Retrieve broader context
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

    # Prompt
    question = """
Based on the uploaded research papers,
generate future research directions.

Include:

1. Potential model improvements
2. New experimental ideas
3. Dataset enhancements
4. Architecture innovations
5. Optimization opportunities
6. Hybrid approaches
7. Real-world deployment improvements
8. Novel research directions

Provide detailed academic suggestions.
"""

    # Generate answer
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

    store_future_work(
        final_response
    )

    return final_response