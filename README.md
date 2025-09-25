# Snowflake Retail Mart
Goal: tiny retail star schema with staging, mart, and QA checks.

## Run

### 1) Create objects in Snowflake
Run SQL files in order inside the Snowflake UI (Worksheets):
- `sql/00_schema.sql`
- `sql/10_staging.sql`
- `sql/20_mart.sql`

### 2) Load sample data locally
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
cp .env.example .env   # Windows: copy .env.example .env
# fill SF_* values in .env, then run:
python loader/load_csv.py


## Notes
- Uses Tasks/Streams in next release.
