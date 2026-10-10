# CrewAI Job Posting example (local-first adaptation)

This is a small, runnable adaptation inspired by CrewAI's archived `crews/job-posting` example. It keeps the key learning concepts—three Agents, five Tasks, YAML configuration, sequential execution, and Pydantic structured outputs—while avoiding a separate Serper/web-search API key. It does **not** scrape or browse the company website; research is based on the inputs supplied by `main.py`.

## Files

- `main.py` — inputs, kickoff, and saving the final output.
- `job_posting_crew/crew.py` — Agent/Task/Crew wiring and Pydantic output models.
- `config/agents.yaml` — Agent roles, goals, and backstories.
- `config/tasks.yaml` — five task definitions.
- `output/job_posting.md` — generated output (created at runtime).

## Run inside the existing project

Expected parent project layout:

```text
crewai-learning/
  .env
  .venv/
  main.py                  # your existing lesson; leave it unchanged
  job-posting/
    main.py
    job_posting_crew/
    config/
    output/
```

Use the existing virtual environment and installed dependencies. From PowerShell:

```powershell
cd F:\ProgramingProjects\crewai-learning
.\.venv\Scripts\Activate.ps1
python .\job-posting\main.py
```

The existing `.env` should provide the same variables used in your current project, for example `MODEL_NAME`, `OPENAI_BASE_URL`, and `OPENAI_API_KEY`. Keep the API key private. No Serper key is required for this local-first version.

If CrewAI reports that `PyYAML` is missing, install it in the existing environment:

```powershell
python -m pip install pyyaml
```

## Customize the sample

Edit the `inputs` dictionary in `main.py` to change the company, role, hiring needs, and benefits. Run again; the final result is printed and saved to `output/job_posting.md`.

## Important notes

- This project uses sequential execution, so tasks run in order and later tasks can use earlier task outputs as context.
- `output_pydantic` is used on the two research tasks to request structured output.
- The industry analysis task runs after the review task, so it is a separate advisory note and is not incorporated into the final posting. Move it earlier if you want the writer/editor to use that context.
- The model output should be reviewed by a human before publication.
