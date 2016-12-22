"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""
    
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)      

    def test_survival(self):
        """Tests the survival page."""
        response = self.client.get('/survival')
        self.assertContains(response, 'Survival', 3, 200)

    def test_tournament(self):
        """Tests the tournament page."""
        response = self.client.get('/tournament')
        self.assertContains(response, 'Tournament', 3, 200)
        
    def test_groupfight(self):
        """Tests the recovery page."""
        response = self.client.get('/groupfight')
        self.assertContains(response, 'Groupfight', 1, 200)

    def test_fight(self):
        """Tests the fight page."""
        response = self.client.get('/fight')
        self.assertContains(response, 'Fight', 3, 200)

    def test_quest(self):
        """Tests the quest page."""
        response = self.client.get('/quest')
        self.assertContains(response, 'Quest', 3, 200)

    
