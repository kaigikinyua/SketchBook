from django.shortcuts import render,render_to_response
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'Home/home.html')
def homepage(request):
	return render(request,'Home/home.html')
def trailers(request):
	return render(request,'Home/trailers.html')