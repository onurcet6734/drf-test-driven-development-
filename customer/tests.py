from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from customer.models import Customer
from django.urls import reverse
import json
from core.jwt_authentication import authenticate_user 


def populate_customer_detail_url(customer_id):
    return reverse("customer:customer-detail", kwargs={"pk": customer_id})

class CustomerTests(APITestCase):

    url_listCreate = reverse("customer:customer-list")

    def setUp(self):
        self.username = "admin"
        self.password = "1234"
        self.user = User.objects.create_user(username= self.username, password=self.password)
        self.test_jwt_authentication()

    def test_jwt_authentication(self):
        is_authenticated = authenticate_user(self.client, self.username, self.password)
        self.assertTrue(is_authenticated)

    def test_create_customer(self):
        response = self.client.post(self.url_listCreate, customer_data = {'name': 'Admin',"user": self.user.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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
          self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_customer(self):
        customer = Customer.objects.create(name="Admin", user=self.user)
        updateDelete_url = populate_customer_detail_url(customer.pk)
        response = self.client.delete(updateDelete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

