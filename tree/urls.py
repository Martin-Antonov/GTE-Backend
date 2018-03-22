from django.conf.urls import url

from tree.views import save_tree

urlpatterns = [
    url(r'^save/', save_tree, name="save_tree"),
]