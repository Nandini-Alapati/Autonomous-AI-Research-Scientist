from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    pages_data = []

    full_text = ""

    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        extracted_text = page.extract_text()

        if extracted_text:

            cleaned_text = extracted_text.strip()

            # Store page-wise data
            page_info = {
                "page_number": page_number,
                "text": cleaned_text
            }

            pages_data.append(page_info)

            # Combine full text
            full_text += cleaned_text + "\n"

    return {
        "full_text": full_text,
        "pages": pages_data
    }