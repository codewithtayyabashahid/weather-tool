def detect_language(text: str) -> str:
    urdu_chars = [c for c in text if '\u0600' <= c <= '\u06FF']
    return "urdu" if len(urdu_chars) > 3 else "english"

def route_query(query: str):
    from agents.urdu_agent import urdu_agent
    from agents.english_agent import english_agent
    lang = detect_language(query)
    if lang == "urdu":
        return urdu_agent.run(query)
    return english_agent.run(query)