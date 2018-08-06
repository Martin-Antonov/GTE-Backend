from django.conf.urls import url

from bimatrix_solver.views import solve_game

urlpatterns = [
    url(r'^$', solve_game, name="solve_game")
]