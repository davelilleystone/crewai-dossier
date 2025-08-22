# Pipeline entrypoint: run(topic, audience, depth, rounds, config)

from utils import create_timestamp
from copy import deepcopy

placeholder_result = {
    "title": "A Brief Title",
    "topic": "placeholder topic",
    "audience": "general",
    "bullets": ["Bullet Point 1", "Bullet Point 2", "Bullet Point 3"],
    "risks": "These are the risks. Second sentence for length.",
    "citations": [
        {"title": "Source 1", "url": "https://one.com", "domain": "one.com"},
        {"title": "Source 2", "url": "https://two.com", "domain": "two.com"},
        {"title": "Source 3", "url": "https://three.com", "domain": "three.com"},
    ],
}


def run(topic, audience="general", depth="summary", rounds=1, config=None):
    return {"run_id": create_timestamp(), "final_brief": deepcopy(placeholder_result)}


print(run("test"))
