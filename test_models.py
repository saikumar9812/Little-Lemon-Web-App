# test_models.py
from django.test import TestCase
from .models import Menu

class MenuModelTests(TestCase):

    def test_menu_creation(self):
        # Test creating a menu item
        menu_item = Menu.objects.create(name="Pizza", price=10.00)
        self.assertEqual(menu_item.name, "Pizza")
        self.assertEqual(menu_item.price, 10.00)

    def test_menu_name_length(self):
        # Test the length of the menu item's name field
        menu_item = Menu.objects.create(name="Pasta", price=15.00)
        self.assertTrue(len(menu_item.name) <= 100, "Name is too long")

    def test_menu_price(self):
        # Test if price is stored correctly and is a positive number
        menu_item = Menu.objects.create(name="Burger", price=12.50)
        self.assertGreater(menu_item.price, 0, "Price should be greater than zero")
