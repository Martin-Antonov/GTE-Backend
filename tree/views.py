import base64

import time

import PIL
from PIL import Image
from django.core.files.base import ContentFile
# Create your views here.
from django.utils import timezone
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from gte_backend.settings import MEDIA_ROOT
from tree.models import Tree


@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
def save_tree(request):
    title = request.POST.get('title')
    tree_json = request.POST.get('tree_json')
    millis = int(round(time.time() * 1000))
    new_tree = Tree.objects.create(
        title=title,
        date=timezone.now(),
        tree_json=tree_json,
        user=request.user
    )

    screenshot = request.POST.get('screenshot')
    new_img = base64.b64decode(screenshot)
    new_img = ContentFile(new_img, "screenshots/" + str(request.user.id) + "_" + str(millis) + '.jpg')
    img_name = new_tree.user.username + "_" + str(millis)
    img = Image.open(new_img).convert('RGB')
    width, height = img.size
    new_width = width / 3
    new_height = height / 3
    img = img.resize((int(new_width), int(new_height)), PIL.Image.ANTIALIAS)
    img.save(MEDIA_ROOT + '/optimized_screenshots/' + str(img_name) + '.jpg', 'JPEG',
                        quality=90,
                        optimize=True, progressive=True)

    new_tree.screenshot_url = "/media/optimized_screenshots/" + img_name + '.jpg'
    new_tree.save()
    return Response({
        "message": "You have successfully saved your tree."
    }, status=status.HTTP_200_OK)
