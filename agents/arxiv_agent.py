from phi.agent import Agent
from phi.tools.arxiv_toolkit import ArxivToolkit
from dotenv import load_dotenv
from phi.model.groq import Groq
import os

load_dotenv()
# openai.api_key=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
agent = Agent(model=Groq(id="llama-3.1-70b-versatile"),tools=[ArxivToolkit()], show_tool_calls=True)
agent.print_response("Search arxiv for 'language models'", markdown=True)
