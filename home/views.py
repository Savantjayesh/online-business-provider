from django.db.models import Count
from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Product
from .models import singup
from .models import about
# Create your views here.

def index(request):
    return render(request, 'index.html')
  #  return HttpResponse("this is homepage")
def about(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone_no =request.POST.get('phone_no')
        query =request.POST.get('query')
        about = about(name=name, email=email, phone_no=phone_no, query=query)
        about.save()
    return render(request,'about.html')

def login1(request):
    return render(request,'login1.html')

def singup(request):
    if request.method == "POST":
        first_name =request.POST.get('first_name')
        medal_name =request.POST.get('medal_name')
        last_name =request.POST.get('last_name')
        contact =request.POST.get('contact')
        birth_date =request.POST.get('birth_date')
        user_name =request.POST.get('user_name')
        password =request.POST.get('password')
        singup = singup(first_name=first_name, medal_name=medal_name, last_name=last_name, contact=contact, birth_date=birth_date, user_name=user_name )
        singup.save()
    return render(request,'singup.html')

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.object.filter(category=val).values('title')
        return render(request,'category.html',locals())