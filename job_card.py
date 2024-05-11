import csv

class JobCard:
    def __init__(self):
        self.name = input("Enter name: ")
        self.Reg = input("Enter Reg no: ")
        self.issue = input("Enter the problem: ")

    def __str__(self):
        return f"Name: {self.name}, Reg No: {self.Reg}, Issue: {self.issue}"

job_cards = []

while True:
    job_cards.append(JobCard())
    add_more = input("Do you want to add another job card? (yes/no): ")
    if add_more.lower() != "yes":
        break

data = [[job_card.name, job_card.Reg, job_card.issue] for job_card in job_cards]

file_name = "job_card.csv"

with open("Data/"+file_name, "a", newline="") as file:
    csv.writer(file).writerows(data)

print("Data has been written to job_card.csv")
print(data)

print("\nContents of job_card.csv:")
with open("Data/"+file_name, newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

