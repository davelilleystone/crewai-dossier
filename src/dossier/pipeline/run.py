# Pipeline entrypoint: run(topic, audience, depth, rounds, config)


def run(topic, audience="general", depth="summary", rounds=1, config=None):
    print("Pipeline run called...")
    print("Arg values:")
    arg_values = f"""
    Topic: {topic}
    Audience: {audience}
    Depth: {depth}
    Rounds: {rounds}
    Config: {config}
    """
    print(arg_values)
