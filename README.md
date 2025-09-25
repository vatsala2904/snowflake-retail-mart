# Snowflake Retail Mart
Goal: tiny retail star schema with staging, mart, and QA checks.

## Run
1) Create DB objects: run files in `/sql` in order.
2) Load data: python loader/load_csv.py
3) Verify: run QA queries in `20_mart.sql` bottom section.

## Notes
- Uses Tasks/Streams in next release.
