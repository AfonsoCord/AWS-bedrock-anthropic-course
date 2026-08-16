# AWS Bedrock Course

Notebooks and mini projects from a course on Amazon Bedrock and the Claude API, covering prompting, tool use, structured data, thinking, images, PDFs, prompt caching, retrieval augmented generation, an MCP server, and a command line agent.

## Workflow
1. Work through individual notebooks covering core Claude API features on Bedrock.
2. Build a retrieval augmented generation pipeline covering chunking, embeddings, vector search, BM25, hybrid search, and reranking.
3. Build an interactive chat CLI connected to Bedrock through the MCP protocol.
4. Build an MCP server exposing document processing tools.

## Technologies
Python, AWS Bedrock, Claude API, MCP, FastMCP, vector databases.

## Contents
* `bedrockinicial.ipynb`, `001_prompting.ipynb`, `001_tools.ipynb`, `003_exercise.ipynb`, `003_structured_data.ipynb`, `005_text_editor_tool.ipynb`, `promptevaluation.ipynb` individual exercises on the Claude API via Bedrock
* `ClaudeFeatures/` exercises on specific Claude features
* `RAG/` retrieval augmented generation pipeline
* `ProjectMCP/` interactive chat CLI connected to Bedrock via the MCP protocol
* `Agents/` Python package with document processing tools exposed via an MCP server

## Certification
AWS credential verification: https://verify.skilljar.com/c/6kmwabgvkwzo
