from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import requests

from tutorial.quickstart import serializers
from tutorial.quickstart.models import ChuckNorrisJoke


CHUCK_NORRIS_JOKE_URL = 'https://api.chucknorris.io/jokes/random'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChuckNorrisJokeViewSet(viewsets.ModelViewSet):
    queryset = ChuckNorrisJoke.objects.all()
    serializer_class = serializers.ChuckNorrisJokeSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def get_chuck_norris_joke(request: Request) -> Response:
    # get a new Chuck Norris joke
    request_api_chuck = requests.get(CHUCK_NORRIS_JOKE_URL)
    # if returned status code is 200, then save the joke and return the response
    if request_api_chuck.status_code == status.HTTP_200_OK:
        request_api_chuck_value = dict(request_api_chuck.json())
        new_joke = ChuckNorrisJoke(id=request_api_chuck_value['id'],
                                   url=request_api_chuck_value['url'],
                                   value=request_api_chuck_value['value'])
        new_joke.save()
        return Response({'value': request_api_chuck_value['value']}, status.HTTP_200_OK)
    else:
        return Response(request_api_chuck.json(), request_api_chuck.status_code)
