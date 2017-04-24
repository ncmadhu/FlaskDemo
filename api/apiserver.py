#!/usr/bin/env python
# Author: ncmadhu@gmail.com

import os
import sys
from flask import Flask
from flask_restful import Api

# Set system path <PYTHONPATH>

pythonPath = os.path.join(os.getcwd(),"..")
sys.path.append(pythonPath)

app = Flask(__name__, static_url_path='')
api = Api(app)


def registerUrls():
    """
    Register version 1 URLS
    """
    registerUrlsV1(api)
    
    """
    Register version 2 URLS
    """
    registerUrlsV2(api)
    
    
def registerUrlsV1(api):
    """
    Registering Version 1 URLS
    """
    from restapis import actions_v1
    
    actions_v1.registerUrls(api)

    
def registerUrlsV2(api):
    """
    Registering Version 2 URLS
    """
    from restapis import actions_v2
    
    actions_v2.registerUrls(api)
    
    
def main():
    """
    Run Flask Rest server
    """
    registerUrls()
    app.run(debug=True, host='0.0.0.0', port=4545)
    

if __name__ == '__main__':
    main()
