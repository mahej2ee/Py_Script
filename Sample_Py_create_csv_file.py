import csv
import datetime
import os
access_token=os.getenv('ACCESS_TOKEN')
# access_token = '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'

# org name
org_name = 'new-gen-omega'

# Initialize the Github instance with your access token
# g = Github(access_token)


def generate_csv_with_date():
    # Generate filename with today's date
    today = datetime.date.today()
    filename = f"REPORT_{today.strftime('%Y%m%d%H%M%S')}.csv"

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

    print(f"CSV file '{filename}' created successfully!")

    # Rename the CSV file to include the current date
    #os.rename(filename, f"REPORT_{today.strftime('%Y-%m-%d-%h-%m-%s')}.csv")

if __name__ == "__main__":
    generate_csv_with_date()
