# LangChain Tools and Agents

A collection of small Python examples for learning LangChain tools, runnable chains, prompt templates, model providers, and human-approved agent tool calls.

The examples use Google Gemini by default, with commented Mistral alternatives in several files.

## Contents

- `owntool.py` - Defines and invokes a simple custom greeting tool.
- `toolcalling.py` - Binds a text-length tool to an LLM and handles the tool call manually.
- `sequencerunnable.py` - Builds a prompt -> model -> string parser sequence.
- `runnablepassthrough.py` - Generates code, then passes it to a parallel code explanation chain.
- `parallelrunnable.py` - Runs short and detailed explanations in parallel.
- `news_summarizer.py` - Searches for current AI news with Tavily and summarizes it with an LLM.
- `agents.py` - Runs an interactive city assistant with weather and news tools, including approval before each tool call.
- `GenAIvideo3.pdf` - Local reference material.

## Requirements

- Python 3.10 or newer
- API access to Google Gemini and Tavily
- An OpenWeather API key for the weather tool in `agents.py`
- An optional Mistral API key if you enable the Mistral model examples

## Setup

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install tavily-python rich
```

`TavilyClient` and Rich are used by the examples but are not currently included in `requirements.txt`.

### 3. Configure environment variables

Create a local `.env` file in the project root:

```dotenv
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

Only add the keys needed for the example you are running. Never commit `.env` or expose API keys in source code.

## Running the examples

Run commands from the project root with the virtual environment activated:

```powershell
python owntool.py
python toolcalling.py
python sequencerunnable.py
python runnablepassthrough.py
python parallelrunnable.py
python news_summarizer.py
python agents.py
```

`toolcalling.py` and `agents.py` are interactive and wait for input in the terminal. Type `exit` in `agents.py` to stop the city assistant.

## What to expect

- The examples make live model or search requests, so they require network access and may incur provider costs.
- `agents.py` asks for approval before executing each weather or news tool call.
- `news_summarizer.py` searches for `Latest AI news of 2026` as written in the example.
- Most examples currently select `gemini-3.5-flash-lite`; update the model name in the source if your provider account uses a different available model.

## Project notes

These scripts are intentionally independent demonstrations rather than a packaged application. They load environment variables with `python-dotenv` and print results directly to the terminal.

The included `.gitignore` excludes local secrets, virtual environments, caches, generated output, and editor metadata.
