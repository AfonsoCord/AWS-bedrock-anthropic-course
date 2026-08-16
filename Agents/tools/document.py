from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pathlib import Path
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    file_path: str = Field(description="Path to DOCX or PDF file (absolute or relative)")
) -> str:
    """Converts a document file to markdown-formatted text.

    This tool reads a DOCX or PDF file from the specified path and converts
    its contents to readable markdown-formatted text using the MarkItDown library.

    When to use:
    - Converting DOCX files to markdown
    - Converting PDF files to markdown
    - Extracting text content from document files for processing
    - When you have a file path rather than binary data

    When NOT to use:
    - For documents already in text format (use direct file reading instead)
    - For image-only PDFs with no text content (limited OCR support)
    - For very large files (>100MB) requiring streaming processing

    Examples:
    >>> result = document_path_to_markdown('/path/to/document.pdf')
    >>> print(result[:100])
    # Document Title
    Some content here...

    >>> result = document_path_to_markdown('relative/path/file.docx')
    >>> len(result) > 0
    True
    """
    path = Path(file_path)

    file_extension = path.suffix.lower().lstrip('.')

    if file_extension not in ('pdf', 'docx'):
        raise ValueError(
            f"Unsupported file type: {file_extension}. "
            "Supported types are: pdf, docx"
        )

    if not path.exists():
        raise FileNotFoundError(f"Document file not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    with open(path, 'rb') as f:
        binary_data = f.read()

    return binary_document_to_markdown(binary_data, file_extension)
