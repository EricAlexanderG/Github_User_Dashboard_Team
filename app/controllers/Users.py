"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from flask import Flask, render_template, g

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

    # load registration page
    def register(self):
        return self.load_view('user/register.html')
    # actually register, set up a session 

    def bandwagon(self):
        session['name'] = request.form['first_name']
        return redirect ("/users/register")

    # load page for editing the user
    def edit_users(self):
        return self.load_view('edit_user.html')

    def log(self):
        return self.load_view('signin.html')