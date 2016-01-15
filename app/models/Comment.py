
from system.core.model import Model

class Comment(Model):
    def __init__(self):
        super(Comment, self).__init__()

    def create_comment(self, message_id, comment_info):
        pass
    def destroy_comment(self, comment_id):
        pass
