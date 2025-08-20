import os, sys


def check_api_key(api_key):
    key = os.getenv(api_key)
    if key:
        print(f"{api_key} loaded, starts with {key[:10]}")
    else:
        print(f"{api_key} not loaded, exiting script...")
        sys.exit(1)
