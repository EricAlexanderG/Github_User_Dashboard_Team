
from system.core.router import routes

#Controller Routes

#Loads index page
routes['default_controller'] = 'Welcome'

#Loads registration page
routes['GET']['/users/register'] = 'Users#register'

#loads edit user
routes['GET']['/users/edit'] = 'Users#edit_users'

#registers user
routes['POST']['/users/bandwagon'] = "Users#bandwagon"

#goes to login page
routes['GET']['/users/log'] = "Users#log"

# Comments: 
routes['POST']['/comments/new_comment'] = "Comments#new_comment"

# Users: 

routes['POST']['/Users/delete'] = "Users#delete"
routes['POST']['/Users/edit_profile'] = "Users#edit_profile"
routes['POST']['/Users/update'] = "Users#update"
routes['POST']['/Users/change_password'] = "Users#change_password"

# Posts:
routes['POST']['/Posts/create'] = "Posts#create"
routes['POST']['/Posts/delete'] = "Posts#delete"

# Sessions:
routes['POST']['/Sessions/create'] = "Sessions#create"
routes['POST']['/Sessions/login'] = "Sessions#login"
routes['GET']['/Sessions/success'] = "Sessions#successlogin"
routes['POST']['/Sessions/logout'] = "Sessions#logout"

