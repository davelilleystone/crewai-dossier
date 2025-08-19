# CLI entry: parse flags, call dossier.pipeline.run, write to /runs
import argparse
from inspect import signature, _empty
from dossier.pipeline import run

sig = signature(run)

defaults = {
    name: (param.default if param.default is not _empty else None)
    for name, param in sig.parameters.items()
}

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--topic", required=True, help="Topic to research (required)")
parser.add_argument(
    "-a",
    "--audience",
    default=defaults.get("audience"),
    help=f"Target audience (default: {defaults.get('audience')})",
)
parser.add_argument(
    "-d",
    "--depth",
    default=defaults.get("depth"),
    help=f"Depth level (default: {defaults.get('depth')})",
)
parser.add_argument(
    "-r",
    "--rounds",
    type=int,
    default=defaults.get("rounds"),
    help=f"Number of rounds (default: {defaults.get('rounds')})",
)

args = parser.parse_args()

# Pass args explicitly as keywords
run(
    topic=args.topic,
    audience=args.audience,
    depth=args.depth,
    rounds=args.rounds,
    config=None,
)
