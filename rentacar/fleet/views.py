from django.shortcuts import redirect, render
from .models import book

# Create your views here.
def fleet(request):
    if request.method=="POST":
        pickup=request.POST['pickup']
        returns=request.POST['returns']
        pudate=request.POST['pudate']
        rdate=request.POST['rdate']
        fullname=request.POST['fullname']
        email=request.POST['email']
        phno=request.POST['phone']
        ab=book(pickup=pickup,returns=returns,pudate=pudate,rdate=rdate,fullname=fullname,email=email,phno=phno)
        ab.save()
        print("Data Stored ")
        return redirect('/')
    else:
        return render(request,'fleet.html')