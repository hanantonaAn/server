from rest_framework import serializers
from user.models import * 
import requests
from django.db import transaction
from .models import UserVacancy


def fetch_and_save_vacancies():
    url = "https://api.hh.ru/vacancies"
    params = {
        # "text": 
        "page": 0, 
        "per_page": 20 
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        vacancies = data.get('items', [])
        with transaction.atomic():
            for vacancy in vacancies:
                UserVacancy.objects.create(
                    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault()),
                    hh_id=vacancy['id'],
                    name=vacancy['name'],
                    area=vacancy['area']['name'],
                    salary_from=str(vacancy['salary']['from']),
                    salary_to=str(vacancy['salary']['to']),
                    address=vacancy['address'],
                    url=vacancy['url'],
                    company=vacancy['employer']['name'],
                    requirements=vacancy['snippet']['requirement'],
                    responsobility=vacancy['snippet']['responsibility'],
                    scedule=vacancy['schedule']['name'],
                    role=vacancy['professional_roles'][0]['name'] if vacancy['professional_roles'] else None,
                    experience=vacancy['experience']['name']
                )
    else:
        print(f"Ошибка при запросе: {response.status_code}") 

class UserDataSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    languages = serializers.ListField(child=serializers.CharField())
    curses = serializers.ListField(child=serializers.CharField())
    
    class Meta:
        model = UserData
        fields = "__all__" 

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']   

class UsersSkillsSerializer(serializers.ModelSerializer):
    skills = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = UserSkills
        fields = "__all__" 

class DataSerializer(serializers.ModelSerializer):
    languages = serializers.ListField(child=serializers.CharField())
    curses = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = UserData
        fields = "__all__"         

class UsersExpSerializer(serializers.ModelSerializer):
    experience = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = UserExperience
        fields = "__all__" 

class UsersPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"         
class UserSkillsSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    skills = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = UserSkills
        fields = "__all__"   

class UserExperienceSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    experience = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = UserExperience
        fields = "__all__"    

class PortfolioSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Portfolio
        fields = "__all__"  

class PortfolioByUserIdSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Portfolio
        fields = "__all__"          

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"       

class TextFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextField
        fields = "__all__" 

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__" 

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__" 

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__" 

class SphereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sphere
        fields = "__all__" 

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = "__all__"                 