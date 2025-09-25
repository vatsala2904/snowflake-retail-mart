import os, snowflake.connector

conn = snowflake.connector.connect(
    user=os.getenv("SF_USER"),
    password=os.getenv("SF_PASS"),
    account=os.getenv("SF_ACCOUNT"),
    warehouse=os.getenv("SF_WH"),
    role=os.getenv("SF_ROLE")
)
cs = conn.cursor()
cs.execute("USE DATABASE RETAIL_DB; USE SCHEMA RAW;")
cs.execute("CREATE OR REPLACE TEMP STAGE TMP;")
cs.execute("PUT file://data/sample/orders.csv @TMP AUTO_COMPRESS=TRUE;")
cs.execute("""
COPY INTO RETAIL_DB.RAW.ORDERS_RAW
FROM @TMP
FILE_FORMAT = (FORMAT_NAME=RETAIL_DB.RAW.CSV_FF)
ON_ERROR='ABORT_STATEMENT';
""")
print("Loaded.")
cs.close(); conn.close()
