# ============================================================
# File Name : generate_incidents.py
# Project   : BFSI SLA & Incident Management Dashboard
# Author    : Akshay Sharma
# ============================================================

import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# ============================================================
# Configuration
# ============================================================

RAW_DATA_PATH = r"E:\Akshay Projects\Job Project\Project 1\Raw_data"

OUTPUT_FILE = os.path.join(
    RAW_DATA_PATH,
    "Fact_Incident.csv"
)

TOTAL_INCIDENTS = 150000

random.seed(42)
np.random.seed(42)

# ============================================================
# Load Master Data
# ============================================================

print("=" * 60)
print("Loading Master Data...")
print("=" * 60)

clients = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Client.csv")
)

projects = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Project.csv")
)

applications = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Application.csv")
)

teams = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Team.csv")
)

users = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_User.csv")
)

priority = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Priority.csv")
)

status = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Status.csv")
)

rootcause = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_RootCause.csv")
)

rejection = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_RejectionReason.csv")
)

release = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Release.csv")
)

sla = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_SLA_Policy.csv")
)

dates = pd.read_csv(
    os.path.join(RAW_DATA_PATH, "Dim_Date.csv")
)

print("Master Data Loaded Successfully")
print()

# ============================================================
# Priority Distribution
# ============================================================

priority_distribution = {

    "P1": 2,

    "P2": 8,

    "P3": 35,

    "P4": 55

}

# ============================================================
# Status Distribution
# ============================================================

status_distribution = {

    "Closed": 70,

    "Resolved": 10,

    "In Progress": 8,

    "Awaiting Client": 4,

    "Assigned": 2,

    "Reopened": 2,

    "Rejected": 4

}

# ============================================================
# Helper Functions
# ============================================================

def random_priority():

    return random.choices(

        population=list(priority_distribution.keys()),

        weights=list(priority_distribution.values()),

        k=1

    )[0]


def random_status():

    return random.choices(

        population=list(status_distribution.keys()),

        weights=list(status_distribution.values()),

        k=1

    )[0]


def random_created_date():

    row = dates.sample(1).iloc[0]

    return pd.to_datetime(row["Full_Date"])


def generate_ticket_number(number):

    return f"INC{number:07}"


print("Initialization Completed")
print("=" * 60)
print()

# ============================================================
# Incident Generation Engine
# ============================================================

print("Generating Incident Records...")
print()

incidents = []

for i in range(1, TOTAL_INCIDENTS + 1):

    # --------------------------------------------------------
    # Ticket Number
    # --------------------------------------------------------

    ticket_id = generate_ticket_number(i)

    # --------------------------------------------------------
    # Select Client
    # --------------------------------------------------------

    client = clients.sample(1).iloc[0]

    # --------------------------------------------------------
    # Select Project of that Client
    # --------------------------------------------------------

    client_projects = projects[
        projects["Client_ID"] == client["Client_ID"]
    ]

    project = client_projects.sample(1).iloc[0]

    # --------------------------------------------------------
    # Select Application of that Project
    # --------------------------------------------------------

    project_apps = applications[
        applications["Project_ID"] == project["Project_ID"]
    ]

    application = project_apps.sample(1).iloc[0]

    # --------------------------------------------------------
    # Engineer
    # --------------------------------------------------------

    engineer = users.sample(1).iloc[0]

    # --------------------------------------------------------
    # Team
    # --------------------------------------------------------

    team = teams[
        teams["Team_ID"] == engineer["Team_ID"]
    ].iloc[0]

    # --------------------------------------------------------
    # Priority
    # --------------------------------------------------------

    priority_code = random_priority()

    priority_row = priority[
        priority["Priority_Code"] == priority_code
    ].iloc[0]

    # --------------------------------------------------------
    # Status
    # --------------------------------------------------------

    status_name = random_status()

    status_row = status[
        status["Status_Name"] == status_name
    ].iloc[0]

    # --------------------------------------------------------
    # Created Date
    # --------------------------------------------------------

    created_date = random_created_date()

    # --------------------------------------------------------
    # Store Record
    # --------------------------------------------------------

    incidents.append({

        "Ticket_ID": ticket_id,

        "Client_ID": client["Client_ID"],

        "Project_ID": project["Project_ID"],

        "Application_ID": application["Application_ID"],

        "Team_ID": team["Team_ID"],

        "User_ID": engineer["User_ID"],

        "Priority_Code": priority_code,

        "Status_Name": status_name,

        "Created_Date": created_date

    })

    # --------------------------------------------------------
    # Progress Bar
    # --------------------------------------------------------

    if i % 10000 == 0:

        print(f"{i:,} incidents generated...")

print()
print("Incident Generation Completed")
print()

# ============================================================
# Business Logic
# ============================================================

print("Applying Business Rules...")
print()

incident_df = pd.DataFrame(incidents)

# ============================================================
# Response Time
# ============================================================

response_time = []

for priority in incident_df["Priority_Code"]:

    if priority == "P1":
        response_time.append(random.randint(1,15))

    elif priority == "P2":
        response_time.append(random.randint(5,30))

    elif priority == "P3":
        response_time.append(random.randint(20,120))

    else:
        response_time.append(random.randint(30,240))

incident_df["Response_Time_Minutes"] = response_time

# ============================================================
# Resolution Time
# ============================================================

resolution_time = []

