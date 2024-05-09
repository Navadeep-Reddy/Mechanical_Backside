def users_log(username):
    with open("Data/user_log.txt", "a") as f:
        f.write(f"User: {username}")
        f.write("\n")
        
def orders_log(username, vehicle_type, repair_type):
    with open("Data/repair_log.txt", "a") as f:
        f.write(f"User: {username} Vehicle Type: {vehicle_type} Repair: {repair_type}")
        f.write("\n")

