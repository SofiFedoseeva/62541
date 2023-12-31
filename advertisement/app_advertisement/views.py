from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisements
from .forms import AdvertisementForm
#from django.http import HttpResponse

def index(request):
    advertisement = Advertisements.objects.all()
    context = {'advertisements': advertisement}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('index')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request,'advertisement-post.html', context)

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

