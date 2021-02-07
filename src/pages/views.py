from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello World!</h1>")

	return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
	return render(request, 'contact.html', {})

def about_view(request, *ars, **kwargs):
	my_context = {
		"my_text": "this is about me",
		"my_number": 123,
		"my_list": [134,244,443,444,'abc'],
		"my_html": "<h1>hello world</h1>"
	}

	return render(request, 'about.html', my_context)