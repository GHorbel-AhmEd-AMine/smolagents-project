# SmolAgents

SmolAgents is a lightweight library designed by Hugging Face (https://huggingface.co/) to simplify the creation and execution of AI agents. It encapsulates agent logic in around 1,000 lines of code and supports both Code Agents and ToolCallingAgents. SmolAgents integrates seamlessly with LLMs like Hugging Face, OpenAI, Anthropic, and more.

## Why Choose SmolAgents?

- **Simplicity**: Simplifies dynamic workflows with minimal code.
- **Compatibility**: Works with any LLM and integrates with the Hugging Face Hub.
- **Secure Execution**: Supports sandboxed environments to ensure safety.
- **Flexibility**: Uses Python code instead of rigid JSON for greater flexibility.

### Key Features

- **Tool Calling**: Executes tasks via external tools (e.g., `get_weather("Paris")`).
- **Multi-Step Agents**: Manages loops with memory and context.
- **Code-Based Actions**: Uses Python instead of JSON for more flexibility.
- **Error Handling**: Logs and retries failed executions.
- **Secure Execution**: Ensures safety with sandboxed environments.

## Installation

1. Create a virtual environment for your project:
   ```bash
   python -m venv venv 
   ```
2. Activate the virtual environment:
   - On Windows: 
   ```
   bash .\venv\Scripts\activate 
   ``` 
   - On macOS/Linux:
    ```
   source venv/bin/activate 
   ``` 
3. Clone this repository to your local machine: 
   ```
   [git clone https://github.com/huggingface/smolagents.git](https://github.com/GHorbel-AhmEd-AMine/smolagents-project.git)
   cd smolagents-project
   If u want the official github of hugging face : git clone https://github.com/huggingface/smolagents.git
   ``` 
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ``` 

## Usage Examples

Here are two agent examples using SmolAgents: a research agent and a stock market agent.
### Example 1: research_agent.py
This example demonstrates how to use an agent to query general information about Generative AI via DuckDuckGo and a GPT-4 model.

**How it works:**

    - Loads an OpenAI API key from a .env file.
    - Uses the DuckDuckGoSearchTool to search for information on "Generative AI".
    - Runs the agent with a GPT-4 model to return relevant information.

**Instructions:**

1. Create a .env file and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

2. Run the script:
   ```bash
   python research_agent.py
   ```

### Example 2: stock_market_agent.py
This example shows how the agent uses DuckDuckGo for information searching and the yfinance library to fetch stock prices for Apple Inc.

**How it works:**

    - Loads an OpenAI API key from a .env file.
    - Uses yfinance to fetch stock prices for Apple (AAPL).
    - Runs the agent with a GPT-4 model to get the response.

**Instructions:**

1. Create a .env file and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

2. Run the script:
   ```bash
   python stock_market_agent.py
   ```

### Example 2: agentic_rag.py
This example demonstrates how to use a Retrieval-Augmented Generation (RAG) agent to retrieve and process information from a PDF document using semantic search.

**How it works:**

    - Loads an OpenAI API key from a .env file.
    - Loads and splits a PDF document into chunks using PyPDFLoader and RecursiveCharacterTextSplitter.
    - Creates a FAISS vector database for semantic search.
    - Uses a custom RetrieverTool to retrieve relevant documents based on a query.
    - Runs the agent with a GPT-4 model to process the query and return relevant information.

**Instructions:**

1. Create a .env file and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```
2. Place your PDF document in the Content folder and update the PDF_PATH variable in the script with the correct path.

3. Run the script:
   ```bash
   python agentic_rag.py
   ```


## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a branch for your feature (git checkout -b feature/your-feature).
3. Commit your changes (git commit -m 'Add new feature').
4. Push the branch (git push origin feature/your-feature).
5. Open a pull request.

