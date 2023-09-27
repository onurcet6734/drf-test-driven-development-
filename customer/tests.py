from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from customer.models import Customer
from django.urls import reverse
import json

def populate_customer_detail_url(customer_id):
    return reverse("customer:customer-detail", kwargs={"pk": customer_id})

class CustomerTests(APITestCase):

    url_listCreate = reverse("customer:customer-list")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "admin"
        self.password = "1234"
        self.user = User.objects.create_user(username= self.username, password=self.password)
        self.test_jwt_authentication()

    def test_jwt_authentication(self):
        response = self.client.post(self.url_login, data = {"username": self.username, "password": self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ self.token)

    def test_create_customer(self):
        response = self.client.post(self.url_listCreate, customer_data = {'name': 'Admin',"user": self.user.id}, format='json')
        self.assertEqual(201, response.status_code)

    def test_authentication_required(self):
        self.client.credentials()
        response = self.client.get('/customer/list-create', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_list_customers(self):
        response = self.client.post(self.url_listCreate, customer_data = {'name': 'Admin',"user": self.user.id}, format='json')
        response = self.client.get(self.url_listCreate, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        

    def test_update_customer(self):
          customer_data = {'name': 'Admin3'}
          updateDelete_url = reverse("customer:customer-detail", kwargs={"pk": Customer.objects.create(name="Admin", user=self.user).pk})
          response = self.client.put(updateDelete_url, customer_data, format='json')
          self.assertEqual(200, response.status_code)

    def test_delete_customer(self):
        customer = Customer.objects.create(name="Admin", user=self.user)
        updateDelete_url = populate_customer_detail_url(customer.pk)
        response = self.client.delete(updateDelete_url)
        self.assertEqual(204, response.status_code)
