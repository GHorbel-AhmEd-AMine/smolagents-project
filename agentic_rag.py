import os
from pathlib import Path
from dotenv import load_dotenv
from smolagents import Tool, LiteLLMModel, DuckDuckGoSearchTool, CodeAgent
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

load_dotenv()

class DocumentProcessor:
    """Class for loading and processing PDF documents."""

    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"The file {self.pdf_path} does not exist.")

    def load_and_split_documents(self):
        """Load a PDF file and split the documents into chunks."""
        loader = PyPDFLoader(str(self.pdf_path))
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
        return splitter.split_documents(pages)

class VectorDBManager:
    """Class for managing the vector database."""

    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key
        if not self.openai_api_key:
            raise ValueError("The OpenAI API key is missing in the .env file.")

    def create_vector_db(self, documents):
        """Create a FAISS vector database from the documents."""
        embed_model = OpenAIEmbeddings(openai_api_key=self.openai_api_key)
        return FAISS.from_documents(documents=documents, embedding=embed_model)

class RetrieverTool(Tool):
    """Semantic search tool to retrieve relevant documents."""

    name = "retriever"
    description = "Uses semantic search to retrieve the parts of the documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question.",
        }
    }

    output_type = "string"

    def __init__(self, vector_db, **kwargs):
        super().__init__(**kwargs)
        self.vector_db = vector_db

    def forward(self, query: str) -> str:
        assert isinstance(query, str), "Your search query must be a string"
        docs = self.vector_db.similarity_search(query, k=4)
        return "\nRetrieved documents:\n" + "".join(
            [f"\n===Document {i}=====\n" + doc.page_content for i, doc in enumerate(docs)]
        )

class RAGAgent:
    """Main class to manage the RAG agent."""

    def __init__(self, pdf_path: Path, openai_api_key: str):
        self.pdf_path = pdf_path
        self.openai_api_key = openai_api_key

        self.document_processor = DocumentProcessor(self.pdf_path)
        self.splitted_docs = self.document_processor.load_and_split_documents()

        self.vector_db_manager = VectorDBManager(self.openai_api_key)
        self.vector_db = self.vector_db_manager.create_vector_db(self.splitted_docs)

        self.retriever_tool = RetrieverTool(vector_db=self.vector_db)

        self.model = LiteLLMModel(model_id="gpt-4o", api_key=self.openai_api_key)
        self.search_tool = DuckDuckGoSearchTool()

        self.agent = CodeAgent(
            tools=[self.retriever_tool, self.search_tool], model=self.model, max_steps=6
        )

    def run(self, query: str):
        """Run the agent with the given query."""
        return self.agent.run(query)

if __name__ == "__main__":
    PDF_PATH = Path("path_to_content")

    openai_api_key = os.getenv("OPENAI_API_KEY")

    rag_agent = RAGAgent(PDF_PATH, openai_api_key)
    result = rag_agent.run("your-query")
    print(result)