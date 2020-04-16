#!/usr/bin/env python3

import connexion

from openapi_server import encoder

#####
import logging
from logging.config import dictConfig
import yaml
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
import dns
## https://github.com/mongodb/mongo-python-driver/commit/62400e548db8e02e82afa77b9014d21e47ed2f7c
## query() got an unexpected keyword argument 'lifetime'
## pip3 install dnspython==1.16.0



def main():
    app = connexion.App(__name__, specification_dir='./openapi_server/openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'OpenAPI BsvContent'},
                pythonic_params=True)
    with open("./openapi_server/log_config.yaml", "r") as f: # 読み込み
        conf_file = yaml.safe_load(f.read()) # yaml.loadは使わない（脆弱性アリ）

        logging.config.dictConfig(conf_file) # 設定の完了
    #app.app.config.from_envvar('OPENAPI_FLASK_CONFIG_FILE')
    app.app.config.from_pyfile("./openapi_server/config.py")
    print(app.app.config)
    ## https://stackoverrun.com/ja/q/11355897
    # must need packagename
    app.app.config.from_object('openapi_server.config.DevelopmentConfig')
    app.app.config["MONGO_URI"] = "mongodb+srv://" + app.app.config['BSVCONTENTSERVER_MONGODB_USER'] + ":" + app.app.config['BSVCONTENTSERVER_MONGODB_PASS'] + "@cluster0-xhjo9.mongodb.net/test?retryWrites=true&w=majority"

    # bootstrap = Bootstrap(app)
    # mongo = PyMongo(app)

    app.run(port=8080)

if __name__ == '__main__':
    main()
