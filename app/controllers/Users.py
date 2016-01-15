"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

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