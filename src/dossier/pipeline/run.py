# Pipeline entrypoint: run(topic, audience, depth, rounds, config)

from datetime import datetime
from pathlib import Path
import os

placeholder_brief_content = """
# Dummy Brief

**Topic:** Support Vector Machines  
**Audience:** students  
**Depth:** summary  
**Rounds:** 1  

---

## Summary
- Placeholder bullet 1
- Placeholder bullet 2
- Placeholder bullet 3

## Risks
This is placeholder risk content. In the real pipeline, this section will
highlight 2–3 potential limitations or risks related to the topic.

## Sources
- example.com (stub)
- example.org (stub)

"""

placeholder_result = {
    "title": "A Brief Title",
    "bullets": ["Bullet Point 1", "Bullet Point 2", "Bullet Point 3"],
    "risks": "These are the risks",
    "sources": ["Source 1", "Source 2", "Source 3"],
}

project_root = Path(__file__).resolve().parents[3] / "runs"


def create_timestamp():
    now = datetime.now()
    return f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}_{now.microsecond}"


def create_folder():

    path = Path(project_root) / create_timestamp()
    path.mkdir(parents=True, exist_ok=True)
    return path


def run(topic, audience="general", depth="summary", rounds=1, config=None):
    folder = create_folder()
    filepath = folder.joinpath("brief.md")

    if folder.exists():
        filepath.write_text(placeholder_brief_content)

    print(f"Brief saved to: {filepath.resolve()}")
    return placeholder_result
