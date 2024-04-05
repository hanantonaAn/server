from django.contrib import admin

from user.models import User, UserData, UserExperience, UserSkills

admin.site.register(User)
admin.site.register(UserData)
admin.site.register(UserSkills)
admin.site.register(UserExperience)


