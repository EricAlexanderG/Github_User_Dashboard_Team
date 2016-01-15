
from system.core.router import routes


routes['default_controller'] = 'Welcome'

routes['GET']['/users/register'] = 'Users#register'

routes['/users/edit'] = 'Welcome#edit_users'

routes['POST']['/users/bandwagon'] = "Users#bandwagon"
