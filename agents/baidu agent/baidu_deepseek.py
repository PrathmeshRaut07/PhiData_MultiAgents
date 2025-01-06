from phi.agent import Agent
from phi.tools.baidusearch import BaiduSearch
from phi.model.openai.like import OpenAILike
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI model with Hyperbolic API
model = OpenAILike(
    id="deepseek-ai/DeepSeek-V3",  # Specify the model name
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.hyperbolic.xyz/v1",
)

# Define the agent
agent = Agent(
    tools=[BaiduSearch()],
    model=model,  # Use the OpenAIModel instance
    description="You are a search agent that helps users find the most relevant information using Baidu.",
    instructions=[
        "Given a topic by the user, respond with the 3 most relevant search results about that topic.",
        "Search for 5 results and select the top 3 unique items.",
        "Search in both English and Chinese.",
    ],
    show_tool_calls=True,
)

# Print the response from the agent
agent.print_response("What are the latest advancements in AI?", markdown=True)