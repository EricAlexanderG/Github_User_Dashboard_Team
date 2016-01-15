
from system.core.controller import *

class Sessions(Controller):
    def __init__(self, action):
        super(Sessions, self).__init__(action)

    def index(self):

        return self.load_view('index.html')

    def create(self):
        new_user= {
        "email" : request.form['email'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "password" : request.form['password'],
        "cpassword" : request.form['cpassword']
        }
        #assume user posts user_data
        #pass data into MOdel
        user_info=self.models['User'].set_new_user(new_user)

        if user_info ['alreadyuser?'] == True:
            return redirect('/login/success')
        else:
            for message in user_info['errors']
                flash(message, 'bankoferrors')
            return redirect('/')


        return self.load_view('edit_user.html')

    def login(self):
        login = {
        "email" : request.form['email'],
        "password" : request.form['password']
        }

        user_check=self.models['User'].check_user_login(login)

        if user_check ['loginstatus'] == True
            flash('You are logged in, NERD.')
        return redirect('/login/success')

    def successlogin(self):

        return self.load_view('User_Dashboard.html')


    def logout(self):

        session.clear()
        return redirect('/')

        return self.load_view('index.html')
