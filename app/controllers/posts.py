from system.core.controller import *

class Post(Controller):
	def __init__(self, action):
		super(Post, self).__init__(action)

	def create(self):
		post = request.form['message']
		return redirect("?????")

	def delete(self):
		delete = request.form["delete"]
		return redirect("?????")