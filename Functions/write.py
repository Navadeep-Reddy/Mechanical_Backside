import csv
      
def orders_log(username, vehicle_type, repair_type):
    file_name="jobcards.csv"
    with open("Data/" + file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow((username, vehicle_type, repair_type))
    

def new_user_log(username, password):
    with open("Data/user_log.txt", "a") as f:
        f.write(f"{username} {password}")
        f.write("\n")
  




