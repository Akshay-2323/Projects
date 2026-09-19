import pandas as pd

files = [
    "Dim_Client.csv",
    "Dim_Project.csv",
    "Dim_Application.csv",
    "Dim_Team.csv",
    "Dim_User.csv",
    "Dim_Priority.csv",
    "Dim_Status.csv",
    "Dim_RootCause.csv",
    "Dim_RejectionReason.csv",
    "Dim_Release.csv",
    "Dim_SLA_Policy.csv",
    "Dim_Date.csv",
    "Fact_Incident.csv"
]

base = r"E:\Akshay Projects\Job Project\Project 1\Raw_data"

for f in files:
    df = pd.read_csv(fr"{base}\{f}", nrows=1)
    print("\n", "="*60)
    print(f)
    print(list(df.columns))