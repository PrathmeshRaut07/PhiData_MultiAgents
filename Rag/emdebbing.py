from phi.agent import AgentKnowledge
from phi.vectordb.pgvector import PgVector
from phi.embedder.google import GeminiEmbedder
import os
api_key=os.getenv("GOOGLE_API_KEY")
embeddings = GeminiEmbedder(api_key=api_key).get_embedding("The quick brown fox jumps over the lazy dog.")

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Example usage:
knowledge_base = AgentKnowledge(
    vector_db=PgVector(
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        table_name="gemini_embeddings",
        embedder=GeminiEmbedder(dimensions=1536),
    ),
    num_documents=2,
)