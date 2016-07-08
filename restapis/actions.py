#!/usr/bin/env python
# Author: ncmadhu@gmail.com


import json
import traceback
from flask import abort, jsonify
from restapis.implementation import *
from flask.ext.restful import Resource, reqparse


class Actions(Resource):


    def __init__(self):
        
        """
        parse the json body using request parser
        """
        
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('arg1', type=str, required=False,
                                   help='Argument one of type string',
                                   location='json')
        self.reqparse.add_argument('arg2', type=List, required=False,
                                   help='Argument two of type List',
                                   location='json')
        super(Actions, self).__init__()
        
        
    def get(self, action):
    
        """
        implementation for get
        """
    
        implemented_actions = [
            'getactionone',
            'getactiontwo',
            'getactionthree'
        ]
        
        if action in implemented_actions:
            try:
                if action == 'getactionone':
                    implementation.getactionone()
                elif action == 'getactiontwo':
                    implementation.getactiontwo()
                elif action == 'getactionthree':
                    implementation.getactionthree()
                return jsonify(response)
            except:
                abort(500)
        else:
            abort(404)
            
            
    def post(self, action):
    
        """
        implementation for get
        """
    
        implemented_actions = [
            'postactionone',
            'postactiontwo',
            'postactionthree'
        ]
        
        if action in implemented_actions:
            try:
                args = self.reqparse.parse_args()
                if action == 'postactionone':
                    implementation.postactionone(args['arg1'],args['arg2'])
                elif action == 'postactiontwo':
                    implementation.postactiontwo(args['arg1'],args['arg2'])
                elif action == 'postactionthree':
                    implementation.postactionthree(args['arg1'],args['arg2'])
                return jsonify(response)
            except:
                abort(500)
        else:
            abort(404)
            
            
    def delete(self, action):
    
        """
        implementation for get
        """
    
        implemented_actions = [
            'deleteactionone',
            'deletectiontwo',
            'deletectionthree'
        ]
        
        if action in implemented_actions:
            try:
                if action == 'deleteactionone':
                    implementation.deleteactionone()
                elif action == 'deletectiontwo':
                    implementation.deletectiontwo()
                elif action == 'deletectionthree':
                    implementation.deletectionthree()
                return jsonify(response)
            except:
                abort(500)
        else:
            abort(404)
            
            
    def put(self, action):
    
        """
        implementation for get
        """
    
        implemented_actions = [
            'putactionone',
            'putactiontwo',
            'putactionthree'
        ]
        
        if action in implemented_actions:
            try:
                args = self.reqparse.parse_args()
                if action == 'putactionone':
                    implementation.putactionone(args['arg1'],args['arg2'])
                elif action == 'putactiontwo':
                    implementation.putactiontwo(args['arg1'],args['arg2'])
                elif action == 'putactionthree':
                    implementation.putactionthree(args['arg1'],args['arg2'])
                return jsonify(response)
            except:
                abort(500)
        else:
            abort(404)
            