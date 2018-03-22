from django.conf.urls import url

from users.views import register_user, login, logout

urlpatterns = [
    url(r'^register/', register_user, name="register_user"),
    url(r'^login/', login, name="login"),
    url(r'^logout/', logout, name="logout")
]