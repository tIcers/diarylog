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

def topic(request,topic_id):
	"""Show a single topics and all its entries"""
	topic = Topic.objects.get(id =topic_id)
	entries = topic.entry_set.order_by('-date_added') # revrse order
	context = {'topic':topic,'entries': entries}
	return render(request, 'learning_logs/topic.html', context)