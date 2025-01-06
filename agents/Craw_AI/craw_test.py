from phi.agent import Agent
import os
from phi.tools.crawl4ai_tools import Crawl4aiTools
from phi.model.google import Gemini
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
agent = Agent( model=Gemini(api_key=api_key,id="gemini-2.0-flash-exp"),tools=[Crawl4aiTools(max_length=None)], show_tool_calls=True)
agent.print_response("Tell me about https://github.com/phidatahq/phidata.")