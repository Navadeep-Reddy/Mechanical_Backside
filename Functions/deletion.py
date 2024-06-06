import csv

def delete_jobcard(username, delivery_date):
    file_name = "Data/jobcards.csv"
    print(f"Running delete_jobcard with username: '{username}' and delivery_date: '{delivery_date}'")
    
    # Read the jobcards from the file into a list
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        jobcards = list(reader)
    
    
    # Filter out the jobcard with the given username and delivery date
    updated_jobcards = [jobcard for jobcard in jobcards if not (jobcard[0].strip() == username and jobcard[6].strip() == delivery_date)]
    
    
    # Write the updated list back to the file
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_jobcards)

if __name__ == "__main__":
    delete_jobcard("Navadeep", "2024-06-25")
