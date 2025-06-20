from langchain.agents import OpenAIAgent
from tools.weather_tool import get_weather

urdu_agent = OpenAIAgent(
    name="urdu_agent",
    instructions="آپ اردو میں پوچھے گئے سوالات کا جواب دیں گے۔",
    tools=[get_weather]
)