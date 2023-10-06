from decimal import Decimal
from django.test import TestCase
from .models import MenuItem
from category.models import Category
from django.core.files.uploadedfile import SimpleUploadedFile
import os



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


class MenuItemTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def tearDown(self):
        self.category.delete()

    def test_image_upload(self):
        image_path = os.path.join(os.path.dirname(__file__),'image.png')
        with open(image_path, 'rb') as image_file:
            image = SimpleUploadedFile("image.png", image_file.read(), content_type="image/png")

        menu_item = MenuItem.objects.create(
            name="Test Item",
            description="Test Description",
            price=10.99,
            category=self.category,
            image=image  
        )

        saved_menu_item = MenuItem.objects.get(pk=menu_item.pk)
        self.assertTrue(saved_menu_item.image.name.startswith('menu/'))
        

    def test_image_upload_blank(self):
    
        menu_item = MenuItem.objects.create(
            name="Test Item",
            description="Test Description",
            price=10.99,
            category=self.category,
        )
        image_exists = MenuItem.objects.filter(pk=menu_item.pk, image=None).exists()  
        self.assertFalse(image_exists)

