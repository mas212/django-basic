from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Feture product ---> jos django</h1>")