from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate

from .models import CustomUser


VERSION = 'v1'
REST_BASE_PATH = '/manage/{version}/rest/'.format(version=VERSION)


class UserManagementAPITestCase(TestCase):

    def setUp(self):
        self.admin_user_1 = CustomUser.objects.create_superuser(username='admin1',
                                                                email='admin1@test.com',
                                                                password='test',
                                                                iban='DE89370400440532013000')
        self.admin1_client = APIClient()
        self.admin1_client.force_authenticate(user=self.admin_user_1)

        self.admin_user_2 = CustomUser.objects.create_superuser(username='admin2',
                                                                email='admin2@test.com',
                                                                password='test',
                                                                iban='CH9300762011623852957')
        self.admin2_client = APIClient()
        self.admin2_client.force_authenticate(user=self.admin_user_2)

        self.normal_user = CustomUser.objects.create_user(username='user1',
                                                          email='user1@test.com',
                                                          password='test',
                                                          iban='ES9000246912501234567891')
        self.normal_user_client = APIClient()
        self.normal_user_client.force_authenticate(user=self.normal_user)

    def test_api(self):

        # LIST USERS

        path = REST_BASE_PATH + 'users/'

        # Admin users can view
        for client in (self.admin1_client, self.admin2_client):
            response = client.get(path=path)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.data), CustomUser.objects.count())

        response = self.normal_user_client.get(path=path)
        self.assertEqual(response.status_code, 403)

        # CREATE USERS

        path = REST_BASE_PATH + 'users/'

        num_of_users = CustomUser.objects.count()

        # admin1 user can create users
        data_user2 = {
                'username': 'user2',
                'email': 'user2@test.com',
                'iban': 'ES6000491500051234567892'
        }

        response = self.admin1_client.post(path=path, data=data_user2)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(num_of_users + 1, CustomUser.objects.count())

        # admin2 user can create users
        data_user3 = {
                'username': 'user3',
                'email': 'user3@test.com',
                'iban': 'ES7100302053091234567895'
            }

        response = self.admin2_client.post(path=path, data=data_user3 )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(num_of_users + 2, CustomUser.objects.count())

        # normal user cannot create users
        data_user4 = {
                'username': 'user4',
                'email': 'user4@test.com',
                'iban': 'ES1720852066623456789011'
            }

        response = self.normal_user_client.post(path=path, data=data_user4)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(num_of_users + 2, CustomUser.objects.count())

        # UPDATE USERS

        user2 = CustomUser.objects.get(username='user2')
        path = REST_BASE_PATH + 'users/' + str(user2.id) + '/'

        new_data_user2 = {
            'username': 'user2',
            'email': 'suser2@test.com',
            'iban': 'ES6621000418401234567891',
        }

        # normal user cannot update
        response = self.normal_user_client.put(path=path, data=new_data_user2)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(user2.iban, 'ES6000491500051234567892') # original iban

        # admin2 user (that not created it) cannot update
        response = self.admin2_client.put(path=path, data=new_data_user2)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(user2.iban, 'ES6000491500051234567892')  # original iban

        # admin1 user (that created it) can update
        response = self.admin1_client.put(path=path, data=new_data_user2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CustomUser.objects.get(username='user2').iban, 'ES6621000418401234567891')  # new iban

        # RETRIEVE USER

        user2 = CustomUser.objects.get(username='user2')
        path = REST_BASE_PATH + 'users/' + str(user2.id) + '/'

        # Admin users can retrieve user
        for client in (self.admin1_client, self.admin2_client):
            response = client.get(path=path)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['iban'], user2.iban)

        # Normal user cannot retrieve user
        response = self.normal_user_client.get(path=path)
        self.assertEqual(response.status_code, 403)

        # DELETE USER

        user2 = CustomUser.objects.get(username='user2')
        path = REST_BASE_PATH + 'users/' + str(user2.id) + '/'

        # normal user cannot delete
        response = self.normal_user_client.delete(path=path)
        self.assertEqual(response.status_code, 403)

        # admin2 user (that not created it) cannot delete
        response = self.admin2_client.delete(path=path)
        self.assertEqual(response.status_code, 403)

        # admin1 user (that created it) can delete
        response = self.admin1_client.delete(path=path)
        self.assertEqual(response.status_code, 204)
