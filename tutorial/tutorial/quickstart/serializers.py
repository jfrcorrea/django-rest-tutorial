from django.contrib.auth.models import User, Group
from rest_framework import serializers

from tutorial.quickstart.models import ChuckNorrisJoke


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ChuckNorrisJokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChuckNorrisJoke
        fields = ['id', 'url', 'value']
