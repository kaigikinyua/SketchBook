from django.urls import path
from . import views
urlpatterns=[
	path('',views.home),
	path('trailers.html',views.trailers),
	path('home.html',views.homepage),
]