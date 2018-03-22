from django.conf.urls import url

from general_information.views import get_website_information

urlpatterns = [
    url(r'^getinfo/', get_website_information, name="website_information")
]