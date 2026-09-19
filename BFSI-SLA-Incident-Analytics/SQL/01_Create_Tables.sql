USE BFSI_SLA_Analytics;

/*==========================================================
    DIM_CLIENT
==========================================================*/
CREATE TABLE dim.Dim_Client(
Client_ID VARCHAR(20) PRIMARY KEY,
Client_Name VARCHAR(150) NOT NULL,
Industry VARCHAR(100) NOT NULL,
Country VARCHAR(100) NOT NULL,
Region VARCHAR(50) NOT NULL,
Support_Model VARCHAR(50) NOT NULL,
Contract_Start_Date DATE NOT NULL,
Contract_End_Date DATE NOT NULL,
Is_Active BIT NOT NULL
);


/*==========================================================
    DIM_PROJECT
==========================================================*/
CREATE TABLE dim.Dim_Project(
Project_ID VARCHAR(20) PRIMARY KEY,
Client_ID VARCHAR(20) NOT NULL,
Project_Name VARCHAR(150) NOT NULL,
Business_Unit VARCHAR(100) NOT NULL,
Project_Manager VARCHAR(100) NOT NULL,
Go_Live_Date DATE NOT NULL,
Support_Start_Date DATE NOT NULL,
Project_Status VARCHAR(50) NOT NULL,
CONSTRAINT FK_Project_Client FOREIGN KEY(Client_ID)
REFERENCES dim.Dim_Client(Client_ID)
);
GO

/*==========================================================
    DIM_APPLICATION
==========================================================*/
CREATE TABLE dim.Dim_Application(
Application_ID VARCHAR(20) PRIMARY KEY,
Project_ID VARCHAR(20) NOT NULL,
Application_Name VARCHAR(150) NOT NULL,
Module_Name VARCHAR(100) NOT NULL,
Technology VARCHAR(100) NOT NULL,
Criticality VARCHAR(50) NOT NULL,
Is_Production BIT NOT NULL,
CONSTRAINT FK_Application_Project FOREIGN KEY(Project_ID)
REFERENCES dim.Dim_Project(Project_ID)
);


/*==========================================================
    DIM_TEAM
==========================================================*/
CREATE TABLE dim.Dim_Team(
Team_ID VARCHAR(20) PRIMARY KEY,
Team_Name VARCHAR(100) NOT NULL,
Department VARCHAR(100) NOT NULL,
Team_Manager VARCHAR(100) NOT NULL,
Shift VARCHAR(30) NOT NULL
);


/*==========================================================
DIM_USER
==========================================================*/
CREATE TABLE dim.Dim_User(
User_ID VARCHAR(20) PRIMARY KEY,
Team_ID VARCHAR(20) NOT NULL,
Employee_Name VARCHAR(100) NOT NULL,
Designation VARCHAR(100) NOT NULL,
Experience_Years INT NOT NULL,
Email VARCHAR(150) NOT NULL,
Location VARCHAR(100) NOT NULL,
Shift VARCHAR(30) NOT NULL,
Is_Active BIT NOT NULL,
CONSTRAINT FK_User_Team FOREIGN KEY(Team_ID)
REFERENCES dim.Dim_Team(Team_ID)
);

CREATE TABLE dim.Dim_Priority(
Priority_Code VARCHAR(10) PRIMARY KEY,
Priority_Name VARCHAR(50) NOT NULL,
Response_SLA_Minutes INT NOT NULL,
Resolution_SLA_Hours INT NOT NULL,
Business_Hours_Only BIT NOT NULL
);

CREATE TABLE dim.Dim_Status(
Status_Name VARCHAR(50) PRIMARY KEY
);

CREATE TABLE dim.Dim_RootCause(
RCA_Category VARCHAR(150) PRIMARY KEY
);

CREATE TABLE dim.Dim_RejectionReason(
Rejection_Reason VARCHAR(200) PRIMARY KEY
);


/*==========================================================
DIM_RELEASE
==========================================================*/
CREATE TABLE dim.Dim_Release(
Release_ID VARCHAR(20) PRIMARY KEY,
Release_Version VARCHAR(50) NOT NULL,
Release_Type VARCHAR(50) NOT NULL,
Deployment_Date DATE NOT NULL,
Rollback_Flag BIT NOT NULL,
Deployment_Status VARCHAR(50) NOT NULL
);

