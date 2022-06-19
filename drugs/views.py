from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .get_db import read_all, read_by_title
from rest_framework.request import Request
from django.http import JsonResponse


# Create your views here.
@api_view(['GET'])
def get_drug(request):
    # query parameter로 받은 title 추출
    title = request.GET['title']
    print('title: ', title)
    result = read_by_title(title)
    print('result: ', result)
    if result:
        return JsonResponse(status=200, data=result, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return Response(status=413)
