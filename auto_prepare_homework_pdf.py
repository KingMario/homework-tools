import fitz  # PyMuPDF
import argparse
import os
from prepare_homework_pdf import prepare_homework_pdf


def find_min_ratio(page, target_text):
    # Get the height of the page
    page_height = page.rect.height

    # Try different ratios to find the minimum ratio that covers the target text
    ratio = 0.05
    while ratio <= 1.0:
        delete_rect = fitz.Rect(
            0, page_height * (1 - ratio), page.rect.width, page_height
        )
        text_instances = page.get_text("blocks")
        for inst in text_instances:
            block_rect = fitz.Rect(inst[:4])
            if delete_rect.intersects(block_rect) and target_text in inst[4]:
                return ratio
        ratio += 0.05
    return 1.0


def process_pdf(pdf_path, target_text):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    for page_num in range(len(doc)):
        page = doc[page_num]
        text_instances = page.search_for(target_text)

        if text_instances:
            print(f"Found target text on page {page_num + 1}")

            # Duplicate the specified page and insert it after the original page
            doc.fullcopy_page(page_num, page_num + 1)

            # Re-fetch the specified page and the duplicated page
            original_page = doc[page_num]
            duplicated_page = doc[page_num + 1]

            # Find the minimum ratio that covers the target text
            min_ratio = find_min_ratio(original_page, target_text)
            print(f"Minimum ratio to cover target text: {min_ratio}")

            prepare_homework_pdf(pdf_path, page_num + 1, min_ratio)
            break

    print("Target text not found in the document.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find and redact specified text in a PDF file."
    )
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file.")
    parser.add_argument(
        "target_text", type=str, nargs="?", help="Text block to search for."
    )

    args = parser.parse_args()

    target_text = args.target_text or os.getenv("APHP_TARGET_TEXT")

    if not target_text:
        print(
            "Please specify the target_text as a command line argument or set it in the environment variable 'APHP_TARGET_TEXT'."
        )
    else:
        process_pdf(args.pdf_path, target_text)
