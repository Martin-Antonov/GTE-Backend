from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from general_information.models import GeneralInformation
from general_information.serializer import GeneralInformationSerializer


@api_view(["GET"])
def get_website_information(request):
    website_info = GeneralInformation.objects.get()
    serialized = GeneralInformationSerializer(website_info, many=False)
    return Response(serialized.data, status=status.HTTP_200_OK)
