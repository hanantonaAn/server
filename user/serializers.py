from rest_framework import serializers
from user.models import * 

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