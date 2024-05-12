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

    with open("Data/" + file_name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            username, vehicle, repair = row
            jobcard_object = JobCard(username, vehicle, repair)
            jobcards_objects.append(jobcard_object)

    return jobcards_objects