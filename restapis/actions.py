#!/usr/bin/env python
# Author: ncmadhu@gmail.com


import json
import traceback
from flask import abort, jsonify
from implementation import *
from flask_restful import Resource, reqparse


class Actions(Resource):


    def __init__(self):
        
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
                    response = getactionone()
                elif action == 'getactiontwo':
                    response = getactiontwo()
                elif action == 'getactionthree':
                    response = getactionthree()
                return jsonify(response)
            except:
                abort(500)
        else:
            abort(404)
            
            
    def post(self, action):
            
        """
        parse the json body using request parser
        """
        
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('arg1', type=str, required=False,
                                   help='Argument one of type string',
                                   location='json')
        self.reqparse.add_argument('arg2', type=list, required=False,
                                   help='Argument two of type List',
                                   location='json')
    
        """
        implementation for post 
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
                    response = postactionone(args['arg1'],args['arg2'])
                elif action == 'postactiontwo':
                    response = postactiontwo(args['arg1'],args['arg2'])
                elif action == 'postactionthree':
                    response = postactionthree(args['arg1'],args['arg2'])
                return jsonify(response)
            except:
                abort(500)
        else:
            abort(404)
            
            
    def delete(self, action):
    
        """
        implementation for delete 
        """
    
        implemented_actions = [
            'deleteactionone',
            'deleteactiontwo',
            'deleteactionthree'
        ]
        
        if action in implemented_actions:
            try:
                if action == 'deleteactionone':
                    response = deleteactionone()
                elif action == 'deleteactiontwo':
                    response = deleteactiontwo()
                elif action == 'deleteactionthree':
                    response = deleteactionthree()
                return jsonify(response)
            except:
                abort(500)
        else:
            abort(404)
            
            
    def put(self, action):
    
        """
        parse the json body using request parser
        """
        
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('arg1', type=str, required=False,
                                   help='Argument one of type string',
                                   location='json')
        self.reqparse.add_argument('arg2', type=list, required=False,
                                   help='Argument two of type List',
                                   location='json')
    
        """
        implementation for put 
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
                    response = putactionone(args['arg1'],args['arg2'])
                elif action == 'putactiontwo':
                    response = putactiontwo(args['arg1'],args['arg2'])
                elif action == 'putactionthree':
                    response = putactionthree(args['arg1'],args['arg2'])
                return jsonify(response)
            except:
                abort(500)
        else:
            abort(404)
            
