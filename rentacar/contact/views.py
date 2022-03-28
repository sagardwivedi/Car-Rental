from django.shortcuts import render,redirect
from .models import Contact
# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']

        xy=Contact(name=name,email=email,message=message)
        xy.save()
        print("Data Stored ")
        return redirect('/')
    else:
        return render(request,'contact.html')