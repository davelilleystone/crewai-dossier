crewai-dossier/
├─ README.md                               # project overview & quickstart
├─ pyproject.toml                          # packaging (fill later)
├─ configs/
│  ├─ config.yaml                          # defaults (topic/audience/depth/rounds, logging)
│  └─ dev.yaml                             # local overrides
├─ runs/                                   # artifacts per run (briefs, logs, sources, etc.)
│  └─ .gitkeep
├─ tests/
│  └─ test_placeholder.md                  # replace with real tests later
└─ src/
   ├─ dossier/                             # CORE library (framework-free)
   │  ├─ __init__.py                       # empty init
   │  ├─ models/
   │  │  ├─ __init__.py
   │  │  └─ README.md                      # list the core data models to add
   │  ├─ agents/
   │  │  ├─ __init__.py
   │  │  ├─ researcher.py                  # stub agent class/function
   │  │  ├─ fact_checker.py                # stub agent class/function
   │  │  └─ editor.py                      # stub agent class/function
   │  ├─ tasks/
   │  │  ├─ __init__.py
   │  │  └─ task_runner.py                 # orchestrates calls to agents
   │  ├─ pipeline/
   │  │  ├─ __init__.py
   │  │  └─ run.py                         # entry function for the pipeline
   │  ├─ tools/
   │  │  ├─ __init__.py
   │  │  ├─ ports.py                       # abstract interfaces (SearchPort, Fetcher, Cache)
   │  │  └─ impl/
   │  │     ├─ __init__.py
   │  │     ├─ search_stub.py              # returns fixed results for E2E smoke test
   │  │     ├─ fetch_stub.py               # no-op or file-backed fetch
   │  │     └─ cache_file.py               # simple file cache adapter
   │  ├─ quality/
   │  │  ├─ __init__.py
   │  │  └─ gates.py                       # validators: bullets=3, risks length, citations>=3/2 domains
   │  ├─ prompts/
   │  │  ├─ __init__.py
   │  │  ├─ researcher_prompt.md           # strict-JSON template (content to add later)
   │  │  ├─ fact_checker_prompt.md         # strict-JSON template
   │  │  └─ editor_prompt.md               # strict-JSON template
   │  ├─ logging/
   │  │  ├─ __init__.py
   │  │  └─ json_logger.py                 # helper for structured logs
   │  └─ config/
   │     ├─ __init__.py
   │     └─ loader.py                      # precedence: CLI > config file > defaults
   └─ interfaces/
      ├─ __init__.py
      ├─ cli/
      │  ├─ __init__.py
      │  └─ cli.py                         # parses args; calls pipeline.run; writes to /runs
      └─ web/                              # (future) FastAPI/Flask
         ├─ __init__.py
         ├─ api/
         │  ├─ __init__.py
         │  └─ routes_placeholder.md       # note what endpoints you'll add later
         └─ app.py                         # thin web entry calling the same pipeline

