from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from customsettings.models import CustomSettings
from customsettings.serializer import CustomSettingsSerializer
from tree.models import Tree
from tree.serializer import TreeSerializer
from users.models import GTEUser


@api_view(["POST"])
@authentication_classes(())
@permission_classes((AllowAny, ))
def register_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.POST.get('institution'):
        institution = request.POST.get('institution')
    else:
        institution = None

    new_user = GTEUser.objects.create(
        username=username,
        institution=institution
    )

    new_user.set_password(password)
    new_user.email = username
    new_user.save()

    CustomSettings.objects.create(
        user=new_user,
    )
    # token = Token.objects.create(user=new_user)
    # response = {}
    # response['token'] = token.key

    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes((BasicAuthentication, ))
def login(request):

    if request.user.is_authenticated:
        if Token.objects.filter(user=request.user).count() > 0:
            pass
        else:
            Token.objects.create(user=request.user)

        request.user.last_login = timezone.now()
        request.user.save()

        response = {}
        response['token'] = request.user.auth_token.key
        trees_to_return = Tree.objects.filter(user__username=request.user.username)
        response['trees'] = []
        response['user'] = request.user.username
        for tree in trees_to_return:
            serialized_tree = TreeSerializer(tree, many=False)
            response['trees'].append(serialized_tree.data)

        try:
            user_settings = CustomSettings.objects.get(user__username=request.user.username)
            serialized_user_settings = CustomSettingsSerializer(user_settings, many=False)
            response['settings'] = serialized_user_settings.data

        except CustomSettings.DoesNotExist:
            pass
        return Response(response, status=status.HTTP_200_OK)
    return Response({"message":"User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
@authentication_classes((TokenAuthentication, ))
def logout(request):
    if Token.objects.filter(user=request.user).count() > 0:
        Token.objects.get(user=request.user).delete()
    else:
        pass

    return Response({"message": "User has logged out"}, status=status.HTTP_200_OK)
