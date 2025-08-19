# Research Dossier Builder (v2) — Implementation Blueprint (Point Form)

1) **Project layout**
   - `src/dossier/` → core library (framework-free, reusable by CLI & web)
     - `models/` → Pydantic/dataclasses (Findings, ReviewFeedback, FinalBrief)
     - `agents/` → Researcher, Fact-Checker, Editor (pure logic)
     - `tasks/` → task runner wrappers (orchestration calls agents)
     - `pipeline/` → iterative loop + quality gates
     - `tools/` → search, fetch, cache, rate-limit
       - `ports.py` → abstract interfaces (e.g., `SearchPort`, `Cache`, `Fetcher`)
       - `impl/` → concrete adapters (start stubbed → real web tools later)
     - `quality/` → validators, schema gates, drift guards
     - `prompts/` → deterministic JSON templates
     - `logging/` → structured logging helpers
     - `config/` → config schema + loader (shared by CLI & web)
   - `src/interfaces/`
     - `cli/cli.py` → parses args, calls pipeline, writes to `/runs`
     - `web/` (future) → thin API/UI calling same pipeline
   - `configs/` → YAML/TOML config files (defaults, dev, etc.)
   - `runs/` → artefacts (inputs.json, round files, editor.json, brief.md, sources.json, logs.jsonl, report.md)
   - `tests/` → unit tests for core logic
   - `README.md`
   - `pyproject.toml` (packaging)

2) **CLI and config behaviour**
   - Flags: `--topic`, `--audience`, `--depth`, `--rounds`
   - Config file (e.g., `configs/config.yaml`) for defaults
   - Precedence: CLI > config file > hardcoded defaults
   - Outputs written to `runs/{timestamp}/`
   - Web (later) reuses the same config loader and pipeline

3) **Agents**
   - Researcher → gather initial findings with citations
   - Fact-Checker → verify claims, produce structured `ReviewFeedback`, trigger retries
   - Editor → polish tone/clarity, output `FinalBrief`
   - All agents are framework-free and testable

4) **Structured outputs**
   - `Findings` → claims + evidence + confidence
   - `ReviewFeedback` → pass/fail + issues
   - `FinalBrief` → title, 3 bullets, risks, citations, audience, topic
   - Defined in `src/dossier/models/` (Pydantic/dataclasses)

5) **Prompts**
   - Deterministic, strict JSON outputs
   - Stored in `src/dossier/prompts/`
   - Shared by CLI and web

6) **Tools**
   - Ports/adapters pattern
     - `ports.py` → abstract interfaces (`SearchPort`, `Fetcher`, `Cache`)
     - `impl/` → stub implementations first, then real adapters (retry/backoff)
   - Async-ready (web can use async; CLI can use sync wrappers)

7) **Quality gates**
   - Schema validation (Pydantic)
   - Exactly 3 bullets in summary
   - Risks = 2–3 sentences
   - ≥3 citations from ≥2 domains
   - Deduplicate citations
   - Topic drift guard
   - Audience fit check

8) **Iterative loop**
   - Researcher → validate → Fact-Checker
   - If fail → revise & retry
   - If pass → Editor
   - Editor → final gates
   - All steps logged (structured JSON)

9) **Observability**
   - Structured JSON logs
   - Artefacts saved under `runs/{timestamp}/`
   - Logs capture feedback, pass/fail status, errors

10) **Reproducibility**
    - Deterministic prompts
    - Logged seeds, versions, and configuration
    - Artefact folders contain everything needed to re-run

11) **Acceptance criteria**
    - Running CLI produces `brief.md` with:
      - Title
      - 3 bullets
      - Risks (2–3 sentences)
      - ≥3 citations from ≥2 domains
    - Logs show feedback and pass/fail state
    - Web (later) serves the same artefacts via API/UI

12) **Commit milestones**
    - Skeleton + CLI (folders, stub pipeline, empty agents)
    - Generic agents (stubs with fixed outputs)
    - Pydantic schemas (models wired)
    - Web search tool (stub first, real later)
    - Fact-Checker + iterative loop
    - Editor + final brief
    - README
    - Logging refactor
    - Web interface (future milestone)

13) **Brief.md spec**
    - Title
    - Summary (3 bullets)
    - Risks (2–3 sentences)
    - Sources

14) **Nice-to-haves**
    - Domain scoring
    - Freshness guard
    - Query planning
    - Semantic dedupe
    - Async tool adapters (for web)

15) **Pitfalls to avoid**
    - Narrative output instead of JSON
    - Prose feedback instead of structured `ReviewFeedback`
    - Topic drift
    - Citation mismatches
    - Coupling core logic to CLI/web framework