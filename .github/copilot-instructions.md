# Project Guidelines

## Code Style
- Use Python 3 syntax.
- Prefer clear, beginner-friendly code and straightforward naming.
- Use consistent function-call formatting like `print("text")` (no space before `(`).

## Architecture
- This project is currently a single script in `main.py`.
- Keep behavior simple and explicit; avoid adding framework structure unless requested.
- If logic grows, prefer extracting functions before introducing classes.

## Build and Test
- Run the script with:
  - `python main.py`
  - `py main.py` (Windows launcher)
- No build step is defined.
- No automated tests are configured yet; verify behavior by running the script.

## Conventions
- Keep output behavior stable unless a task explicitly asks to change it.
- Add an `if __name__ == "__main__":` guard if converting this file into reusable functions.
- Do not add dependency or packaging files unless needed by the task.