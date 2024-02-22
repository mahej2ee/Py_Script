from github import Github
from github import InputFileContent
from datetime import datetime
import csv
import datetime
import os
# access_token=os.getenv('ACCESS_TOKEN')
access_token = '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'

# org name
org_name = 'new-gen-omega'

# Initialize the Github instance with your access token
g = Github(access_token)
def generate_csv(filename):
    # Sample data to write to CSV
    data = [
        {"Name": "John", "Age": 30, "City": "New York"},
        {"Name": "Alice", "Age": 25, "City": "Los Angeles"},
        {"Name": "Bob", "Age": 35, "City": "Chicago"}
    ]
    
    # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    # Generate filename with today's date
    today = datetime.date.today()
    filename = f"output_{today.strftime('%Y-%m-%d')}.csv"
    
    # Generate CSV file
    generate_csv(filename)
    print(f"CSV file '{filename}' created successfully!")

if __name__ == "__main__":
    main()
