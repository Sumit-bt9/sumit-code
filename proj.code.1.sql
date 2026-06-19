SELECT Crash_Reason, COUNT(*) as Total_Crashes, SUM(Downtime_Minutes) as Total_Downtime_Mins
FROM it_project.server_downtime_logs
GROUP BY Crash_Reason
ORDER BY Total_Downtime_Mins DESC;