/*==========================================================
DIM_SLA_POLICY
==========================================================*/
CREATE TABLE dim.Dim_SLA_Policy(
SLA_ID VARCHAR(20) PRIMARY KEY,
Priority_Code VARCHAR(10) NOT NULL,
Response_SLA_Minutes INT NOT NULL,
Resolution_SLA_Hours INT NOT NULL,
Business_Hours_Only BIT NOT NULL,
Effective_From DATE NOT NULL,
Effective_To DATE NOT NULL,
CONSTRAINT FK_SLA_Priority FOREIGN KEY(Priority_Code)
REFERENCES dim.Dim_Priority(Priority_Code)
);

/*==========================================================
DIM_DATE
==========================================================*/
CREATE TABLE dim.Dim_Date(
Date_Key INT PRIMARY KEY,
Full_Date DATE NOT NULL,
Day_Number INT NOT NULL,
Day_Name VARCHAR(20) NOT NULL,
Week_Number INT NOT NULL,
Month_Number INT NOT NULL,
Month_Name VARCHAR(20) NOT NULL,
Quarter_Number INT NOT NULL,
Year_Number INT NOT NULL,
Financial_Year VARCHAR(20) NOT NULL,
Is_Weekend BIT NOT NULL,
Is_Holiday BIT NOT NULL
);


/*==========================================================
FACT_INCIDENT
==========================================================*/
CREATE TABLE fact.Fact_Incident(
Ticket_ID VARCHAR(20) PRIMARY KEY,
Client_ID VARCHAR(20) NOT NULL,
Project_ID VARCHAR(20) NOT NULL,
Application_ID VARCHAR(20) NOT NULL,
Team_ID VARCHAR(20) NOT NULL,
User_ID VARCHAR(20) NOT NULL,
Priority_Code VARCHAR(10) NOT NULL,
Status_Name VARCHAR(50) NOT NULL,
Created_Date DATETIME NOT NULL,
Assigned_Date DATETIME NULL,
Resolved_Date DATETIME NULL,
Closed_Date DATETIME NULL,
Current_Status_Date DATETIME NULL,
Response_Time_Minutes INT NOT NULL,
Resolution_Time_Hours DECIMAL(10,2) NOT NULL,
Client_Wait_Hours DECIMAL(10,2) NOT NULL,
Reopen_Count INT NOT NULL,
Root_Cause VARCHAR(150) NULL,
Rejection_Reason VARCHAR(200) NULL,
Release_Version VARCHAR(50) NULL,
Response_SLA_Met BIT NOT NULL,
Resolution_SLA_Met BIT NOT NULL,
SLA_Met BIT NOT NULL,
Is_Rejected BIT NOT NULL,
Is_Reopened BIT NOT NULL,

CONSTRAINT FK_Fact_Client FOREIGN KEY(Client_ID)
REFERENCES dim.Dim_Client(Client_ID),

CONSTRAINT FK_Fact_Project FOREIGN KEY(Project_ID)
REFERENCES dim.Dim_Project(Project_ID),

CONSTRAINT FK_Fact_Application FOREIGN KEY(Application_ID)
REFERENCES dim.Dim_Application(Application_ID),

CONSTRAINT FK_Fact_Team FOREIGN KEY(Team_ID)
REFERENCES dim.Dim_Team(Team_ID),

CONSTRAINT FK_Fact_User FOREIGN KEY(User_ID)
REFERENCES dim.Dim_User(User_ID),

CONSTRAINT FK_Fact_Priority FOREIGN KEY(Priority_Code)
REFERENCES dim.Dim_Priority(Priority_Code),

CONSTRAINT FK_Fact_Status FOREIGN KEY(Status_Name)
REFERENCES dim.Dim_Status(Status_Name)
);


CREATE INDEX IX_Fact_CreatedDate ON fact.Fact_Incident(Created_Date);
CREATE INDEX IX_Fact_Project ON fact.Fact_Incident(Project_ID);
CREATE INDEX IX_Fact_Priority ON fact.Fact_Incident(Priority_Code);
CREATE INDEX IX_Fact_Status ON fact.Fact_Incident(Status_Name);
