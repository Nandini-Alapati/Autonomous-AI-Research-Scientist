from langchain_text_splitters import RecursiveCharacterTextSplitter

def clean_text(text):

    # Remove excessive whitespace
    text = text.replace("\n", " ")

    text = " ".join(text.split())

    return text

def chunk_text(text):

    # Clean text first
    cleaned_text = clean_text(text)

    # Research-paper optimized splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_text(cleaned_text)

    # Remove tiny noisy chunks
    filtered_chunks = [
        chunk.strip()
        for chunk in chunks
        if len(chunk.strip()) > 50
    ]

    return filtered_chunks