#Importing modules for mechanic login
from flask import Flask, render_template, request, jsonify, url_for

from Functions.read_prog import alljobcards
from Functions.deletion import delete_jobcard

import os
os.chdir(os.path.dirname(os.getcwd()))

#creating 
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        return render_template("orders.html")
    
    if request.method == "POST":

        name = request.form.get("customer_name")
        date = request.form.get("date")
        

        delete_jobcard(name, date)

        return render_template("orders.html", order_url = url_for('orders'))
    

@app.route("/get_jobs", methods = ["GET"])
def get_jobs():

    #List for storing all jobcards to send to javascript
    jobcards =  alljobcards()

    #List for storing the required fields for javascript
    Data = []

    for card in jobcards:
        Data.append([card.username, card.vehicle, card.repair, card.reg_no, card.delivery_date])
        
    return jsonify(Data)
    
