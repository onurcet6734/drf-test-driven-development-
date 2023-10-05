from decimal import Decimal
from django.test import TestCase
from .models import MenuItem
from category.models import Category
import tempfile
from PIL import Image
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MenuModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Kahveler")
        self.menu_item = MenuItem.objects.create(
            name="Test Ürün",
            description="Bu bir test ürünüdür.",
            price=Decimal("10.99"),
            category=self.category
        )

    def test_menu_item_exist(self):
        item_count = MenuItem.objects.count()
        self.assertEqual(item_count, 1)

    def test_menu_item_attributes(self):
        menu_item = MenuItem.objects.get(id=1)
        self.assertEqual(menu_item.name, "Test Ürün")
        self.assertEqual(menu_item.description, "Bu bir test ürünüdür.")
        self.assertEqual(menu_item.price, Decimal("10.99"))  

    def test_menu_item_str_representation(self):
        menu_item = MenuItem.objects.get(id=1)
        expected_str = f"{menu_item.name}"  
        self.assertEqual(str(menu_item), expected_str)

    def test_read_menu_item(self):
        menu_item = MenuItem.objects.get(id=self.menu_item.id)
        self.assertEqual(menu_item.name, "Test Ürün")

    def test_update_menu_item(self):
        updated_menu_item = MenuItem.objects.get(id=self.menu_item.id)
        updated_menu_item.name = "Güncellenmiş Ürün"
        updated_menu_item.save()

        self.assertEqual(updated_menu_item.name, "Güncellenmiş Ürün")

    def test_delete_menu_item(self):
        menu_item_to_delete = MenuItem.objects.get(id=self.menu_item.id)
        menu_item_to_delete.delete()
        self.assertEqual(MenuItem.objects.count(), 0)

class MenuItemImageUploadTest(APITestCase):
    def setUp(self):
        self.menu_item = MenuItem.objects.create(
            name="Test Item",
            description="Test Description",
            price=10.99,
            category=Category.objects.create(name="Test Category"),
        )

    def tearDown(self):
        self.menu_item.image.delete()

    def test_recipe_image_upload(self):
        "Test to upload a valid image."
        with tempfile.NamedTemporaryFile(suffix=".png") as ntf:
            img = Image.new('RGB', (100, 100))
            img.save(ntf, format="PNG")
            ntf.seek(0)
            url = f'http://127.0.0.1:5555/menu/1.png'
            file_data = {'image': ntf}
            response = self.client.post(url, file_data, format="multipart")
        
        self.menu_item.refresh_from_db()
        self.assertTrue(self.menu_item.image.url.startswith('/menu'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_image_payload(self):
        "Test with an invalid image payload."
        payload = {'image': 'bad bad'}
        url = f'http://127.0.0.1:5555/menu/2.png'
        response = self.client.post(url, payload, format="multipart")
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



#ekleme -> 302
#güncelleme -> 302
#silme -> 302