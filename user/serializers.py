from rest_framework import serializers
from user.keywords import SearchWords
from user.models import * 
import requests
from django.db import transaction
from .models import UserVacancy
from rest_framework_simplejwt.tokens import AccessToken

def fetch_and_save_vacancies(username):
    url = "https://api.hh.ru/vacancies"
    user = User.objects.filter(username=username).get()
    if UserExperience.objects.filter(user_id=user.id).exists():
        experience = UserExperience.objects.filter(user_id=user.id).first()
        exp = experience.experience_years
    else:
        exp = "between1And3" 
    if  UserData.objects.filter(user_id=user.id).exists():       
        userdata = UserData.objects.filter(user_id=user.id).first()
        position = userdata.position
        city = userdata.city
    else:
        position = "Разработчик" 
        city = "Москва"   
    if Portfolio.objects.filter(user_id=user.id).exists():
        port = Portfolio.objects.filter(user_id=user.id).first()
        text = port.portfolio_text
        key = SearchWords(text)
    else:
        text = ""    
        key = ""
    if key == "string": key = ""    
    data = [position, city, key]
    result = ' '.join(data)
    print(result)

    params = {
        "page": 0, 
        "per_page":10,
        "text": result,
        "experience": exp,
        "only_with_salary": True,
        "no_magic": True,

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
                if not UserVacancy.objects.filter(url=vacancy['url']).exists():
                    UserVacancy.objects.create(
                        username=username,
                        hh_id=vacancy['id'],
                        name=vacancy['name'],
                        area=vacancy['area']['name'],
                        salary_from=str(vacancy['salary']['from']),
                        salary_to=str(vacancy['salary']['to']),
                        address=vacancy['address'],
                        url=vacancy['alternate_url'],
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
    # languages = serializers.ListField(child=serializers.CharField())
    # curses = serializers.ListField(child=serializers.CharField())
    
    class Meta:
        model = UserData
        fields = "__all__" 

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']   

class UserSerializerChat(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class UsersSkillsSerializer(serializers.ModelSerializer):
    skills = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = UserSkills
        fields = "__all__" 

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = "__all__"         

class UserDataChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['fullname', 'surname', 'picture', 'status']

class UsersExpSerializer(serializers.ModelSerializer):
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

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVacancy
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

class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = "__all__"        

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = "__all__" 

class SliderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = "__all__"         

class SphereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sphere
        fields = "__all__" 

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = "__all__"                  