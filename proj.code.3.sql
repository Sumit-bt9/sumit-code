SELECT Server_ID, Server_Location, Downtime_Minutes, Crash_Reason
FROM it_project.server_downtime_logs
WHERE Environment = 'Production'
ORDER BY Downtime_Minutes DESC
LIMIT 3;

