from multiprocessing import context
from django.shortcuts import render

from .models import Topic, Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm,EntryForm

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

def new_topic(request):
	"""Add a new topic"""
	if request.method !="POST":
		#no data submitted; create a blank form 
		form = TopicForm()
	else:
		#POst data submitted; process data
		form = TopicForm(request.POST)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('topics'))
	
	context = {'form':form}
	

	return render(request,'learning_logs/new_topic.html',context)

def new_entry(request,topic_id):
	"""Add a new entry for a spefic topic"""
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('topics',args=[topic_id]))
			# include the path of urls and list containing any args that need to be included in url

	context = {'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request, entry_id):
	"""Edit an existing entry"""
	entry = 
