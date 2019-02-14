from django.shortcuts import render,redirect
from .models import Katalog
# from .forms import PostForm

# Create your views here.

def Katalog(request):
    return render(request,'katalog/katalog.html',{})


