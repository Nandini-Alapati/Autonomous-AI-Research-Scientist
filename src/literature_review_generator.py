from src.embeddings import create_query_embedding
from src.vector_store import search_chunks
from src.llm_engine import generate_answer

from src.memory_manager import (
    store_literature_review
)

def generate_literature_review():

    # Broad retrieval query
    review_query = """
    methodology datasets experiments results
    limitations future work contributions
    """

    # Create embedding
    query_embedding = create_query_embedding(
        review_query
    )

    # Retrieve broader research context
    results = search_chunks(
        query_embedding,
        n_results=15
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

    # Literature review prompt
    question = """
Generate a detailed academic literature review
based on the uploaded research papers.

Include:

1. Introduction
2. Existing methodologies
3. Datasets used
4. Comparative analysis
5. Strengths and weaknesses
6. Research trends
7. Limitations
8. Conclusion

Write in formal academic style.
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

    store_literature_review(
        final_response
    )

    return final_response