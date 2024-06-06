#Importing modules for mechanic login
from flask import Flask, render_template, request, jsonify, url_for

#creating 
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        return render_template("orders.html")
    
    if request.method == "POST":

        name = request.form.get("customer_name")
        

        return render_template("orders.html", order_url = url_for('orders'))
    
