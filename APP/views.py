from django.shortcuts import render,HttpResponse
from datetime import datetime
from APP.models import Contact
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('confirm-password')
        date = datetime.today()
        contact = Contact(username=name,email=email,password=password,date=date)
        contact.save()
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")
