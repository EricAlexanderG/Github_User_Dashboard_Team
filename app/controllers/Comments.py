
from system.core.controller import *

class Comments(Controller):
    def __init__(self, action):
        super(Comments, self).__init__(action)

    def index(self):
        return self.load_view('comments.html')

    def new_comment(self, message_id):
        self.models['Comment'].create_comment(message_id, request.form)
        return redirect('/')

