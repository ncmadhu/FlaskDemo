#!/usr/bin/env python
# Author: ncmadhu@gmail.com

from restapis import Actions
from api import constants

def registerUrls(api):

    """
    Register the urls supported in version one
    # POST:    https://server:port/flaskdemo/api/v1.0/apione
    """
    
    version = 'v1.0'
    
    version_url = constants.base_url + version
    api.add_resource(ActionsV1, version_url + '/<string:action>')
    
    
class ActionsV1(Actions):
    """
    override the methods you want to override in version 1 from base version
    """
    pass
    
    