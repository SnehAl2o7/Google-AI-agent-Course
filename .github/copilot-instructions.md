## Purpose
Help an AI coding agent get productive quickly in this repository: a small course repository centered around a single Jupyter notebook.

### Repo snapshot (what I discovered)
- Top-level files: `Day-1a.ipynb`, `README.md`, `LICENSE`.
- No dependency manifest (no `requirements.txt`, `pyproject.toml`, or `environment.yml`).

## What the agent should know first
- This repository is a teaching/course repo. The primary artifact is `Day-1a.ipynb` (Jupyter notebook).
- There is no build or test system present. Treat changes conservatively.

## When editing or contributing
- Prefer non-destructive edits to the notebook. If adding an exercise or longer example, create a new notebook (e.g. `Day-1b.ipynb`) rather than overwriting outputs in `Day-1a.ipynb`.
- If you must add code files (Python modules or scripts), also add a dependency manifest (`requirements.txt` or `pyproject.toml`) documenting any new packages.

## Environment & run hints (explicit, minimal commands)
- To run interactively: open `Day-1a.ipynb` in VS Code (Jupyter extension) or run `jupyter lab` / `jupyter notebook` in a Python environment with Jupyter installed.
- Quick execution from CLI (non-default; useful for CI or validation):
  - Ensure a Python env with `jupyter` and required packages, then
    `jupyter nbconvert --execute Day-1a.ipynb --to notebook --output executed.ipynb`

## Patterns & conventions observed
- Single-notebook course: there are no packages, modules, tests, or CI configured. Assume the repository is intended for reading/running notebooks and lightweight edits.
- Keep repository history readable: prefer adding new notebooks or small text edits instead of large binary diff churn from re-running/clearing outputs.

## What the agent should NOT assume
- Do not assume any specific dependencies or versions — none are declared.
- Do not add broad refactors across the repo without asking the human maintainer: this is a small learning repo and changes should be coordinated.

## Recommended next steps for contributors (if asked to extend)
1. Add a `requirements.txt` listing minimal dependencies used by new code/notebooks.
2. Add a short `CONTRIBUTING.md` or update `README.md` describing how to run notebooks and the desired notebook-editing policy (preserve original, create `Day-1b.ipynb`, etc.).

## Where to look for examples
- `Day-1a.ipynb` — the canonical place to inspect course content and code examples.
- `README.md` — very short project description.

If anything here is unclear or you'd like me to expand any section (examples for adding a `requirements.txt`, a one-file test harness, or a small CI step to execute notebooks), tell me which part to expand.
