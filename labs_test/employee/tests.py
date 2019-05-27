import json
from django.test import TestCase
from employee.models import Employee
from django.urls import reverse
from rest_framework.test import APITestCase
from employee.serializers import EmployeeSerializer

class EmployeeListCreateAPIViewTestCase(APITestCase):
    url_list = reverse("employee:employee-list")

    def test_create_employee(self):
        response = self.client.post(self.url_list, {"name": "test", "email": "teste@test.com", "department": "test"})
        self.assertEqual(201, response.status_code)

    def test_create_employee_invalid_email(self):
        response = self.client.post(self.url_list, {"name": "test", "email": "teste", "department": "test"})
        self.assertEqual(400, response.status_code)

    def test_create_employee_invalid_name(self):
        response = self.client.post(self.url_list, {"name": "", "email": "teste@test.com", "department": "test"})
        self.assertEqual(400, response.status_code)

    def test_create_employee_invalid_department(self):
        response = self.client.post(self.url_list, {"name": "test", "email": "teste@test.com", "department": ""})
        self.assertEqual(400, response.status_code)
  
    def test_get_employee(self):
        Employee.objects.create(name="test", email="test@test.com.br", department="test")
        response = self.client.get(self.url_list)
        self.assertTrue(len(json.loads(response.content)) == Employee.objects.count())

    def test_employee_object_update(self):
        emp = Employee.objects.create(name="test", email="test@test.com.br", department="test")
        url_detail = reverse('employee:employee-detail', kwargs={'pk': emp.id})
        response = self.client.put(url_detail, {"name": "teste updated", "email": "test@test.com.br", "department": "test"})
        response_data = json.loads(response.content)
        employee = Employee.objects.get(id=emp.id)
        self.assertEqual(response_data.get("name"), employee.name)

    def test_employee_object_delete(self):
        emp = Employee.objects.create(name="test", email="test@test.com.br", department="test")
        url_detail = reverse('employee:employee-detail', kwargs={'pk': emp.id})
        response = self.client.delete(url_detail)
        self.assertEqual(204, response.status_code)