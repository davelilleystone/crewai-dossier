# Design Note: Separation of Pipeline, Renderer, and Interface

## Current Question
Should the pipeline `run()` function be responsible for creating folders and writing files, or should it only return structured data?

## Recommended Approach
**`run()` should be pure.**  
It should take inputs, execute the workflow, and return structured data (a `FinalBrief`) plus lightweight metadata (e.g., a `run_id`).  
It should **not** create folders or write files.

## Why This Matters
- **Separation of concerns**: logic vs. presentation vs. I/O are cleanly separated.
- **Testability**: unit tests can run the pipeline without touching the filesystem.
- **Extensibility**: same pipeline supports CLI, web app, or batch jobs; only the renderer changes.
- **Determinism**: fewer side effects inside core logic.

## Minimal Refactor Plan
1. **Pipeline (`run()`)**
   - Inputs: `topic, audience, depth, rounds, config`.
   - Output: `FinalBrief` (structured) + `run_id` (timestamp string for traceability).
   - No file creation, no markdown rendering.

2. **Renderer Layer**
   - `to_markdown(final_brief)`: returns a markdown string.
   - Future extensions: `to_json(final_brief)`, `to_html(final_brief)`, `to_pdf(final_brief)`.

3. **Writer Layer**
   - `ensure_output_dir(base="runs", run_id)`: returns the correct path (created if missing).
   - `write_text(path, filename, content)`: saves rendered content to file.

4. **Interface Layer (CLI, web, etc.)**
   - Collects user input.
   - Calls `run()` → gets `FinalBrief` + `run_id`.
   - Selects a renderer (default: markdown).
   - Uses writer to create `/runs/{run_id}/brief.md`.
   - Prints/logs the saved path.

## Near-Term MVP Adjustments
- Move folder creation and `brief.md` writing out of `run()` into the CLI.
- Add a simple renderer function for markdown (returning a string).
- Keep the timestamp helper but have the CLI own it (or return `run_id` from `run()`).
- Continue returning a dict for now; later replace with Pydantic `FinalBrief`.