"""Define URL patterns for learning_logs"""

from django.conf.urls import url 
from . import views

urlpatterns = [
	#home page
	url(r'^$', views.index, name ='index')
]
