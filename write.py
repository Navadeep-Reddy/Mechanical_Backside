        
def orders_log(username, vehicle_type, repair_type):
    with open("Data/repair_log.txt", "a") as f:
        f.write(f"User: {username} Vehicle Type: {vehicle_type} Repair: {repair_type}")
        f.write("\n")

def new_user_log(username, password):
    with open("Data/user_log.txt", "a") as f:
        f.write(f"{username} {password}")
        f.write("\n")