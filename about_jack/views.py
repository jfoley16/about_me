#about_jack/views.py

from django.shortcuts import render
#from django.views.generic.base import TemplateViews
from django.http import HttpResponse

# Create your views here.

#class HomePageView(TemplateView):
#	def get(self, request, **kwargs):
#		return render(request, 'index.html', context=None)

def index(request):
	return HttpResponse("Hello, world. You're at the about_jack index.")


