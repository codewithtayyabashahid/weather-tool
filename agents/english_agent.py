from langchain.agents import OpenAIAgent
from tools.weather_tool import get_weather

english_agent = OpenAIAgent(
    name="english_agent",
    instructions="You will respond to queries in English.",
    tools=[get_weather]
)
