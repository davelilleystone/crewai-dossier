# creates folder in the root/runs folder

from pathlib import Path
from utils import create_timestamp

project_root = Path(__file__).resolve().parents[2] / "runs"


def create_folder():
    path = Path(project_root) / create_timestamp()
    path.mkdir(parents=True, exist_ok=True)
    return path
