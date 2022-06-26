"""Define URL patterns for learning_logs"""

from django.urls import path
from . import views

urlpatterns = [
	#home page
	path('', views.index, name ='index'),

	#show all topics
	path('topics/',views.topics, name='topics'),

	#Detail page for single topic
	path('topics/<int:topic_id>',views.topic, name='topic')
	
]
