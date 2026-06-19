import csv
import random
import os

# Lists for dummy data generation
locations = ['Mumbai', 'Virginia', 'Singapore', 'London', 'Frankfurt']
environments = ['Production', 'Testing', 'Development']
reasons = ['Network Failure', 'Database Overload', 'Software Update', 'Power Outage', 'None']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Generate and write CSV file
file_name = 'server_downtime_logs.csv'

with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['Server_ID', 'Server_Location', 'Environment', 'Downtime_Minutes', 'Crash_Reason', 'Month'])
    
    # Generate 50 rows of dummy data
    for i in range(1, 51):
        server_id = f"SRV-{100 + random.randint(1, 5)}"
        loc = random.choice(locations)
        env = random.choice(environments)
        month = random.choice(months)
        reason = random.choice(reasons)
        downtime = 0 if reason == 'None' else random.randint(15, 180)
            
        writer.writerow([server_id, loc, env, downtime, reason, month])

print(f"CSV file generated: {file_name}")
os.system(f"start {file_name}")

