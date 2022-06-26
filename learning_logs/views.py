from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(reqest):
	"""the home page for learning log"""
	return render(reqest, 'learning_logs/index.html')

def topics(request):
	"""Show all topics"""
	topics = Topic.objects.order_by('date_added')
	context = {'topic':topics}
	return render(request, 'learning_logs/topics.html',context)

	
