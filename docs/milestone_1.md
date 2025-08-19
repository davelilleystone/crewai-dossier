## 🎯 Milestone 1 — Project skeleton (boilerplate)

1. **Project setup**
   - Created folder structure (`src/dossier/`, `src/interfaces/cli/`, `configs/`, `runs/`, etc.)
   - Added placeholder files for agents, tasks, pipeline, tools, prompts, logging, config.

2. **Configuration**
   - Added `pyproject.toml` with `[project]`, `[tool.setuptools]`, and `[build-system]`.
   - Added `config.yaml` for topic, audience, depth, rounds, output path, logging.
   - Added `.gitignore` to ignore `.env`, `runs/`, venvs, and IDE files.
   - Added `.env.example` with placeholder `OPENAI_API_KEY`.

3. **Environment**
   - Initialized uv project with `uv init --bare`.
   - Verified `.venv/` created and set as Python interpreter in VS Code.
   - Installed `crewai` using `uv add crewai`.
   - Installed `python-dotenv` for environment variable loading.

4. **Version control**
   - Initialized git repo with `git init`.
   - Staged and committed skeleton with `git commit -m "chore: project skeleton with uv, config, and CrewAI dependency"`.
   - Ensured `.env` is ignored and tracked `.env.example` instead.