
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from user.views import *
from rest_framework import routers

router = routers.SimpleRouter()

# http://127.0.0.1:8000/api/userdata/
router.register(r'userdata', UserDataViewSet)
router.register(r'userskills', UserSkillsViewSet)
router.register(r'userdata', UserExperienceViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
    # path('api/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)