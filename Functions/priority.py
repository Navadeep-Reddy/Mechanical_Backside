# Functions/priority.py
from Functions.jobcard import JobCard
import csv
from datetime import datetime

class PriorityQueue:
    def __init__(self, jobcards):
        self.jobcards = jobcards

    def sort_jobcards(self):
        self.jobcards.sort(key=self.priority_key)
        return self.jobcards

    @staticmethod
    def priority_key(jobcard):
        # Convert delivery date string to a datetime object
        delivery_date = datetime.strptime(jobcard.delivery_date, "%Y-%m-%d")
        # Emergency jobs are given the highest priority
        emergency_priority = 0 if jobcard.emergency_state == "on" else 1
        return (emergency_priority, delivery_date)

def alljobcards():
    file_name = "jobcards.csv"
    jobcards_objects = []

    with open("Data/" + file_name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            username, vehicle, repair, engine_no, reg_no, delivery_date, emergency_state = row
            jobcard_object = JobCard(username, vehicle, repair, engine_no, reg_no, delivery_date, emergency_state)
            jobcards_objects.append(jobcard_object)

    # Create a PriorityQueue object and sort jobcards
    pq = PriorityQueue(jobcards_objects)
    sorted_jobcards = pq.sort_jobcards()
    return sorted_jobcards
