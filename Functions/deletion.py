import csv

def delete_jobcard(username, delivery_date):
    file_name = "Data/jobcards.csv"
    
    # Read the jobcards from the file into a list
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        jobcards = list(reader)
    
    # Filter out the jobcard with the given username and delivery date
    updated_jobcards = [jobcard for jobcard in jobcards if not (jobcard[0] == username and jobcard[5] == delivery_date)]
    
    # Write the updated list back to the file
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_jobcards)

if __name__ == "__main__":
    delete_jobcard("Navadeep", "2024-05-21")
