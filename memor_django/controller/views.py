from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RaspSerializer
from .models import Control_words
import mimetypes
import os


# Create your views here.
@api_view(['GET'])
def login_info(request):
    users = Control_words.objects.all()
    serializers = RaspSerializer(users, many= True)
    return Response(serializers.data)

order = 0

@api_view(['POST'])
def get_login(request):
    if request.method == "POST":
        #CREATE
        global order
        order = request.data['user_id']
        print(order)
        serializers = RaspSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
    elif request.method == "GET":
        # READ (LIST) 
        users = Control_words.objects.all()
        serializers = RaspSerializer(users, many= True)
        return Response(serializers.data)


@api_view(['Post'])
def get_image(request):
    dir_path = os.path.dirname(__file__)
    img_path = os.path.join(dir_path,'images/tvmonitor_19_2021-05-29_22_09_37.jpg')
    with open(img_path,'rb') as img:
        mime_type, _ = mimetypes.guess_type(img_path)
        response = HttpResponse(img)
        img.close()
    return response