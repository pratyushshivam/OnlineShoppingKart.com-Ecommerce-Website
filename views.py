from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
    # return HttpResponse("Index Blog") keep in mind that index.html is inside blog so we use blog/index.html