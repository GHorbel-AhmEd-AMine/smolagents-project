import os
from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

def load_api_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found. Make sure it is defined in the .env file under the key OPENAI_API_KEY.")
    return api_key

def initialize_agent(api_key):
    search_tool = DuckDuckGoSearchTool()
    model = LiteLLMModel(model_id="gpt-4", api_key=api_key)
    return CodeAgent(tools=[search_tool], model=model)

def main():
    api_key = load_api_key()
    agent = initialize_agent(api_key)
    response = agent.run("Tell me about Generative AI.")
    print(response)

if __name__ == "__main__":
    main()
