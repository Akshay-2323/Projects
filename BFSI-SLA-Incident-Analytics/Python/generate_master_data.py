
import os
import random
from datetime import datetime
import pandas as pd
from faker import Faker

fake = Faker("en_IN")
random.seed(42)

RAW_DATA_PATH = r"E:\Akshay Projects\Job Project\Project 1\Raw_data"
os.makedirs(RAW_DATA_PATH, exist_ok=True)

NUM_CLIENTS = 10
NUM_PROJECTS = 20
NUM_APPLICATIONS = 50
NUM_TEAMS = 8
NUM_USERS = 250
NUM_RELEASES = 40

# ---------------- Clients ----------------
clients = []
client_names = [
    "Apex Bank","Zenith Finance","SecureLife Insurance","Nova Payments",
    "Capital Trust Bank","Horizon Lending","Unity Mutual",
    "Mercury Digital Bank","Pinnacle Finance","Infinity Banking Group"
]
industries = ["Banking","Finance","Insurance","Payments"]
regions = ["North","South","East","West"]
support_models = ["24x7","16x5"]

for i in range(NUM_CLIENTS):
    clients.append({
        "Client_ID":f"CLI{i+1:03}",
        "Client_Name":client_names[i],
        "Industry":random.choice(industries),
        "Country":"India",
        "Region":random.choice(regions),
        "Support_Model":random.choice(support_models),
        "Contract_Start_Date":fake.date_between("-5y","-2y"),
        "Contract_End_Date":fake.date_between("+1y","+4y"),
        "Is_Active":1
    })

df_clients=pd.DataFrame(clients)
df_clients.to_csv(os.path.join(RAW_DATA_PATH,"Dim_Client.csv"),index=False)

# ---------------- Projects ----------------

projects = []

business_units = [
    "Retail Banking",
    "Cards",
    "Lending",
    "Payments",
    "Insurance"
]

project_counter = 1

for client_id in df_clients["Client_ID"]:

    # Every client gets exactly 2 projects
    for _ in range(2):

        projects.append({

            "Project_ID": f"PRJ{project_counter:03}",

            "Client_ID": client_id,

            "Project_Name": f"{random.choice(business_units)} Project {project_counter}",

            "Business_Unit": random.choice(business_units),

            "Project_Manager": fake.name(),

            "Go_Live_Date": fake.date_between("-3y", "-1y"),

            "Support_Start_Date": fake.date_between("-2y", "today"),

            "Project_Status": "Active"

        })

        project_counter += 1

df_projects = pd.DataFrame(projects)

df_projects.to_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Project.csv"),
    index=False
)

# ---------------- Applications ----------------

apps = []

techs = [
    "Java",
    ".NET",
    "Python",
    "Angular",
    "React",
    "Spring Boot"
]

criticality = [
    "Critical",
    "High",
    "Medium",
    "Low"
]

application_counter = 1

for project_id in df_projects["Project_ID"]:

    # Every project will have 2-4 applications
    number_of_apps = random.randint(2, 4)

    for _ in range(number_of_apps):

        apps.append({

            "Application_ID": f"APP{application_counter:03}",

            "Project_ID": project_id,

            "Application_Name": f"Application {application_counter}",

            "Module_Name": f"Module {random.randint(1,8)}",

            "Technology": random.choice(techs),

            "Criticality": random.choice(criticality),

            "Is_Production": 1

        })

        application_counter += 1

df_applications = pd.DataFrame(apps)

df_applications.to_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Application.csv"),
    index=False
)


# ---------------- Teams ----------------
teams=[
("TM001","L1 Support"),("TM002","L2 Support"),("TM003","L3 Support"),
("TM004","Infrastructure"),("TM005","DBA"),("TM006","DevOps"),
("TM007","QA"),("TM008","Product")
]
team_rows=[]
for t in teams:
    team_rows.append({
        "Team_ID":t[0],
        "Team_Name":t[1],
        "Department":"Technology",
        "Team_Manager":fake.name(),
        "Shift":"24x7" if "Support" in t[1] else "General"
    })
df_team=pd.DataFrame(team_rows)
df_team.to_csv(os.path.join(RAW_DATA_PATH,"Dim_Team.csv"),index=False)

