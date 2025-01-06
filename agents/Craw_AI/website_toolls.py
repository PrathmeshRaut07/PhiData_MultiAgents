from phi.agent import Agent
from phi.tools.website import WebsiteTools
from phi.model.google import Gemini
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
agent = Agent(model=Gemini(api_key=api_key,id="gemini-2.0-flash-exp"),tools=[WebsiteTools()], show_tool_calls=True)
agent.print_response("Search web page: 'https://docs.phidata.com/introduction'", markdown=True)