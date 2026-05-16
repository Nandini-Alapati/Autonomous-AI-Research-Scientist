import chromadb
import os

# =========================================
# CHROMA DB CONFIG
# =========================================

CHROMA_DB_DIR = "data/chroma_db"

os.makedirs(
    CHROMA_DB_DIR,
    exist_ok=True
)

# =========================================
# PERSISTENT CLIENT
# =========================================

client = chromadb.PersistentClient(
    path=CHROMA_DB_DIR
)

# =========================================
# COLLECTION
# =========================================

collection = client.get_or_create_collection(
    name="research_papers"
)

# =========================================
# CHECK PAPER EXISTS
# =========================================

def paper_already_exists(
    paper_name
):

    results = collection.get(
        where={
            "paper_name": paper_name
        }
    )

    return len(results["ids"]) > 0

# =========================================
# STORE CHUNKS
# =========================================

def store_chunks(
    chunks,
    embeddings,
    paper_name
):

    if paper_already_exists(
        paper_name
    ):

        print(
            f"{paper_name} already exists."
        )

        return

    ids = []
    documents = []
    embedding_list = []
    metadatas = []

    for i, (
        chunk,
        embedding
    ) in enumerate(
        zip(chunks, embeddings)
    ):

        chunk_id = (
            f"{paper_name}_chunk_{i}"
        )

        ids.append(chunk_id)

        documents.append(chunk)

        embedding_list.append(
            embedding.tolist()
        )

        metadatas.append({

            "paper_name": paper_name,

            "chunk_id": i

        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embedding_list,
        metadatas=metadatas
    )

# =========================================
# GET ALL PAPERS
# =========================================

def get_all_papers():

    results = collection.get()

    metadatas = results.get(
        "metadatas",
        []
    )

    paper_names = set()

    for metadata in metadatas:

        if (
            metadata
            and "paper_name" in metadata
        ):

            paper_names.add(
                metadata["paper_name"]
            )

    return sorted(
        list(paper_names)
    )

# =========================================
# SEARCH CHUNKS
# =========================================

def search_chunks(
    query_embedding,
    selected_papers=None,
    n_results=5
):

    # =====================================
    # FILTERED SEARCH
    # =====================================

    if (
        selected_papers
        and len(selected_papers) > 0
    ):

        if len(selected_papers) == 1:

            where_filter = {
                "paper_name": (
                    selected_papers[0]
                )
            }

        else:

            where_filter = {
                "$or": [

                    {
                        "paper_name": paper
                    }

                    for paper in selected_papers
                ]
            }

        results = collection.query(

            query_embeddings=[
                query_embedding.tolist()
            ],

            n_results=n_results,

            where=where_filter
        )

    # =====================================
    # GLOBAL SEARCH
    # =====================================

    else:

        results = collection.query(

            query_embeddings=[
                query_embedding.tolist()
            ],

            n_results=n_results
        )

    return results