release: cd backend && alembic upgrade head
web: uvicorn app.main:app --host 0.0.0.0 --port 8000 --app-dir backend