# ---------------- Users ----------------
users=[]
designations=["Support Engineer","Senior Engineer","Lead","Analyst"]
for i in range(NUM_USERS):
    tm=random.choice(df_team.Team_ID.tolist())
    users.append({
        "User_ID":f"USR{i+1:04}",
        "Team_ID":tm,
        "Employee_Name":fake.name(),
        "Designation":random.choice(designations),
        "Experience_Years":round(random.uniform(1,12),1),
        "Email":fake.email(),
        "Location":random.choice(["Noida","Pune","Hyderabad","Bangalore","Chennai"]),
        "Shift":random.choice(["Morning","Evening","Night"]),
        "Is_Active":1
    })
pd.DataFrame(users).to_csv(os.path.join(RAW_DATA_PATH,"Dim_User.csv"),index=False)

# Priority
priority=pd.DataFrame([
["P1","Critical",15,4,0],
["P2","High",30,8,0],
["P3","Medium",120,24,1],
["P4","Low",240,48,1]
],columns=["Priority_Code","Priority_Name","Response_SLA_Minutes","Resolution_SLA_Hours","Business_Hours_Only"])
priority.to_csv(os.path.join(RAW_DATA_PATH,"Dim_Priority.csv"),index=False)

# Status
statuses=["New","Assigned","Acknowledged","In Progress","Awaiting Client","Awaiting Infrastructure","Awaiting Vendor","Awaiting Deployment","Resolved","Validation","Closed","Reopened","Rejected"]
pd.DataFrame({"Status_Name":statuses}).to_csv(os.path.join(RAW_DATA_PATH,"Dim_Status.csv"),index=False)

# RCA
rca=["Application Bug","Database","Infrastructure","Network","Deployment Failure","Configuration","Security","Third Party","Data Issue","User Error"]
pd.DataFrame({"RCA_Category":rca}).to_csv(os.path.join(RAW_DATA_PATH,"Dim_RootCause.csv"),index=False)

# Rejection
rej=["Missing Information","Duplicate","Wrong Application","Wrong Team","Outside Scope","Already Resolved","Test Ticket","User Error","Invalid Details"]
pd.DataFrame({"Rejection_Reason":rej}).to_csv(os.path.join(RAW_DATA_PATH,"Dim_RejectionReason.csv"),index=False)

# Release
rels=[]
for i in range(NUM_RELEASES):
    rels.append({
        "Release_ID":f"REL{i+1:03}",
        "Release_Version":f"v{random.randint(1,5)}.{random.randint(0,9)}",
        "Release_Type":random.choice(["Major","Minor","Patch"]),
        "Deployment_Date":fake.date_between("-2y","today"),
        "Rollback_Flag":random.randint(0,1),
        "Deployment_Status":"Success"
    })
pd.DataFrame(rels).to_csv(os.path.join(RAW_DATA_PATH,"Dim_Release.csv"),index=False)

# SLA
sla=pd.DataFrame([
["SLA001","P1",15,4,0],
["SLA002","P2",30,8,0],
["SLA003","P3",120,24,1],
["SLA004","P4",240,48,1]
],columns=["SLA_ID","Priority_Code","Response_SLA_Minutes","Resolution_SLA_Hours","Business_Hours_Only"])
sla["Effective_From"]="2024-01-01"
sla["Effective_To"]="2030-12-31"
sla.to_csv(os.path.join(RAW_DATA_PATH,"Dim_SLA_Policy.csv"),index=False)

# Date
dates=pd.date_range("2024-01-01","2025-12-31")
rows=[]
for d in dates:
    fy=f"{d.year}-{str(d.year+1)[2:]}" if d.month>=4 else f"{d.year-1}-{str(d.year)[2:]}"
    rows.append({
        "Date_Key":int(d.strftime("%Y%m%d")),
        "Full_Date":d.date(),
        "Day_Number":d.day,
        "Day_Name":d.day_name(),
        "Week_Number":int(d.strftime("%U")),
        "Month_Number":d.month,
        "Month_Name":d.strftime("%B"),
        "Quarter_Number":(d.month-1)//3+1,
        "Year_Number":d.year,
        "Financial_Year":fy,
        "Is_Weekend":1 if d.weekday()>=5 else 0,
        "Is_Holiday":0
    })
pd.DataFrame(rows).to_csv(os.path.join(RAW_DATA_PATH,"Dim_Date.csv"),index=False)

print("All Dimension CSV files generated successfully.")