for priority in incident_df["Priority_Code"]:

    if priority == "P1":
        resolution_time.append(round(random.uniform(1,6),2))

    elif priority == "P2":
        resolution_time.append(round(random.uniform(2,10),2))

    elif priority == "P3":
        resolution_time.append(round(random.uniform(4,30),2))

    else:
        resolution_time.append(round(random.uniform(8,60),2))

incident_df["Resolution_Time_Hours"] = resolution_time

# ============================================================
# Client Wait Hours
# ============================================================

client_wait = []

for status in incident_df["Status_Name"]:

    if status == "Awaiting Client":

        client_wait.append(round(random.uniform(4,48),2))

    else:

        client_wait.append(0)

incident_df["Client_Wait_Hours"] = client_wait

# ============================================================
# Reopen Count
# ============================================================

reopen_count = []

is_reopened = []

for status in incident_df["Status_Name"]:

    if status == "Reopened":

        reopen_count.append(random.randint(1,3))

        is_reopened.append(1)

    else:

        reopen_count.append(0)

        is_reopened.append(0)

incident_df["Reopen_Count"] = reopen_count

incident_df["Is_Reopened"] = is_reopened

# ============================================================
# Rejected
# ============================================================

is_rejected = []

rejection_reason = []

for status in incident_df["Status_Name"]:

    if status == "Rejected":

        is_rejected.append(1)

        rejection_reason.append(

            rejection.sample(1).iloc[0]["Rejection_Reason"]

        )

    else:

        is_rejected.append(0)

        rejection_reason.append(None)

incident_df["Is_Rejected"] = is_rejected

incident_df["Rejection_Reason"] = rejection_reason

# ============================================================
# Root Cause
# ============================================================

rca_list = []

for status in incident_df["Status_Name"]:

    if status in [

        "Closed",

        "Resolved",

        "Reopened"

    ]:

        rca_list.append(

            rootcause.sample(1).iloc[0]["RCA_Category"]

        )

    else:

        rca_list.append(None)

incident_df["Root_Cause"] = rca_list

# ============================================================
# Release Mapping
# ============================================================

release_version = []

for _ in range(len(incident_df)):

    if random.random() <= 0.15:

        release_version.append(

            release.sample(1).iloc[0]["Release_Version"]

        )

    else:

        release_version.append(None)

incident_df["Release_Version"] = release_version

print("Business Rules Applied Successfully")
print()

# ============================================================
# SLA Calculation
# ============================================================

sla_met = []
response_sla_met = []
resolution_sla_met = []

assigned_dates = []
resolved_dates = []
closed_dates = []

current_status_dates = []

for _, row in incident_df.iterrows():

    created = pd.to_datetime(row["Created_Date"])

    priority = row["Priority_Code"]

    response = row["Response_Time_Minutes"]

    resolution = row["Resolution_Time_Hours"]

    # ---------------- Response SLA ----------------

    if priority == "P1":
        response_limit = 15
        resolution_limit = 4

    elif priority == "P2":
        response_limit = 30
        resolution_limit = 8

    elif priority == "P3":
        response_limit = 120
        resolution_limit = 24

    else:
        response_limit = 240
        resolution_limit = 48

    response_flag = int(response <= response_limit)
    resolution_flag = int(resolution <= resolution_limit)

    response_sla_met.append(response_flag)
    resolution_sla_met.append(resolution_flag)

    sla_met.append(
        int(response_flag == 1 and resolution_flag == 1)
    )

    # ---------------- Dates ----------------

    assigned = created + timedelta(
        minutes=random.randint(1,30)
    )

    resolved = assigned + timedelta(
        hours=float(resolution)
    )

    closed = resolved + timedelta(
        hours=random.randint(24,48)
    )

    assigned_dates.append(assigned)

    resolved_dates.append(resolved)

    closed_dates.append(closed)

    current_status_dates.append(closed)

# ============================================================
# Add Columns
# ============================================================

incident_df["Assigned_Date"] = assigned_dates

incident_df["Resolved_Date"] = resolved_dates

incident_df["Closed_Date"] = closed_dates

incident_df["Current_Status_Date"] = current_status_dates

incident_df["Response_SLA_Met"] = response_sla_met

incident_df["Resolution_SLA_Met"] = resolution_sla_met

incident_df["SLA_Met"] = sla_met

# ============================================================
# Reorder Columns
# ============================================================

incident_df = incident_df[[
    "Ticket_ID",
    "Client_ID",
    "Project_ID",
    "Application_ID",
    "Team_ID",
    "User_ID",
    "Priority_Code",
    "Status_Name",
    "Created_Date",
    "Assigned_Date",
    "Resolved_Date",
    "Closed_Date",
    "Current_Status_Date",
    "Response_Time_Minutes",
    "Resolution_Time_Hours",
    "Client_Wait_Hours",
    "Reopen_Count",
    "Root_Cause",
    "Rejection_Reason",
    "Release_Version",
    "Response_SLA_Met",
    "Resolution_SLA_Met",
    "SLA_Met",
    "Is_Rejected",
    "Is_Reopened"
]]

# ============================================================
# Save CSV
# ============================================================

incident_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ============================================================
# Summary
# ============================================================

print("=" * 60)
print("Fact_Incident.csv Generated Successfully")
print("=" * 60)

print(f"Total Incidents : {len(incident_df):,}")

print(f"SLA Met         : {incident_df['SLA_Met'].sum():,}")

print(f"Rejected        : {incident_df['Is_Rejected'].sum():,}")

print(f"Reopened        : {incident_df['Is_Reopened'].sum():,}")

print()

print("File Location")

print(OUTPUT_FILE)

print()

print(incident_df.head())