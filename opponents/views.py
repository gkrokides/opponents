from django.shortcuts import render
from .models import Game
from .forms import GameForm

def index(request):
    return render(request,'opponents/index.html')

def games(request):
    form = GameForm()
    return render(request,'opponents/listgames.html',{'form': form})

def gamedetail(request):
    form = GameForm()
    return render(request,'opponents/gamedetail.html',{'form': form})