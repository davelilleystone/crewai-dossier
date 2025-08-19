## 🎯 Milestone 2 — Skeleton + CLI (stub pipeline)

1. **CLI entrypoint (`cli.py`)**
   - Use `argparse` (or `typer`) to parse:
     - `--topic`
     - `--audience`
     - `--depth`
     - `--rounds`
   - Load `.env` (`load_dotenv()`) so the API key is available.
   - Call a placeholder `dossier.pipeline.run(...)`.
   - Save a dummy output file in `runs/{timestamp}/brief.md`.

2. **Pipeline stub (`pipeline/run.py`)**
   - Define `run(topic, audience, depth, rounds, config)`.
   - For now: just log inputs, create `runs/{timestamp}/`, and write a fake brief.
   - Return a placeholder `FinalBrief` object.

3. **Tools stub**
   - In `tools/impl/search_stub.py`, return a fixed fake search result (so the pipeline can pretend it did work).

4. **Models placeholder**
   - Define minimal `FinalBrief` Pydantic model in `models/`.
   - Just `title: str`, `bullets: list[str]`, `risks: str`, `sources: list[str]`.

5. **Test run**
   - Run:
     ```bash
     python -m src.interfaces.cli.cli --topic "Support Vector Machines" --audience "students"
     ```
   - Check that a folder `runs/{timestamp}/` is created with `brief.md` (dummy content).

6. **Commit**
   - `git add .`
   - `git commit -m "feat: stub CLI + pipeline writing dummy brief"`