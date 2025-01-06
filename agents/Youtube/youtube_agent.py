from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.youtube_tools import YouTubeTools
import os
from dotenv import load_dotenv
load_dotenv()
# openai.api_key=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
agent = Agent(
    name="YouTube Timestamps Agent",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    instructions=[
        "You are a YouTube agent. First check the length of the video. Then get the detailed timestamps for a YouTube video corresponding to correct timestamps.",
        "Don't hallucinate timestamps.",
        "Make sure to return the timestamps in the format of `[start_time, end_time, summary]`.",
    ],
)
agent.print_response(
    "Get the detailed timestamps for this video https://www.youtube.com/watch?v=M5tx7VI-LFA", markdown=True
)
