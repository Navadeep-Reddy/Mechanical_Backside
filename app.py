#Importing functions needed for webpage
from flask import Flask, render_template, request, jsonify

#importing functions from another file
from Functions.write import new_user_log, orders_log
from Functions.read_prog import UserDetails,alljobcards
from Functions.graphs import bike_graph,  car_graph, cycle_graph 

#Dictionary that stores the usernames and passwords
userpass=UserDetails()

#Generate graphs for each vehicle type and its repairs
bike_repairs = bike_graph()
car_repairs = car_graph()
cycle_repairs = cycle_graph()

#Default value of username for displaying 
about_name = "There"
vehicle_type="Vehicle"
repair_type="Repair"

#Counter variable for " / " Get requests for index
index_get_count = 0

app = Flask(__name__)


#Handles authentication and the rendering of the landing and login page
@app.route('/', methods=["POST", "GET"])
def index():
    global about_name
    global vehicle_type
    global repair_type
    global index_get_count   

    #rendering login page when It is the first get request to "/" route and rendering landing page if it's more than one
    if request.method == "GET":
        if (index_get_count == 0):
            index_get_count += 1
            return render_template("index.html", message="")
        else:
            return render_template("land.html")
    
    #If its a post request, we get the data from the route and render landing page if correct else render login again with message
    if request.method == "POST":
        
        #get username and password from the route
        username = request.form.get("Username", None).strip()
        password = request.form.get("Password", None)

        #Storing the username in a global variable to be reused outside this funcion
        about_name = username

        #Check if username exists in dictionary
        if username in userpass:
            if userpass[username] == password:
                return render_template("land.html")
            else:
                return render_template("index.html", message="Incorrect Password!")
        else:
            return render_template("index.html", message="User does not exist!")


        
#creating new route for account creation
@app.route("/create_account", methods = ["POST", "GET"])
def create_account():
    global userpass

    if request.method == "GET":
        return render_template("new_account.html")
    
    elif request.method == "POST":
        #getting values of new account
        new_username = request.form.get("user", "Error")
        new_password = request.form.get("password", "No")

        #writing new values into file
        new_user_log(new_username, new_password)

        #updating dictionary after new account
        userpass=UserDetails()
        return render_template('index.html', message = "New Account Created")




#Created a new route for the about page
@app.route('/about', methods = ["POST", "GET"])
def about():
    return render_template("about.html", user = about_name)

#Created a new route for make a request button
@app.route("/make_request", methods=['GET', 'POST'])
def make_request():
    #Render the page when it's the (first) get request
    if request.method == "GET":
        return render_template("request.html")

    #If It's a post request then It means that submission has occured
    if request.method == "POST":

        #Store the vehicle_type and repair_type in variables
        vehicle_type = request.form.get("vtype", "Empty")
        repair_type = request.form.get("repair", "Empty")
        engine_no = request.form.get("eng_no", "Empty")
        reg_no = request.form.get("reg_no", "Empty")
        delivery_date = request.form.get("date", "Empty")

        #setting default value of button to be off as on is the value we get when selected 
        emergency_state = request.form.get("emergency", "off")

        #Writing info of order into csv
        orders_log(about_name, vehicle_type, repair_type, engine_no, reg_no, delivery_date, emergency_state)

        #Render the same page with the updated message
        return render_template("request.html", confirm = "Your Order Has Been Noted")

#Ajax to get the related repairs
@app.route('/get_related_repairs', methods=['POST'])
def get_related_repairs():
    data = request.get_json()
    repair_type = data.get('repair_type')
    vehicle_type = data.get('vehicle_type')
    
    # Initialize the variable to store the next related repairs
    next_repairs = []

    if vehicle_type == "Car":
        next_repairs = car_repairs.next_related_repair(repair_type)
    elif vehicle_type == "Motorcycle":
        next_repairs = bike_repairs.next_related_repair(repair_type)
    elif vehicle_type == "Bicycle":
        next_repairs = cycle_repairs.next_related_repair(repair_type)
    
    # Return the related repairs as a JSON response
    return jsonify(next_repairs)


@app.route("/pending")
def pending():
    #Get class objects of all current jobcards into a list
    jobcards=alljobcards()

    #new list for storing jobcard objects of the current user
    user_jobs = []

    for card in jobcards:
        if card.username == about_name:
            user_jobs.append(card)

    if (len(user_jobs) == 0):

        return render_template('pending.html', name = about_name, Vehicle_Type = "NIL", Repair_Type ="NIL", Engine_No ="NIL", Registration_No ="NIL", Est_Date = "NIL")
    
    else:
        #Get the earliest submitted request
        First_Job = user_jobs[0]
        return render_template('pending.html', name = about_name, Vehicle_Type = First_Job.vehicle, Repair_Type = First_Job.repair, Engine_No =First_Job.engine_no, Registration_No =First_Job.reg_no, Est_Date = First_Job.delivery_date)



