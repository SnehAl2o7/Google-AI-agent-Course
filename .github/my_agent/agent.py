from google.adk.agents import Agent
from google.adk.tools import google_search

# Use a Gemini 2 model (required for google_search tool)
# Swap to 'gemini-2.5-flash' if you want more capability.
root_agent = Agent(
    name="helpful_assistant",
    model="gemini-2.5-flash-lite",
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)
