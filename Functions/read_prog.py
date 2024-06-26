from Functions.priority import PriorityQueue
import csv
from Functions.jobcard import JobCard
def UserDetails():
    d={}
    f=open("Data/user_log.txt","r")
    text=f.readlines()
    
    
    for word in text:
        word=word.split()
        d[word[0]]=word[1]
    return d    



def alljobcards():
    file_name = "jobcards.csv"
    jobcards_objects = []

    with open("Data/jobcards.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            username, email, vehicle, repair,  engine_no, reg_no, delivery_date, emergency_state = row
            jobcard_object = JobCard(username, email, vehicle, repair,  engine_no, reg_no, delivery_date, emergency_state)
            jobcards_objects.append(jobcard_object)

    # Create a PriorityQueue object and sort jobcards
    pq = PriorityQueue(jobcards_objects)
    sorted_jobcards = pq.sort_jobcards()
    return sorted_jobcards

def get_current_email(name):
    with open("Data/user_log.txt","r") as f:
        text = f.readlines()
        for line in text:
            L = line.split()
            if L[0] == name:
                return L[2]