from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Product
# Create your views here.

def index(request):
    return render(request, 'index.html')
  #  return HttpResponse("this is homepage")
def about(request):
    return render(request,'about.html')
def login1(request):
    return render(request,'login1.html')
def singup(request):
    return render(request,'singup.html')

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        return render(request,'category.html',locals())