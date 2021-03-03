from django.test import TestCase
from django.urls import reverse
from .models import Developer

class DeveloperModelTests(TestCase):

    def test_save_developer(self):
        dev=Developer(name="Gorge",experience=5,country="Japan")
        dev.save()
        assert dev.name == "Gorge"

    def test_index(self):
        url = reverse('ninjas:index')
        response = self.client.get(url)
        assert response.status_code == 200   

    def test_detail(self):
        dev=Developer(name="Gorge",experience=5,country="Japan")
        dev.save()
        url = reverse('ninjas:detail',args=(dev.id,))
        response = self.client.get(url)
        assert response.status_code == 200   

    def test_negative_detail(self):
        url = reverse('ninjas:detail',args=(4,))
        response = self.client.get(url)
        assert response.status_code == 404 
    
    def test_results(self):
        dev=Developer(name="Gorge",experience=5,country="Japan")
        dev.save()
        url = reverse('ninjas:results',args=(dev.id,))
        response = self.client.get(url)
        assert response.status_code == 200

    def test_negative_results(self):
        url = reverse('ninjas:results',args=(4,))
        response = self.client.get(url)
        assert response.status_code == 404     


class SkillModelsTests(TestCase):
    def test_save_skill(self):
        dev=Developer(name="Gorge",experience=5,country="Japan")
        dev.save()
        dev.skill_set.create(name='coding', level=0)
        dev.skill_set.create(name='Backend', level=0)
        skill=dev.skill_set.all()
        assert skill[0].name == "coding"

    def test_count_skill(self):
        dev=Developer(name="Gorge",experience=5,country="Japan")
        dev.save()
        dev.skill_set.create(name='coding', level=0)
        dev.skill_set.create(name='Backend', level=0)
        assert dev.skill_set.count() == 2    