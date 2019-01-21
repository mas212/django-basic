from django.shortcuts import render

# Create your views here.

def index(request):
	contex = {
		'judul' : 'data python',
		'nav' : [
			['/', 'Home'],
			['/items', 'Items'],
			['/product', 'Product'],
			['/member', 'Member']
		]
	}
	return render(request, 'ui/index.html', contex)
