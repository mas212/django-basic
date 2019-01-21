from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul' : 'PYTHON PROGRAMER EXPERT THE NEXT',
		'kontributor' : 'Hariyanto',
		'benner' : 'item/img/adsvokat.png'
	}
	return render(request, 'item/index.html', context)

def cerita(request):
	context = {
		'judul' : 'cerita programmer experts python',
		'kontributor' : 'mas hari'
	}
	return render(request, 'item/index.html', context)