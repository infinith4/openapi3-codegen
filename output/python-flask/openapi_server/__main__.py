#!/usr/bin/env python3

import connexion

from openapi_server import encoder

#####
# from flask_bootstrap import Bootstrap
# from flask_pymongo import PyMongo
# import dns
## https://github.com/mongodb/mongo-python-driver/commit/62400e548db8e02e82afa77b9014d21e47ed2f7c
## query() got an unexpected keyword argument 'lifetime'
## pip3 install dnspython==1.16.0



def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'OpenAPI BsvContent'},
                pythonic_params=True)
    app.config.from_object('config.DevelopmentConfig')
    app.config.from_envvar('FLASK_CONFIG_FILE')
    # app.config["MONGO_URI"] = "mongodb+srv://" + app.config['BSVCONTENTSERVER_MONGODB_USER'] + ":" + app.config['BSVCONTENTSERVER_MONGODB_PASS'] + "@cluster0-xhjo9.mongodb.net/test?retryWrites=true&w=majority"

    # bootstrap = Bootstrap(app)
    # mongo = PyMongo(app)

    app.run(port=8080)
