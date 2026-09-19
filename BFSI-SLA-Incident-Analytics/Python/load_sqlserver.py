import os
import pandas as pd
from sqlalchemy import create_engine
import urllib

# ===================================================
# SQL SERVER CONFIGURATION
# ===================================================

SERVER = "YOUR_SQL_SERVER\\SQLEXPRESS"

DATABASE = "BFSI_SLA_Analytics"

RAW_DATA = r"path/to/Raw_data"

# ===================================================
# SQL CONNECTION
# ===================================================

params = urllib.parse.quote_plus(

    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)

engine = create_engine(

    f"mssql+pyodbc:///?odbc_connect={params}"

)

print("="*60)
print("CONNECTED TO SQL SERVER")
print("="*60)

# ===================================================
# FILE LIST
# ===================================================

files = [

("Dim_Client.csv","dim","Dim_Client"),

("Dim_Project.csv","dim","Dim_Project"),

("Dim_Application.csv","dim","Dim_Application"),

("Dim_Team.csv","dim","Dim_Team"),

("Dim_User.csv","dim","Dim_User"),

("Dim_Priority.csv","dim","Dim_Priority"),

("Dim_Status.csv","dim","Dim_Status"),

("Dim_RootCause.csv","dim","Dim_RootCause"),

("Dim_RejectionReason.csv","dim","Dim_RejectionReason"),

("Dim_Release.csv","dim","Dim_Release"),

("Dim_SLA_Policy.csv","dim","Dim_SLA_Policy"),

("Dim_Date.csv","dim","Dim_Date"),

("Fact_Incident.csv","fact","Fact_Incident")

]

# ===================================================
# LOAD DATA
# ===================================================

for file,schema,table in files:

    path=os.path.join(RAW_DATA,file)

    print(f"Loading {file}")

    df=pd.read_csv(path)

    df.to_sql(

        table,

        engine,

        schema=schema,

        if_exists="append",

        index=False,

        chunksize=5000

    )

    print(f"{table} Loaded")

print()

print("="*60)

print("ALL FILES LOADED SUCCESSFULLY")

print("="*60)
