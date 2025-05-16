import os
import json
from openai import OpenAI


_llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def decide(cmd: dict) -> dict:
    """
    build prompt specifying our available tools
    send it to the LLM and parse back a JSON response
    """

    prompt = f"""
    You are a To-Do List Agent. The usage says \"{cmd['raw']}\".
    Choose exactly one tool from: add_task list_tasks, remove_tasks
    Return a JSON object with keys:
    - tool: name of the tool
    - args: dictioanry of arguments for that tool
    Example: {{"tool": "add_task", "args": {{"description": "Buy milk"}} }}
    """

    response = _llm.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    decision = json.loads(response.choices[0].message.content)
    return decision
