### Assignment 01: Simple Agents Workflow with OpenAI Agents SDK, Chainlit, and LiteLLM (Gemini)

import chainlit as cl
from agents.triagent import route_query

@cl.on_message
def main(message: cl.Message):
    user_input = message.content
    response = route_query(user_input)
    cl.Message(content=response).send()