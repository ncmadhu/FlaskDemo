from flask import Flask
from flask.ext.restful import Api

app = Flask(__name__, static_url_path='')
api = Api(app)

def registerURLs():
    """
    Register version 1 URLS
    """
    registerUrlv1(api)
    
    """
    Register version 2 URLS
    """
    registerUrlv2(api)
    
    
def registerUrlv1(api):
    """
    Registering Version 1 URLS
    """
    pass
    
    
def registerUrlv2(api):
    """
    Registering Version 2 URLS
    """
    pass
    
    
def main():
    """
    Run Flask Rest server
    """
    app.run(debug=True, host='0.0.0.0', port=4545)
    

if __name__ == '__main__':
    main()
