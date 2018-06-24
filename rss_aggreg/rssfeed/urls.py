from django.conf.urls import url,include
from . import views
from . import forms


urlpatterns=[
	url(r'^search',views.index,name = 'index'),
	url(r'^results',views.results,name = 'results'),
]
