from phi.agent import Agent
from phi.tools.file import FileTools
from phi.model.google import Gemini
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
agent = Agent(model=Gemini(api_key=api_key,id="gemini-2.0-flash-exp"),tools=[FileTools(base_dir=r"agents\FILETOOLS",save_files=r"agents\FILETOOLS")],show_tool_calls=True)
agent.print_response("What is the most advanced LLM ? Save the answer to a file to lam.txt.", markdown=True)