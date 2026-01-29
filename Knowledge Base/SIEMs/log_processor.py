import os
import csv

# Define the path to the CSV file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'wazuh_report.csv')

# List to hold processed alerts
alerts = []

# Function to extract relevant fields from each row and create an alert dictionary
def extract_alert(row):
    alert = {
        'timestamp': row['_source.timestamp'],
        'agent_name': row['_source.agent.name'],
        'agent_id': row['_source.agent.id'],
        'rule_level': row['_source.rule.level'],
        'rule_description': row['_source.rule.description'],
        'rule_id': row['_source.rule.id'],
        'decoder': row['_source.decoder.name'],
        'full_log': row['_source.full_log']
    }
    return alert

# Function to export alerts to a new CSV file
def export_csv(alerts, output_path):
    fieldnames = ['timestamp', 'agent_name', 'agent_id', 'rule_level', 'rule_description', 'rule_id', 'decoder', 'full_log']
    with open(output_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for alert in alerts:
            writer.writerow(alert)

# Read the CSV file and process each row
with(open(csv_path, mode='r') as file):
    reader = csv.DictReader(file)
    for row in reader:
        alert = extract_alert(row)
        alerts.append(alert)

# Export the processed alerts to a new CSV file
output_csv_path = os.path.join(BASE_DIR, 'processed_wazuh_report.csv')
export_csv(alerts, output_csv_path)

       


    