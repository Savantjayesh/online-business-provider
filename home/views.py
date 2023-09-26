from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
  #  return HttpResponse("this is homepage")
def about(request):
    return render(request,'about.html')
def login1(request):
    return render(request,'login1.html')