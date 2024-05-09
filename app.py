#Importing functions needed for webpage
from flask import Flask, render_template, request

#importing functions from another file
from write import users_log, orders_log

#Dictionary that stores the usernames and passwords
userpass = {"Navadeep": "Water", "Anakin": "Sand", "TamilBharathi": "123"}

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

    if request.method == "GET": 
        if (index_get_count == 0):
            index_get_count += 1
            return render_template("index.html", message="")
        else:
            return render_template("land.html")
    
    if request.method == "POST":
        username = request.form.get("Username", None).strip()
        about_name = username
        password = request.form.get("Password", None)
        if username in userpass:
            if userpass[username] == password:
                return render_template("land.html")
            else:
                return render_template("index.html", message="Incorrect Password!")
        else:
            return render_template("index.html", message="User does not exist!")


@app.route('/about')
def about():
    return render_template("about.html", user = about_name)


@app.route("/make_request", methods=['GET', 'POST'])
def make_request():
    if request.method == "GET":
        return render_template("request.html")

    if request.method == "POST":
        vehicle_type = request.form.get("vtype", "Did not work")
        repair_type = request.form.get("repair", "Not working")
        orders_log(about_name ,vehicle_type, repair_type)
        return render_template("request.html", confirm = "Your Order Has Been Noted")
