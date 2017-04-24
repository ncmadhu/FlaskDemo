#!/usr/bin/env python
# Author: ncmadhu@gmail.com

from restapis.actions import Actions
from api import constants

def registerUrls(api):

    """
    Register the urls supported in version two
    # POST:    https://server:port/flaskdemo/api/v2.0/apitwo
    """
    
    version = 'v2.0'
    
    version_url = constants.base_url + version
    api.add_resource(ActionsV2, version_url + '/<string:action>')
    
    
class ActionsV2(Actions):
    """
    override the methods you want to override in version 2 from base version
    """
    pass
