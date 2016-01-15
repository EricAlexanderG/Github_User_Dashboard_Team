from system.core.model import Model

class User(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()
    def show_all_users(self):
        return self.db.query_db("SELECT * FROM users")
    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        data = ['user_id']
        return self.db.query_db(query, data)
    def create_user(self, user):
        # pass data to the query like so
        count=0
        if len(user['first_name']) < 1:
            flash('Invalid password')
            count+=1
        query = "SELECT * FROM users"
        data = self.db.query_db(query)
        if len(data) < 1:
            level = 9
        else:
            level = 1
        query = "INSERT INTO users (email, first_name, last_name, password, user_level, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, NOW(), NOW())"
        data = [user['id'], user['email'], user['first_name'], user['last_name'], user['password'], level]
        return self.db.query_db(query, data)
    def edit_profile(self, user):
        query = "UPDATE users SET email=%s, first_name=%s, last_name=%s, updated_at=NOW() WHERE id = %s"
        data = [user['id'], user['email'], user['first_name'], user['last_name'], user['id']]
        return self.db.query_db(query, data)
    def update_user(self, user):
        query = "UPDATE users SET email=%s, first_name=%s, last_name=%s, user_level=%s, updated_at=NOW() WHERE id = %s"
        data = [user['email'], user['first_name'], user['last_name'], user['user_level'], user['id']]
        return self.db.query_db(query, data)
    def update_password(self, user):
        query = "UPDATE users SET password=%s, updated_at=NOW() where id = %s"
        data = [user['password'], user['user_id']]
        return self.db.query_db(query, data)
