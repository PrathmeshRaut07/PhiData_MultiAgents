import typer
from typing import Optional
from phi.agent import Agent
from rich.prompt import Prompt
from phi.vectordb.chroma import ChromaDb
from phi.knowledge.pdf import PDFUrlKnowledgeBase
import os
from phi.model.groq import Groq
from phi.storage.agent.sqlite import SqlAgentStorage
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = Groq(id="llama-3.1-70b-versatile")
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

knowledge_base = PDFUrlKnowledgeBase(
  urls = ["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
  vector_db= ChromaDb(collection="recipes_with_memory_new"),
  embedder = embedder
)

knowledge_base.load()
# Set up SQL storage for the agent's data
storage = SqlAgentStorage(table_name="recipes_with_memory_table_new_latest", db_file="data_new.db")
storage.create()  # Create the storage if it doesn't exist

def pdf_agent(user:str = "user"):
  run_id: Optional[str] = None
  
  agent = Agent(
    run_id = run_id,
    user_id=user,
    model=model,
    knowledge_base=knowledge_base,
    use_tools=True,
    show_tool_calls=True,
    #debug_mode=True,
    read_chat_history=True,
     storage=storage,
  )
  if run_id is None:
      run_id = agent.run_id
      print(f"Started Run: {run_id}\n")
  else:
      print(f"Continuing Run: {run_id}\n")
      
  while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in ("exit", "bye"):
            break
        agent.print_response(message)
        
if __name__ == "__main__":
    typer.run(pdf_agent)