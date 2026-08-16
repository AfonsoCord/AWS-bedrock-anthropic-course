# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) server for document-related tools. It exposes document conversion and processing capabilities through an MCP interface, allowing AI assistants to interact with tools for converting and analyzing documents.

## Development Commands

### Setup
```bash
# Create and activate virtual environment
uv venv
.venv\Scripts\Activate.ps1  # On Windows PowerShell
source .venv/bin/activate    # On Unix/macOS

# Install dependencies in development mode
uv pip install -e .
```

### Running
```bash
# Start the MCP server
uv run main.py
```

### Testing
```bash
# Run all tests
uv run pytest

# Run tests for a specific module
uv run pytest tests/test_document.py

# Run a specific test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

### MCP Server Structure
- **Entry Point** (`main.py`): Uses FastMCP to create and configure the MCP server
- **Tool Registration**: Tools are Python functions decorated with `@mcp.tool()` and registered with the server
- **Tools Directory** (`tools/`): Contains individual tool implementations

### Tool Development Pattern

Tools follow a standardized pattern using Pydantic Field for parameter documentation:

```python
from pydantic import Field

def tool_name(
    param1: str = Field(description="Description of param1"),
    param2: int = Field(description="Description of param2"),
) -> ReturnType:
    """Brief description.
    
    Detailed explanation of functionality.
    
    When to use:
    - Use case 1
    - Use case 2
    
    Examples:
    >>> tool_name("example", 42)
    expected_output
    """
    # Implementation
    pass
```

### Defining MCP Tools

Tools are defined as Python functions and registered with the MCP server. Follow this pattern:

**Registration**:
```python
from mcp.server.fastmcp import FastMCP
from tools.my_tool import my_function

mcp = FastMCP("server-name")
mcp.tool()(my_function)  # Register the tool
```

**Tool Definition Template**:
```python
from pydantic import Field

def my_function(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does")
) -> ReturnType:
    """Comprehensive docstring here"""
    # Implementation
```

**Docstring Requirements**:
Tool descriptions should:
1. Begin with a one-line summary
2. Provide detailed explanation of functionality
3. Explain when to use (and not use) the tool
4. Include usage examples with expected input/output

**Example**:
```python
from pydantic import Field

def binary_to_markdown(
    binary_data: bytes = Field(description="Binary content of the document"),
    file_type: str = Field(description="File extension: 'pdf', 'docx', etc."),
) -> str:
    """Converts binary documents to markdown format.
    
    This tool takes binary document data and converts it to readable
    markdown-formatted text using the MarkItDown library.
    
    When to use:
    - Converting PDFs to markdown
    - Converting DOCX documents to markdown
    - Extracting text from binary document formats
    
    When NOT to use:
    - For documents already in text format
    - For image-only PDFs (limited OCR support)
    
    Examples:
    >>> with open('document.pdf', 'rb') as f:
    ...     result = binary_to_markdown(f.read(), 'pdf')
    >>> print(result[:100])
    # Document Title...
    """
    # Implementation
```

### Current Tools

**document.py**: `binary_document_to_markdown(binary_data, file_type)`
- Converts binary document data (DOCX, PDF) to markdown text
- Uses MarkItDown library for robust conversion
- Returns markdown-formatted string

**math.py**: `add(a, b)`
- Example tool demonstrating basic functionality
- Used as a template for tool structure

### Key Dependencies

- **markitdown**: Document format conversion (DOCX, PDF, etc. to markdown)
- **mcp**: Model Context Protocol framework with FastMCP for rapid server development
- **pydantic**: Data validation and parameter documentation using Field descriptors
- **pytest**: Testing framework; test fixtures stored in `tests/fixtures/`

### Testing

Tests are located in `tests/` with fixtures in `tests/fixtures/`:
- Use pytest fixtures for test data (DOCX and PDF files)
- Test both the conversion logic and proper error handling
- Verify output is valid markdown with expected formatting markers

## Code Guidelines

### Tool Descriptions (Critical for MCP)
When creating new tools, ensure docstrings include **all of the following**:
1. **One-line summary** at the start
2. **Detailed functionality explanation** - what the tool does and how it works
3. **"When to use" section** - specific use cases where this tool is appropriate
4. **"When NOT to use" section** - use cases where this tool should be avoided (optional but recommended)
5. **Usage examples** - concrete code examples with expected input/output

Poor descriptions result in poor tool usage by AI assistants. Be explicit about edge cases and limitations.

### Parameter Documentation (Exposed via MCP)
Always use Pydantic's `Field` with **detailed descriptive text** for all tool parameters:
```python
param_name: type = Field(description="Detailed, complete description of what this parameter does and expected format")
```

Parameter descriptions are exposed through the MCP interface and help AI assistants understand how to properly use the tool. Avoid generic descriptions like "the input" or "a value".

### Return Types
Always specify explicit return types. The MCP interface uses type hints to communicate the expected output format to AI assistants.

## Common Tasks

- **Add a new tool**: Create a function in `tools/` following the pattern above, then register with `mcp.tool()` in `main.py`
- **Test a conversion**: Place test file in `tests/fixtures/` and add test case to `test_document.py`
- **Debug server**: Run `uv run main.py` directly to see server startup messages and errors
