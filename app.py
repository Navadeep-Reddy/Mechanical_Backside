from flask import Flask, render_template, request

# Dictionary that stores the usernames and passwords
userpass = {"Navadeep": "Water", "Anakin": "Sand", "TamilBharathi": "123"}

#Default value of username for displaying 
about_name = "There"

app = Flask(__name__)



@app.route('/', methods=["POST", "GET"])
def index():
    global about_name
    if request.method == "GET":
        return render_template("index.html", message="")
    
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
    return render_template("request.html")
