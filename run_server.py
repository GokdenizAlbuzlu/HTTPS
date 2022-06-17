# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""
from flask import Flask, render_template, redirect, session
from ssl import SSLContext
from flask import request
import logging
from logging.config import dictConfig
import datetime
# définir le message secret
SECRET_MESSAGE = "<h1>lightningmcqueen<h1>" # A modifier

RESSOURCE_DIR="resources/"
SERVER_PRIVATE_KEY_FILENAME=RESSOURCE_DIR + "server-private-key.pem"
SERVER_PUBLIC_KEY_FILENAME=RESSOURCE_DIR+ "server-public-key.pem"

app = Flask(__name__)

fileLogger = logging.getLogger('file')
fileHandler = logging.FileHandler(".\logs\connexions.log")
fileLogger.addHandler(fileHandler)
app.secret_key = 'A_SECRET_KEY'

@app.route("/")
def home():
    return redirect("login")

@app.route("/login" , methods=("GET","POST"))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username == "gokdeniz" and password =="rawan"):
            session['isLoggedIn'] = True
            print("***User is logged in")
            return redirect("secret")
        else:
            session['isLoggedIn'] = False
            return redirect("error")
        
    ip_address = request.remote_addr
    fileLogger.warning(f'{ip_address} had access to login at {datetime.datetime.now()} ')
    return render_template("index.html")

@app.route("/error")
def error():
    return "<h1>mot de passe ou identifiants incorrect !<h1>"

@app.route("/secret")
def get_secret_message():
    if "isLoggedIn" in session:
        if session["isLoggedIn"] != True:
            return redirect("login")
        ip_address = request.remote_addr
        fileLogger.warning(f'{ip_address} had access to secret at {datetime.datetime.now()} ')
        session.pop("isLoggedIn",None)
    else :
         return redirect("login")
    return SECRET_MESSAGE



if __name__ == "__main__":
    # HTTP version
    #app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    context = (SERVER_PUBLIC_KEY_FILENAME,SERVER_PRIVATE_KEY_FILENAME)
  
    app.run(debug = True,ssl_context=context, host="0.0.0.0" ,port=8081)
    # A compléter  : nécessité de déplacer les bons fichiers vers ce répertoire
   
