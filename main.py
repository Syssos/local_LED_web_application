#!/usr/bin/python3
""" This is the main page for the web application
"""
from flask import Flask, request, redirect, make_response, jsonify, Response, abort, render_template, flash
import os
from helpers.helpers import decide_color, decide_palette, stop_color
import requests
from flask_cors import CORS
import serial                                 # add Serial library for Serial communication
from Objects.LightyObject.Lighty import Lighty
from Objects.CurrentObject.Current import Current

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SECRET_KEY'] = 'you-will-never-guess'
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
CurrentOBJ = Current()
EntertainmentController = Lighty(name="Entertainment Center", Color="Red", Pattern="Flash", ledcount="110", stripcount="5")
DeskController = Lighty(name="Desk", Color="Green", Pattern="Solid", ledcount="90", stripcount="6")

# Arduino_Serial_Enter = serial.Serial('/dev/ttyACM0',9600)  #Create Serial port object called arduinoSerialData
# Arduino_Serial_Desk = serial.Serial('/dev/ttyACM0',9600)  #Create Serial port object called arduinoSerialData
             #read the serial data and print it as line


@app.teardown_appcontext
def tear_down(self):
    return


@app.errorhandler(404)
def not_found(error):
    "error handler for 404"
    return render_template('custom_404.html')

# START MAIN ROUTES

#HOME
@app.route('/', strict_slashes=False)
def home():
    """ Home page
        return: template for index with required information
    """
    Color = request.args.get('Color')
    if (Color):
        CurrentOBJ.SetHome(Color)
        return render_template('index.html', CC=CurrentOBJ.Home)
    return render_template('index.html', CC=CurrentOBJ.Home)

@app.route('/enter', strict_slashes=False)
def Entertainment():
    """ Home page
        return: template for index with required information
    """
    Color = request.args.get('Color')
    if (Color):
        CurrentOBJ.SetEnter(Color)
        return render_template('Entertainment.html', CC=CurrentOBJ.Enter)
    return render_template("Entertainment.html", CC=CurrentOBJ.Enter)

@app.route('/desk', strict_slashes=False)
def Desk():
    """ Home page
        return: template for index with required information
    """
    Color = request.args.get('Color')
    if (Color):
        CurrentOBJ.SetDesk(Color)
        
        return render_template('desk.html', CC=CurrentOBJ.Desk)
    return render_template("desk.html", CC=CurrentOBJ.Desk)

# @app.route('/test', strict_slashes=False)
# def testroute():
#     objectstest = []
#     objectstest.append(EntertainmentController)
#     objectstest.append(DeskController)
#     return jsonify(objectstest)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=False)

# @app.route('/endcolor', methods=['GET', 'POST'], strict_slashes=False)
# def stopcolor():
# #    stop_color(Arduino_Serial_Desk)
# #    stop_color(Arduino_Serial_Enter)
#     return redirect('/')