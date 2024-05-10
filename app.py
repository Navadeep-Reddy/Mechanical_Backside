#Importing functions needed for webpage
from flask import Flask, render_template, request

#importing functions from another file
from write import users_log, orders_log

#Dictionary that stores the usernames and passwords
userpass = {"Navadeep": "Water", "Anakin": "Sand", "TamilBharathi": "123"}
print(userpass)

#Default value of username for displaying 
about_name = "There"

#Counter variable for " / " Get requests for index
index_get_count = 0

app = Flask(__name__)


#Handles authentication and the rendering of the landing and login page
@app.route('/', methods=["POST", "GET"])
def index():
    global about_name
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

#Created a new route for the about page
@app.route('/about')
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
        vehicle_type = request.form.get("vtype", "Did not work")
        repair_type = request.form.get("repair", "Not working")

        #Pass It into the imported function to write It into a file
        orders_log(about_name ,vehicle_type, repair_type)

        #Render the same page with the updated message
        return render_template("request.html", confirm = "Your Order Has Been Noted")
