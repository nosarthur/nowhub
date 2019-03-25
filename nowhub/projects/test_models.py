from projects.models import Project
from django.test import TestCase
        
class ProjectTests(TestCase):
    def test_saving_and_retrieving_projects(self):
        title1 = '1st Project title'
        description1 = '1st Project description'
        first_project = Project()
        first_project.title = title1
        first_project.description = description1
        first_project.save()

        title2 = '2nd Project title'
        description2 = '2nd Project description'
        second_project = Project()
        second_project.title = title2
        second_project.description = description2
        second_project.save()

        saved_projects = Project.objects.all()
        
        self.assertEqual(saved_projects.count(), 2)

        self.assertEqual(saved_projects[0].title, title1)
        self.assertEqual(saved_projects[1].title, title2)

        self.assertEqual(saved_projects[0].description, description1)
        self.assertEqual(saved_projects[1].description, description2)