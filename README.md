# GHCI Python Starter (FastAPI + pytest)

This is a tiny sample repo for **Session 1: AI‑Assisted GitHub & CI**.

## What’s here
- `app/main.py`: a minimal FastAPI app with a `/health` endpoint
- `tests/test_health.py`: a basic test that asserts `/health` returns `{"status":"ok", ...}`
- `.github/workflows/ci.yml`: GitHub Actions to run tests on **push** and **pull_request**
- `.github/pull_request_template.md`: a simple template for quality PRs

## Run locally (optional)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# in another terminal
pytest -q
```

## Micro‑exercise A (Green PR in ~7 minutes)
1. Edit `README.md` → add one helpful line under “Run locally”.
2. In the commit box, select **Create a new branch** named `docs/add-test-instructions`.
3. **Propose changes → Create pull request**.
4. Wait for ✅ CI checks, then paste an AI‑drafted PR description (What/Why/How/Tests) and submit.

## Micro‑exercise B (Explain a failing run)
Use the **instructor‑seeded failing PR** (separate repo or branch). Open the failing check, copy the error snippet, ask AI to explain it simply, and post a comment with root cause + smallest fix.

## Notes
- Keep PRs **small** and **focused**.
- Use AI for drafting and explanations, but **you** verify commands and code.
