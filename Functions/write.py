import csv
      
def orders_log(username, email, vehicle_type, repair_type, engine_no, reg_no, delivery_date, emergency_state):
    file_name="jobcards.csv"
    with open("Data/" + file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow((username, email, vehicle_type, repair_type, engine_no, reg_no, delivery_date, emergency_state))
    

def new_user_log(username, password, email):
    with open("Data/user_log.txt", "a") as f:
        f.write(f"{username} {password} {email}")
        f.write("\n")
  




