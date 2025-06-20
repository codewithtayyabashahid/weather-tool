import random

def get_weather(city: str) -> str:
    """Returns a random weather condition for a given city."""
    conditions = ["sunny", "cold", "windy", "rainy", "cloudy"]
    return f"The weather in {city} is {random.choice(conditions)}."