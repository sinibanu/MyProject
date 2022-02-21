from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return HttpResponse(" Congratulations, You have created a web application using django")

@api_view(['GET'])
def firstApi(request):
    message = "Congratulations , you have created an API"
    return Response(message)

