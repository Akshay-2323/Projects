

# BFSI SLA & Incident Analytics

## 📊 Project Overview

The **BFSI SLA & Incident Analytics** project is an end-to-end data analytics solution designed to analyze IT incidents, SLA compliance, ticket performance, resolution times, rejections, reopenings, root causes, projects, and support teams in a BFSI operations environment.

The project demonstrates how operational incident data can be transformed into meaningful business insights using **Python, SQL Server, and Power BI**.

The solution processes **150,000 incident records** and provides an interactive **5-page Power BI dashboard** for executive monitoring and detailed operational analysis.

---

## 🎯 Business Objective

The primary objective of this project is to help operations and management teams:

- Monitor overall incident volume
- Track SLA compliance and SLA breaches
- Analyze incident resolution performance
- Identify high-volume teams and projects
- Understand incident root causes
- Monitor rejected and reopened tickets
- Analyze incident trends over time
- Compare SLA performance across priorities
- Identify operational areas requiring attention
- Drill down from high-level KPIs to individual incident records

---

## 🏗️ Solution Architecture

```text
                Python
                  │
                  ▼
        Data Generation & Preparation
                  │
                  ▼
             SQL Server
                  │
        ┌─────────┴─────────┐
        │                   │
   Dimension Tables      Fact Table
        │                   │
        └─────────┬─────────┘
                  ▼
             SQL Views
                  │
                  ▼
              Power BI
                  │
                  ▼
       Interactive Dashboard

## 🛠️ Technology Stack

| Technology | Purpose                                                          |
| ---------- | ---------------------------------------------------------------- |
| Python     | Data generation, preparation and SQL Server loading              |
| Pandas     | Data processing and CSV handling                                 |
| SQL Server | Data storage and analytical database                             |
| SQL        | Database design, transformations, validation and reporting views |
| Power BI   | Interactive dashboard and visualization                          |
| DAX        | KPI calculations and analytical measures                         |
| GitHub     | Project version control and portfolio presentation               |

---

## 🗄️ Data Model

The SQL Server database is designed using a dimensional model.

### Dimension Tables

The project contains dimensions for:

* Client
* Project
* Application
* Team
* User
* Priority
* Status
* Root Cause
* Rejection Reason
* Release
* SLA Policy
* Date

### Fact Table

The central fact table is:

```text
fact.Fact_Incident
```

It contains incident-level information including:

* Ticket ID
* Client
* Project
* Application
* Priority
* Team
* Status
* Created Date
* Resolution Date
* Resolution Time
* Response Time
* SLA Status
* Rejection Status
* Reopen Status
* Root Cause
* Rejection Reason

### Reporting Layer

Reporting views are created under the:

```text
rpt
```

schema to support analytical reporting and Power BI consumption.

---

# 📈 Power BI Dashboard

The Power BI solution contains **5 analytical pages**.

## 1. Executive Dashboard

Provides a management-level overview of incident operations.

### Key KPIs

* Total Incidents
* SLA Compliance %
* SLA Not Met
* Rejected Tickets
* Reopened Tickets
* Average Resolution Hours
* Average Response Minutes
* Active Clients

### Analysis

* Incident trend
* SLA trend
* Incidents by priority
* Incidents by status
* Incidents by project

---

## 2. SLA & Performance Analysis

Focuses on SLA compliance and resolution performance.

### Key Metrics

* SLA Compliance %
* SLA Not Met
* Average Resolution Hours
* Median Resolution Hours
* P90 Resolution Hours

### Analysis

* SLA compliance trend
* SLA compliance by priority
* Resolution performance by team
* SLA performance by project
* SLA breaches by priority
* Resolution time distribution
* Project-level performance table

---

## 3. Incident & Root Cause Analysis

Focuses on understanding why incidents occur and how rejected/reopened tickets are distributed.

### Analysis

* Incidents by root cause
* Rejected incidents by rejection reason
* Reopened incidents by priority
* Incidents by team
* Monthly incident trend
* Summary performance metrics

---

## 4. Team & Operational Analysis

Focuses on operational performance across support teams.

### Analysis

* SLA compliance by team
* Incident workload by team
* Average resolution time by team
* Reopened tickets by team
* Incident workload by priority and team
* Team performance comparison table

---

## 5. Ticket & Detailed Analysis

Provides detailed incident-level analysis.

### Analysis

* Incident status distribution
* SLA status by priority
* Incidents by resolution time
* Incident trend
* Detailed incident table

The detailed table allows users to examine individual ticket-level information including resolution time, response time, SLA status, rejection status and reopen status.

---

# 📊 Key Project Metrics

The generated dataset contains approximately:

| Metric                  | Value        |
| ----------------------- | ------------ |
| Total Incidents         | 150,000      |
| SLA Compliance          | ~76.5%       |
| SLA Not Met             | ~35K         |
| Rejected Tickets        | ~6K          |
| Reopened Tickets        | ~3K          |
| Average Resolution Time | ~25 Hours    |
| Average Response Time   | ~100 Minutes |

> Dashboard values change dynamically when filters such as date, client, project, team, priority and status are applied.

---

# 🔎 Power BI Interactivity

The dashboard provides common operational filters including:

* Date Range
* Client Name
* Project Name
* Team Name
* Priority
* Status

Users can filter the dashboard and analyze how operational KPIs change across different dimensions.

---

# 🧮 Key Analytical Measures

The Power BI model includes measures for:

* Total Incidents
* SLA %
* SLA Compliance %
* SLA Breach %
* SLA Not Met
* Average Resolution Hours
* Average Response Minutes
* Median Resolution Hours
* P90 Resolution Hours
* Rejected Tickets
* Rejection Rate
* Reopened Tickets
* Reopen Rate
* MoM Incident Growth
* YTD Incidents
* Rolling 30-Day Incidents

---

# 📁 Project Structure
BFSI-SLA-Incident-Analytics/
│
├── PowerBI/
│   └── BFSI_SLA_Analytics_Dashboard.pbix
│
├── Python/
│   ├── generate_master_data.py
│   ├── generate_incidents.py
│   ├── creating_table.py
│   └── load_sqlserver.py
│
├── SQL/
│   ├── 01_Create_Tables.sql
│   └── 02_Create_Reporting_Views.sql
│
├── Screenshots/
│   ├── 01_Executive_Dashboard.png
│   ├── 02_SLA_Performance_Analysis.png
│   ├── 03_Incident_Root_Cause_Analysis.png
│   ├── 04_Team_Operational_Analysis.png
│   └── 05_Ticket_Detailed_Analysis.png
│
└── README.md
# 🐍 Python Workflow

Python is used as part of the data preparation and loading process.

### Main scripts

**generate_master_data.py**

Generates the supporting/master data used by the analytical model.

**generate_incidents.py**

Generates the incident-level dataset used for analysis.

**creating_table.py**

Creates the required SQL Server database tables.

**load_sqlserver.py**

Loads the prepared data into SQL Server using Python and SQLAlchemy.

---

# 🗃️ SQL Workflow

The SQL layer contains:

### 01_Create_Tables.sql

Creates the database structures including:

* Dimension tables
* Fact table
* Keys and relationships
* Supporting indexes

### 02_Create_Reporting_Views.sql

Creates reporting views for:

* Executive summary
* SLA trends
* Team performance
* Project performance
* Rejection analysis
* Root-cause analysis

These views provide an analytical layer between SQL Server and Power BI.

---

# 📌 Business Questions Answered

The dashboard is designed to answer questions such as:

1. How many incidents are being handled?
2. What percentage of incidents meet SLA?
3. Which priorities have the highest incident volume?
4. Which teams handle the largest workload?
5. Which projects have lower SLA compliance?
6. What are the major incident root causes?
7. Why are tickets being rejected?
8. Which priority levels have more reopened tickets?
9. How long does it take to resolve incidents?
10. How is incident volume changing over time?
11. Which teams have higher resolution workloads?
12. Which projects require closer operational monitoring?

---

# 💡 Analytical Approach

The project follows a structured analytics workflow:

1. Generate / Prepare Data
          ↓
2. Validate Data
          ↓
3. Load Data into SQL Server
          ↓
4. Build Dimensional Data Model
          ↓
5. Create SQL Reporting Views
          ↓
6. Connect Power BI
          ↓
7. Create DAX Measures
          ↓
8. Build Interactive Dashboard
          ↓
9. Analyze Operational KPIs

# 👨‍💻 Skills Demonstrated

This project demonstrates practical experience in:

### Data Engineering / SQL

* SQL Server
* Dimensional data modeling
* Fact and dimension tables
* Primary and foreign keys
* SQL views
* SQL aggregations
* CASE expressions
* Data validation
* Indexing

### Python

* Pandas
* Data generation
* Data processing
* CSV handling
* SQL Server connectivity
* SQLAlchemy

### Power BI

* Data modeling
* DAX measures
* KPI development
* Interactive filters
* Trend analysis
* Drill-down analysis
* Performance dashboards
* Operational reporting

### Analytics

* SLA analysis
* Incident management
* Root-cause analysis
* Operational performance analysis
* Trend analysis
* Team and project performance

---

# 📷 Dashboard Preview

Dashboard screenshots are available in the `Screenshots` folder.

The dashboard consists of:

1. Executive Dashboard
2. SLA & Performance Analysis
3. Incident & Root Cause Analysis
4. Team & Operational Analysis
5. Ticket & Detailed Analysis

---

# 🚀 Project Outcome

The final solution provides a centralized analytical view of incident operations and allows users to move from **executive-level KPIs to detailed ticket-level analysis**.

The project demonstrates an end-to-end workflow from:

**Python → SQL Server → SQL Reporting Layer → Power BI → Business Insights**

---

## 👤 Author

**Akshay Sharma**

Data Analyst | Data Engineering | SQL | Python | Power BI


### One important recommendation

I would **not** put phrases like **"real-time dashboard"** or **"real-time data"** in the README. Your current project is an analytical dashboard using a generated/static dataset, so saying **"operational monitoring"** is more accurate and more defensible in an interview.

Also, don't put your local SQL Server name (`Akshay\SQLEXPRESS`) or local Windows paths anywhere in GitHub.

This README is now strong enough to be the **main landing page for the project**. The next thing I'd do before making the repository public is make sure your **Python files are sanitized**, then we can make the GitHub folder structure clean and recruiter-ready.
