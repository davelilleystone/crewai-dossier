# Milestone 2 – Pipeline Stub (Dummy Brief)

### Goal
Finish the pipeline stub so that each run creates a timestamped folder under `runs/` and writes a dummy `brief.md`. It should also return a structured object (a plain dict for now), which will later be replaced by a Pydantic `FinalBrief` model.

---

### Step-by-step plan

1. **Decide `run()` defaults (for CLI help text to show sane defaults)**
   - `audience`: `"general"`
   - `depth`: `"basic"`
   - `rounds`: `1`
   - `config`: `None`

2. **Create a timestamped output folder**
   - Use local time (e.g., Europe/London) to build a string like `YYYY-MM-DD_HH-MM-SS`.
   - Output directory: `runs/<that-timestamp>/`.
   - Ensure parent folders are created if they don’t exist.

3. **Prepare dummy brief content**
   - **Title**: `"Dummy Brief"`
   - Echo the inputs (`topic`, `audience`, `depth`, `rounds`).
   - Add three placeholder bullets (e.g., `"Placeholder bullet 1"`, `"Placeholder bullet 2"`, `"Placeholder bullet 3"`).
   - Add a short **Risks** paragraph (one or two sentences, placeholder).
   - Add a small **Sources** list with obvious fake entries (e.g., `"example.com (stub)"`).

   The structure should mimic the eventual real brief so later renders can simply swap in actual content.

4. **Write `brief.md`**
   - File path: `runs/<timestamp>/brief.md`.
   - Write the dummy content (UTF-8).
   - Optionally print/log the full file path so the CLI shows where the artifact landed.

5. **Return a placeholder result to the caller**
   - For now, return a plain Python dict with keys:
     - `title` (string)
     - `bullets` (list of three strings)
     - `risks` (string)
     - `sources` (list of strings)

   This dict will later be swapped out for a proper Pydantic `FinalBrief` model. Keeping the shape consistent now makes that transition trivial.

6. **Wire-up import paths if needed**
   - Ensure the `pipeline` package exposes `run` so that `from dossier.pipeline import run` continues to work.

7. **Test**
   - Run the CLI with a topic and audience.
   - Confirm a new folder appears under `runs/` with the current timestamp.
   - Confirm `brief.md` exists and has the dummy structure.

8. **Commit**
   - Stage and commit with a message such as:
     ```
     feat: pipeline stub writes timestamped dummy brief to /runs
     ```

---

### Why this order?
- Produces a full end-to-end artifact early.
- Next, the **models placeholder (Pydantic)** can replace the returned dict with a `FinalBrief` instance.
- After that, the **tools stub** can be added to generate fixed fake search results without changing any plumbing.