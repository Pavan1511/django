from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome_django(request):

	s1 = "<h1>Hello Abcians</h1>"

	s2 = "<h1>Welcome to Django Framework</h1>"

	s3 = (s1,s2)

	return HttpResponse(s3)


