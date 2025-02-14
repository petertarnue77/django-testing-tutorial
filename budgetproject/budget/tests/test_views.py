from django.test import TestCase, client
from django.urls import reverse
from budget import views 
from budget.models import Project, Category, Expense
import json

class TestViews(TestCase): 
    def test_project_list_GET(self): 
        client = client() 
        response = client.get(reverse('list')) 
        self.assertEquals(response.status_code, 200) 
        self.assertTemplateUsed(response, 'budget/project-list.html')
        