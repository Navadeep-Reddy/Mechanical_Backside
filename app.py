# app.py
from flask import Flask, render_template, request
from Functions.write import new_user_log, orders_log
from Functions.read_prog import UserDetails, alljobcards

# Dictionary that stores the usernames and passwords
userpass = UserDetails()

# Default value of username for displaying 
about_name = "There"
index_get_count=0

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    global about_name
    global index_get_count
    if request.method == "GET":
        if index_get_count == 0:
            index_get_count += 1
            return render_template("index.html", message="")
        else:
            return render_template("land.html")
    
    if request.method == "POST":
        username = request.form.get("Username", None).strip()
        password = request.form.get("Password", None)
        about_name = username

        if username in userpass:
            if userpass[username] == password:
                return render_template("land.html")
            else:
                return render_template("index.html", message="Incorrect Password!")
        else:
            return render_template("index.html", message="User does not exist!")

@app.route("/create_account", methods=["POST", "GET"])
def create_account():
    if request.method == "GET":
        return render_template("new_account.html")
    
    elif request.method == "POST":
        new_username = request.form.get("user", "Error")
        new_password = request.form.get("password", "No")
        new_user_log(new_username, new_password)
        userpass = UserDetails()
        return render_template('index.html', message="New Account Created")

@app.route('/about', methods=["POST", "GET"])
def about():
    return render_template("about.html", user=about_name)

@app.route("/make_request", methods=['GET', 'POST'])
def make_request():
    if request.method == "GET":
        return render_template("request.html")
    
    if request.method == "POST":
        vehicle_type = request.form.get("vtype", "Empty")
        repair_type = request.form.get("repair", "Empty")
        engine_no = request.form.get("eng_no", "Empty")
        reg_no = request.form.get("reg_no", "Empty")
        delivery_date = request.form.get("date", "Empty")
        emergency_state = request.form.get("emergency", "off")
        orders_log(about_name, vehicle_type, repair_type, engine_no, reg_no, delivery_date, emergency_state)
        return render_template("request.html", confirm="Your Order Has Been Noted")

@app.route("/pending")
def pending():
    jobcards = alljobcards()
    user_jobs = [card for card in jobcards if card.username == about_name]

    if len(user_jobs) == 0:
        return render_template('pending.html', name=about_name, Vehicle_Type="NIL", Repair_Type="NIL", Engine_No="NIL", Registration_No="NIL", Est_Date="NIL")
    else:
        First_Job = user_jobs[0]
        return render_template('pending.html', name=about_name, Vehicle_Type=First_Job.vehicle, Repair_Type=First_Job.repair, Engine_No=First_Job.engine_no, Registration_No=First_Job.reg_no, Est_Date=First_Job.delivery_date)

