# DBT GitHub Conversational AI Agent

A conversational AI agent that answers questions about the Data Build Tool (dbt) GitHub repository using search, Agentic RAG, and LLMs.

## Project Highlights
- Built a conversational AI agent over a GitHub repository
- Built an Agentic RAG pipeline
- Processed code and documentation with embeddings
- Added evaluation and testing pipeline
- Deployed with a simple UI

## Demo
Watch the Streamlit interface in action:

![streamlit](images/streamlit.gif)

Watch the CLI interface in action:

![cli](images/cli.gif)

## Overview
This project ingests and indexes the Data Build Tool (dbt) GitHub repository, processes repository code and documentation using AI, and allows users to ask questions about the repository through a conversational interface.

The system uses lexical search combined with an Agentic Retrieval Augmented Generation (RAG) pipeline to retrieve relevant context and generate accurate, context-aware answers.


## Tech Stack
- Python
- OpenAI API
- Streamlit

## Installation

### Clone the repository
```bash
git clone https://github.com/shahi2099/dbt-ai-agent.git
cd dbt-ai-agent
```

### Create virtual environment

```bash
cd app/
uv sync
```

### Add environment variables
```bash
export OPENAI_API_KEY="your_api_key"
```

## Usage

CLI mode
```bash
uv run main.py
```
This opens an interactive CLI environment. You can ask the conversational agent any question about Data Build Tool (DBT).

Web UI mode
```bash
uv run streamlit run app.py
```
This launches a Streamlit app. You can chat with the assistant in your browser.

The app is available at http://localhost:8501.


Example questions:
- What is a dbt model and how does it work?
- What is the difference between a view and a table in dbt?
- What are incremental models in dbt?
- What is a dbt test and how do I write one?

## Features
- GitHub repository ingestion
- Code + documentation processing with AI
- Agentic RAG pipeline
- Conversational interface
- Two interfaces: CLI (main.py) and Streamlit (app.py)
- Evaluation and testing
- Simple UI deployment


## Tests
We evaluate the agent using the following criteria:

- instructions_follow: The agent followed the user's instructions
- instructions_avoid: The agent avoided doing things it was told not to do
- answer_relevant: The response directly addresses the user's question
- answer_clear: The answer is clear and correct
- answer_citations: The response includes proper citations or sources when required
- completeness: The response is complete and covers all key aspects of the request
- tool_call_search: Is the search tool invoked?

We do this in two steps:

- First, we generate synthetic questions (see [app/eval/data-gen.ipynb](app/eval/data-gen.ipynb)).
- Next, we run our agent on the generated questions and check the criteria (see [app/eval/evaluations.ipynb](app/eval/evaluations.ipynb)) 

Current evaluation metrics:
```
instructions_follow    100.0
instructions_avoid     100.0
answer_relevant        100.0
answer_clear            93.3
answer_citations       100.0
completeness           100.0
tool_call_search        60.0
```

The most important metric for this project is answer_relevant. This measures whether the system's answer is relevant to the user. It's currently 100%, meaning all answers were relevant.

Improvements: Our evaluation is currently based on only 10 questions. We need to collect more data for a more comprehensive evaluation set.

## Project file overview
- app/main.py: Entry point for the CLI version of the assistant
- app/app.py: Streamlit-based web UI for the assistant
- app/ingest.py: Handles data ingestion and indexing from the GitHub DBT repository
- app/search_tools.py: Defines the search tool used by the agent
- app/search_agent.py: Defines and configures the AI Agent
- app/logs.py: Utility for logging all interactions
- app/eval/data-gen.ipynb — Notebook for generating synthetic questions.
- app/eval/evaluation.ipynb — Notebook for running evaluations.

## Deployment
Run the web mode application locally.
```bash
uv run streamlit run app.py
```

Streamlit deployment:
Click "deploy", connect your GitHub repo, and configure deployment settings.

In the settings, make sure you configure OPENAI_API_KEY.

Once configured, Streamlit Cloud will automatically detect changes. It will redeploy your app whenever you push updates.
