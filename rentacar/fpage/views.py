from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from fleet.models import book

def index(request):
   
    return render(request, 'index.html')


def booking(request):
    booking=book.objects.all()
    
    return render(request,'bookhistory.html',{"booking":booking})




class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'