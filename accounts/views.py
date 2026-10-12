from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def sayHi(response):
    return HttpResponse("<h1>Hello everyone</h1>")