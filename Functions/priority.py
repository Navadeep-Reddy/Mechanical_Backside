# Functions/priority.py
from Functions.jobcard import JobCard
from datetime import datetime

class PriorityQueue:
    def __init__(self, jobcards):
        self.jobcards = jobcards

    def sort_jobcards(self):
        self.jobcards.sort(key=self.priority_key)
        return self.jobcards

    @staticmethod
    def priority_key(jobcard):
        try:
            # Convert delivery date string to a datetime object
            delivery_date = datetime.strptime(jobcard.delivery_date, "%Y-%m-%d")
        except ValueError:
            # If the date is malformed or empty, use a default far future date
            delivery_date = datetime.max
        # Emergency jobs are given the highest priority
        emergency_priority = 0 if jobcard.emergency_state == "on" else 1
        return (emergency_priority, delivery_date)
