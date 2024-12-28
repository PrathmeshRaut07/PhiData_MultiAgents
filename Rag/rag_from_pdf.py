"""
1. Run: `pip install openai lancedb tantivy pypdf sqlalchemy phidata cohere` to install the dependencies
2. Run: `python cookbook/rag/03_traditional_rag_lancedb.py` to run the agent
"""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.embedder.google import GeminiEmbedder
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.reranker.cohere import CohereReranker
from dotenv import load_dotenv
import os
load_dotenv()
# openai.api_key=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
api_key=os.getenv('GOOGLE_API_KEY')
# Create a knowledge base of PDFs from URLs

# Load the knowledge base: Comment after first run as the knowledge base is already loaded
knowledge_base.load()

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    # Add a tool to search the knowledge base which enables agentic RAG.
    # This is enabled by default when `knowledge` is provided to the Agent.
    search_knowledge=True,
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("How do I make chicken and galangal in coconut milk soup", stream=True)