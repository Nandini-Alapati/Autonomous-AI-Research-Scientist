from src.embeddings import create_query_embedding
from src.vector_store import search_chunks
from src.llm_engine import generate_answer

def compare_papers(comparison_topic):

    # Create query embedding
    query_embedding = create_query_embedding(
        comparison_topic
    )

    # Retrieve more chunks for comparison
    results = search_chunks(
        query_embedding,
        n_results=10
    )

    retrieved_chunks = results["documents"][0]

    retrieved_metadata = results["metadatas"][0]

    # Build structured context
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

    # Combined comparison context
    comparison_context = "\n\n".join(
        context_parts
    )

    # Comparison question
    comparison_question = f"""
Compare the uploaded research papers based on:

{comparison_topic}

Include:
- similarities
- differences
- strengths
- weaknesses
- important observations
"""

    # Generate comparison answer
    answer = generate_answer(
        context=comparison_context,
        question=comparison_question
    )

    # Add sources
    final_response = f"""
{answer}

Sources:
""" + "\n".join(
        [f"- {source}" for source in sources]
    )

    return final_response