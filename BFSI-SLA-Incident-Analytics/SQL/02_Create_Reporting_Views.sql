USE BFSI_SLA_Analytics;


CREATE VIEW rpt.vw_Executive_Summary
AS
SELECT
COUNT(*) AS Total_Incidents,
SUM(CASE WHEN SLA_Met=1 THEN 1 ELSE 0 END) AS SLA_Met,
SUM(CASE WHEN SLA_Met=0 THEN 1 ELSE 0 END) AS SLA_Breached,
SUM(CASE WHEN Is_Rejected=1 THEN 1 ELSE 0 END) AS Rejected,
SUM(CASE WHEN Is_Reopened=1 THEN 1 ELSE 0 END) AS Reopened,
AVG(Response_Time_Minutes) AS Avg_Response_Minutes,
AVG(Resolution_Time_Hours) AS Avg_Resolution_Hours,
CAST(
100.0 *
SUM(CASE WHEN SLA_Met=1 THEN 1 ELSE 0 END)
/ COUNT(*)
AS DECIMAL(5,2)
) AS SLA_Percentage
FROM fact.Fact_Incident;

CREATE VIEW rpt.vw_SLA_Trend
AS
SELECT
CAST(Created_Date AS DATE) AS Incident_Date,
COUNT(*) AS Total_Incidents,
SUM(CASE WHEN SLA_Met=1 THEN 1 ELSE 0 END) AS SLA_Met,
SUM(CASE WHEN SLA_Met=0 THEN 1 ELSE 0 END) AS SLA_Breached,
CAST(
100.0 *
SUM(CASE WHEN SLA_Met=1 THEN 1 ELSE 0 END)
/ COUNT(*)
AS DECIMAL(5,2)
) AS SLA_Percentage
FROM fact.Fact_Incident
GROUP BY
CAST(Created_Date AS DATE);

CREATE VIEW rpt.vw_Team_Performance
AS
SELECT
t.Team_Name,
COUNT(*) AS Total_Incidents,
SUM(CASE WHEN f.SLA_Met=1 THEN 1 ELSE 0 END) AS SLA_Met,
SUM(CASE WHEN f.SLA_Met=0 THEN 1 ELSE 0 END) AS SLA_Breached,
CAST(
100.0 *
SUM(CASE WHEN f.SLA_Met=1 THEN 1 ELSE 0 END)
/ COUNT(*)
AS DECIMAL(5,2)
) AS SLA_Percentage,
AVG(f.Resolution_Time_Hours) AS Avg_Resolution_Hours,
SUM(CAST(f.Is_Reopened AS INT)) AS Reopened,
SUM(CAST(f.Is_Rejected AS INT)) AS Rejected
FROM fact.Fact_Incident f
JOIN dim.Dim_Team t
ON f.Team_ID=t.Team_ID
GROUP BY
t.Team_Name;

CREATE OR ALTER VIEW rpt.vw_Project_Performance
AS
SELECT
    p.Project_Name,
    COUNT(*) AS Total_Incidents,
    AVG(f.Resolution_Time_Hours) AS Avg_Resolution,
    SUM(CAST(f.Is_Reopened AS INT)) AS Reopened,
    SUM(CAST(f.Is_Rejected AS INT)) AS Rejected,
    CAST(
        100.0 * SUM(CASE WHEN f.SLA_Met = 1 THEN 1 ELSE 0 END)
        / COUNT(*)
        AS DECIMAL(5,2)
    ) AS SLA_Percentage
FROM fact.Fact_Incident f
INNER JOIN dim.Dim_Project p
	ON f.Project_ID = p.Project_ID
GROUP BY p.Project_Name;

CREATE OR ALTER VIEW rpt.vw_Rejection_Analysis
AS
SELECT
    Rejection_Reason,
    COUNT(*) AS Rejected_Count
FROM fact.Fact_Incident
WHERE Is_Rejected = 1
GROUP BY Rejection_Reason;

CREATE OR ALTER VIEW rpt.vw_RootCause_Analysis
AS
SELECT
    Root_Cause,
    COUNT(*) AS Incident_Count,
    AVG(Resolution_Time_Hours) AS Avg_Resolution
FROM fact.Fact_Incident
GROUP BY Root_Cause;




