# Portfolio API

The FastAPI service provides the portfolio health check and contact-message endpoint.

## Run locally

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Set `ALLOWED_ORIGINS` in `.env` to a comma-separated list of frontend origins when the UI is not running on the default Vite port.
