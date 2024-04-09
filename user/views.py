from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import *
from user.permissions import *
from user.serializers import *


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    # permission_classes = (IsOwnerOrReadOnly,  )

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username=username)    
    
class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def list(self, request, username=None):
        user = User.objects.filter(username=username).get()
        user_data = UserData.objects.filter(user_id=user.id).first()
        user_skills = UserSkills.objects.filter(user_id=user.id).first()
        user_exp = UserExperience.objects.filter(user_id=user.id).first()

        user_serializer = UsersSerializer(user)
        user_data_serializer = UserDataSerializer(user_data) if user_data else None
        user_skills_serializer = UserSkillsSerializer(user_skills) if user_skills else None
        user_exp_serializer = UserExperienceSerializer(user_exp) if user_exp else None

        data = {
            'user': user_serializer.data,
            'user_data': user_data_serializer.data if user_data_serializer else None,
            'user_skills': user_skills_serializer.data if user_skills_serializer else None,
            'user_experience': user_exp_serializer.data if user_exp_serializer else None,
        }

        return Response(data)

class UserDataByUserIdViewSet(viewsets.ModelViewSet):
    serializer_class = UserDataSerializer
    def get_queryset(self):
        return UserData.objects.filter(user_id=self.request.user)    

class UserSkillsViewSet(viewsets.ModelViewSet):
    queryset = UserSkills.objects.all()
    serializer_class = UserSkillsSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class UserSkillsByUserIdViewSet(viewsets.ModelViewSet):
    serializer_class = UserSkillsSerializer
    def get_queryset(self):
        return UserSkills.objects.filter(user_id=self.request.user)     

class UserExperienceViewSet(viewsets.ModelViewSet):
    queryset = UserExperience.objects.all()
    serializer_class = UserExperienceSerializer  
    permission_classes = (IsOwnerOrReadOnly, )

class UserExperienceByUserIdViewSet(viewsets.ModelViewSet):
    serializer_class = UserExperienceSerializer
    def get_queryset(self):
        return UserExperience.objects.filter(user_id=self.request.user)  
       

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer 

class PortfolioGetByUserIdViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioByUserIdSerializer
    def get_queryset(self):
        return Portfolio.objects.filter(user_id=self.request.user)  

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
     
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer 

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer 
     
class TextFieldViewSet(viewsets.ModelViewSet):
    queryset = TextField.objects.all()
    serializer_class = TextFieldSerializer  

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer  
  
class SphereViewSet(viewsets.ModelViewSet):
    queryset = Sphere.objects.all()
    serializer_class = SphereSerializer  

class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer    
    