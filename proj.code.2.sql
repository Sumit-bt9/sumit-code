
SELECT Server_Location, SUM(Downtime_Minutes) as Total_Downtime_Mins
FROM it_project.server_downtime_logs
GROUP BY Server_Location
ORDER BY Total_Downtime_Mins DESC;

