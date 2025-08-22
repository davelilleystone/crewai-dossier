from datetime import datetime, timezone


def create_timestamp():
    now = datetime.now()
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%fZ")
