from django.shortcuts import render

# Create your views here.

def index(reqest):
	"""the home page for learning log"""
	return render(reqest, 'learning_logs/index.html')
	