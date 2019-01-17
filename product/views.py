from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'productCatalog.html')

def detail(request):
	return render(request, 'detail.html')

