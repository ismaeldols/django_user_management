# Django User Management

* For Google authentication you need to generate google api-keys for oauth2: https://console.developers.google.com/
1. Create a proyect
2. create credentials selecting "Oauth client ID" in "Create credentials" menu
3. Select web application and fill required data with redirect URIS: 	http://localhost/auth/complete/google-oauth2/ and 
http://localhost/admin/admin_sso/assignment/end/

redirect URIs:

4. Click on create button and a key and secret will be generate
5. Google includes authentication with OAuth 2 through its Google + API, so we need to enable it. Go to APIs & Services and click on Enable APIs and Services button. Then, search for Google+ API and enable it.
6. Congure the proyect, edit the variables DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID, DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET, SOCIAL_AUTH_GOOGLE_OAUTH2_KEY and SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET on django_user_management/setting.py




### Start development environment:
$ docker-compose up --build

### Run unit tests: (need development environment running)
$ docker-compose exec web python manage.py test

### Use
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

LIST and POST: http://localhost/manage/v1/rest/users
RETRIEVE, PUT and DELETE: http://localhost/manage/v1/rest/users/<user_id>

* You can only PUT or DELETE users created by your admin user.
