# Django User Management

Start development environment:
>docker-compose up --build

First go to http://localhost/admin and access with default credentials:
* User: test
* Password: test

Then go to http://localhost/admin/user_management/customuser/add/
and create your admin user, your email must be a valid google account
to enable login with google auth.

Now you can logout from the default test admin user:
http://localhost/admin/logout

Then you can login with your google account
http://localhost/auth/login/google-oauth2

And manage user with CRUD operations over the navigable REST-API:

LIST and POST: http://localhost/v1/rest/users
RETRIEVE, PUT and DELETE: http://localhost/v1/rest/users/<user_id>

* You can only PUT or DELETE users created by you.