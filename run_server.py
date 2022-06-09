# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""
import build
from ssl import SSLContext
from flask import Flask,render_template
# définir le message secret
SECRET_MESSAGE = "lightningmcqueen" # A modifier
app = Flask(__name__)


RESSOURCE_DIR="resources/"
SERVER_PRIVATE_KEY_FILENAME=RESSOURCE_DIR + "server-private-key.pem"
SERVER_PUBLIC_KEY_FILENAME=RESSOURCE_DIR+ "server-public-key.pem"

@app.route("/")
def get_secret_message():
    return render_template('index.html',secret_message=SECRET_MESSAGE) 



if __name__ == "__main__":
    # HTTP version
    #app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    context = (SERVER_PUBLIC_KEY_FILENAME,SERVER_PRIVATE_KEY_FILENAME)
    app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=context)
    # A compléter  : nécessité de déplacer les bons fichiers vers ce répertoire
   
