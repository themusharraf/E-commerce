from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

# Create your tests here.
class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('usersapp:signup'),
            data = {
                'first_name':'Rashid',
                'username':'admin',
                'email':'a@gmail',
                'password1': 'chalamulla',
                'password2': 'chalamulla',
            }
        )
        user = CustomUser.objects.get(username='admin')
        self.assertEqual(user.first_name,'Rashid')
        self.assertEqual(user.email,'a@gmail.com')
        self.assertTrue(user.check_password('chalamulla'))

        second_response = self.client.get('/users/profile/admin')
        self.assertEqual(second_response.status_code,200)

        #login
        self.client.login(username='admin',password='chalamulla')

        third_response = self.client.post(
            reverse('usersapp:update'),
            data={
                'username':'admin1',
                'first_name':'Admin1',
                'last_name':'Adminov',
                'email':'aaa@aaa.aaa',
                'phone_number':'+998991234567',
                'tg_username':'username1',
                }
        )
        user = CustomUser.objects.get(username='admin1')
        self.assertEqual(user.phone_number,'+998991234567')
        self.assertEqual(user.first_name,'Admin1')
        self.assertNotEqual(user.first_name,'Rashid')
        self.assertEqual(third_response.status_code,302)