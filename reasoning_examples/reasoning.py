from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
# openai.api_key=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
task = "Prove that for any positive integer n, the sum of the first n odd numbers is equal to n squared. Provide a detailed proof."

reasoning_agent = Agent(model=Groq(id="llama-3.1-70b-versatile"), reasoning=True, markdown=True, structured_outputs=True)
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)