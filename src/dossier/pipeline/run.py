# Pipeline entrypoint: run(topic, audience, depth, rounds, config)

from datetime import datetime
from pathlib import Path
import os

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
    print(dir(folder))


run("testing")
