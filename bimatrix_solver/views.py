import subprocess

import os
from bimatrix_solver.solver.solve_game import execute
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.
from rest_framework.response import Response

from gte_backend.settings import BASE_DIR


@api_view(["POST"])
@authentication_classes(())
@permission_classes((AllowAny, ))
def solve_game(request):
    game_text = request.POST.get('game_text')
    file = open(os.path.join(BASE_DIR,"bimatrix_solver/solver/example_input/game_to_solve.txt"), "w+")
    file.write(str(game_text))
    file.close()
    result = execute()
    # print(result)
    return Response({"solver_output": result}, status=status.HTTP_201_CREATED)