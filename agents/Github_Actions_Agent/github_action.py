from phi.agent import Agent
import os
from phi.tools.github import GithubTools
from phi.model.google import Gemini
from dotenv import load_dotenv
load_dotenv()
access_token=os.getenv("GITHUB_ACCESS_TOKEN")
api_key=os.getenv("GOOGLE_API_KEY")
agent = Agent(
    model=Gemini(api_key=api_key,id="gemini-2.0-flash-exp"),
    instructions=[
        "Use your tools to answer questions about the repo: phidatahq/phidata",
        "Do not create any issues or pull requests unless explicitly asked to do so",
    ],
    tools=[GithubTools(access_token=access_token,base_url="https://github.com/Prathmesh-ChumsAI")],
)

agent.print_response("What is the latest opened issue?", markdown=True)
