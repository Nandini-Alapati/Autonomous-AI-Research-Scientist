from src.embeddings import (
    create_query_embedding
)

from src.vector_store import (
    search_chunks
)

from src.llm_engine import (
    generate_answer
)

# =========================================
# ASK QUESTION
# =========================================

def ask_question(
    question,
    selected_papers=None
):

    # =====================================
    # CREATE QUERY EMBEDDING
    # =====================================

    query_embedding = (
        create_query_embedding(
            question
        )
    )

    # =====================================
    # SEARCH CHUNKS
    # =====================================

    results = search_chunks(

        query_embedding=query_embedding,

        selected_papers=selected_papers,

        n_results=5
    )

    retrieved_chunks = (
        results["documents"][0]
    )

    retrieved_metadata = (
        results["metadatas"][0]
    )

    # =====================================
    # BUILD CONTEXT
    # =====================================

    context_parts = []

    structured_sources = []

    for chunk, metadata in zip(
        retrieved_chunks,
        retrieved_metadata
    ):

        paper_name = metadata[
            "paper_name"
        ]

        chunk_id = metadata[
            "chunk_id"
        ]

        formatted_chunk = f"""
Paper: {paper_name}

Chunk ID: {chunk_id}

Content:
{chunk}
"""

        context_parts.append(
            formatted_chunk
        )

        structured_sources.append({

            "paper_name": paper_name,

            "chunk_id": chunk_id,

            "content": chunk

        })

    # =====================================
    # FINAL CONTEXT
    # =====================================

    context = "\n\n".join(
        context_parts
    )

    # =====================================
    # GENERATE ANSWER
    # =====================================

    answer = generate_answer(

        context=context,

        question=question
    )

    # =====================================
    # RETURN STRUCTURED RESPONSE
    # =====================================

    return {

        "answer": answer,

        "sources": structured_sources
    }