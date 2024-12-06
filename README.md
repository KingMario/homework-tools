# PDF Homework Tools

## Introduction

When preparing homework for your child, sometimes the homework includes reference answers. If the reference answers are on a new page, you can simply print the pages before the answer page. However, if the reference answers do not start at the beginning of a page, you need to cover the answers on that page before printing. Simply covering the answers may not meet the need for fully printing the answers.

## Solution

For situations where the (partial) homework and (partial) answers are on the same page, you can copy the page and cover the answer and homework parts separately to get pages that can be printed separately.

The solution is divided into manual and automatic methods.

### Manual Method

Specify the PDF document path, page number, and the proportion of the page from the bottom up that needs to be covered.

### Automatic Method

Specify the target text to search for (e.g., "reference answer"), then automatically search for the page containing the target text, find the best coverage proportion through inspection, and process it in the same way as the manual method.

You can also set the target text using the environment variable `APHP_TARGET_TEXT`.

The benefit of using the environment variable `APHP_TARGET_TEXT` is that it simplifies the command for multiple PDF documents with the same target text.

## Scripts

### `prepare_homework_pdf.py`

This script allows you to manually specify the PDF document path, page number, and the proportion of the page to cover from the bottom up.

### `auto_prepare_homework_pdf.py`

This script allows you to specify the target text to search for, automatically find the page containing the target text, determine the best coverage proportion, and process the page accordingly.

## Usage

### Manual Method

```bash
python prepare_homework_pdf.py <pdf_path> <page_number> <cover_ratio>
```

### Automatic Method

```bash
python auto_prepare_homework_pdf.py <pdf_path> <target_text>
```

Alternatively, you can set the target text using the environment variable `APHP_TARGET_TEXT`:

```bash
export APHP_TARGET_TEXT="reference answer"
python auto_prepare_homework_pdf.py <pdf_path>
```

## Requirements

- Python 3.x
- PyMuPDF

Install the required packages using:

```bash
pip install PyMuPDF
```

## License

This project is licensed under the MIT License.