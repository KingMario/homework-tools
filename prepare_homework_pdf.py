import fitz  # PyMuPDF
import argparse
import os

def redact_text_in_area(page, delete_rect):
    # Get all text blocks on the page
    text_instances = page.get_text("blocks")

    # Delete text blocks in the specified area
    for inst in text_instances:
        block_rect = fitz.Rect(inst[:4])
        if delete_rect.intersects(block_rect):
            page.add_redact_annot(block_rect, fill=(1, 1, 1))
    page.apply_redactions()

def prepare_homework_pdf(pdf_path, page_num, delete_ratio):
    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Duplicate the specified page and insert it after the original page
    doc.fullcopy_page(page_num - 1, page_num)

    # Re-fetch the specified page after duplication
    page = doc[page_num - 1]

    # Get the height of the page
    page_height = page.rect.height

    # Define the area to delete (bottom part of the page with the specified ratio)
    delete_rect = fitz.Rect(
        0, page_height * (1 - delete_ratio), page.rect.width, page_height
    )

    # Delete text in the specified area on the original page
    redact_text_in_area(page, delete_rect)

    # Process the next page
    next_page = doc[page_num]
    next_page_height = next_page.rect.height

    # Define the area to delete (top part of the next page with the specified ratio)
    delete_rect_next_page = fitz.Rect(
        0, 0, next_page.rect.width, next_page_height * (1 - delete_ratio)
    )

    # Delete text in the specified area on the next page
    redact_text_in_area(next_page, delete_rect_next_page)

    # Save the modified PDF file
    output_path = pdf_path.replace(".pdf", "_modified.pdf")
    doc.save(output_path)
    doc.close()
    print(f"Modified PDF saved as {output_path}")

    # Open the modified PDF file using macOS 'open' command
    os.system(f"open '{output_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Remove text from the bottom part of a specified page in a PDF file."
    )
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file.")
    parser.add_argument(
        "page_num", type=int, help="Page number to modify (1-based index)."
    )
    parser.add_argument(
        "delete_ratio",
        type=float,
        help="Ratio of the bottom part to delete (0.0 to 1.0).",
    )

    args = parser.parse_args()

    prepare_homework_pdf(args.pdf_path, args.page_num, args.delete_ratio)