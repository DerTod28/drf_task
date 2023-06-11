from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

factory = APIRequestFactory()


class DepartmentsAPIViewTests(APITestCase):
    def setUp(self):
        self.u = User.objects.create_superuser(username='admin', password='admin')
        self.u.save()
        self.client = APIClient()
        self.refresh = RefreshToken.for_user(self.u)
        resp = self.client.post("/api/token/", {'username': 'admin', 'password': 'admin'}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_departments_authenticated(self):
        resp = self.client.get('/v1/api/departments/', format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_departments_un_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer ')
        resp = self.client.get('/v1/api/departments/', format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_departments(self):
        data = {
            "name": "Отдел_1",
        }
        resp = self.client.post('/v1/api/departments/', data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)


class EmployeesAPIViewTests(APITestCase):
    def setUp(self):
        self.u = User.objects.create_superuser(username='admin', password='admin')
        self.u.save()
        self.client = APIClient()
        self.refresh = RefreshToken.for_user(self.u)
        resp = self.client.post("/api/token/", {'username': 'admin', 'password': 'admin'}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_employees_authenticated(self):
        resp = self.client.get('/v1/api/employees/', format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_employees_un_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer ')
        resp = self.client.get('/v1/api/employees/', format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_employee_authenticated(self):
        data = {
            "name": "Отдел_1",
        }
        department_id = self.client.post('/v1/api/departments/', data=data, format='json').data['id']

        data = {
            "full_name": "Иванов Иван Алексеевич",
            "position": "Дир",
            "salary": "100000.00",
            "age": 20,
            "department": department_id
        }
        resp = self.client.post('/v1/api/employees/', data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_get_filter_employee_authenticated(self):
        data = {
            "name": "Отдел_1",
        }
        department_id = self.client.post('/v1/api/departments/', data=data, format='json').data['id']
        data = {
            "full_name": "Иванов Иван Алексеевич",
            "position": "Дир",
            "salary": "100000.00",
            "age": 20,
            "department": department_id
        }
        self.client.post('/v1/api/employees/', data=data, format='json')
        resp = self.client.get('/v1/api/employees/', data={"full_name": "ано"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_check_unique_employee_department_authenticated(self):
        data = {
            "name": "Отдел_1",
        }
        department_id = self.client.post('/v1/api/departments/', data=data, format='json').data['id']
        data = {
            "full_name": "Иванов Иван Алексеевич",
            "position": "Дир",
            "salary": "100000.00",
            "age": 20,
            "department": department_id
        }
        self.client.post('/v1/api/employees/', data=data, format='json')
        resp = self.client.post('/v1/api/employees/', data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
