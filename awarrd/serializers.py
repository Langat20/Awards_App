# from rest_framework import serializers
# from .models import Project, Profile,Rating
# from django.contrib.auth.models import User
# from .models import *

# class ProfileSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username') # new
#     class Meta:
#         model = Profile
#         fields = ['name','user', 'profile_picture', 'bio']

# class ProjectSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user')

#     class Meta:
#         model = Project 
#         fields = ['user','title', 'photo', 'url','description', 'date']