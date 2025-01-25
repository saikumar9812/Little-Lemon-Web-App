# test_views.py
from django.test import TestCase
from django.urls import reverse

class ViewTests(TestCase):

    def test_home_view(self):
        # Test that the home page loads with status code 200
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        # Test that the about page loads with status code 200
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
    
    def test_menu_view(self):
        # Test that the menu page loads with status code 200
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Menu Items")

    def test_booking_form_submission(self):
        # Test that a valid booking form submission redirects
        data = {'name': 'John Doe', 'email': 'johndoe@example.com', 'date': '2025-01-30'}
        response = self.client.post(reverse('book'), data)
        self.assertEqual(response.status_code, 302)  # Redirect means successful submission

    def test_booking_form_invalid_submission(self):
        # Test that an invalid booking form shows errors
        data = {'name': '', 'email': 'invalidemail', 'date': ''}
        response = self.client.post(reverse('book'), data)
        self.assertEqual(response.status_code, 200)  # Form should return with errors
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
