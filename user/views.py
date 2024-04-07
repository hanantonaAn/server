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
    permission_classes = (IsOwnerOrReadOnly,  )

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
    