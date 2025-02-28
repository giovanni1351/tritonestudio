from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReportsForm
from django.contrib import messages
from .models import Game
def index(request):
    if request.method == 'POST':
        form = ReportsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulário enviado com sucesso!')
            return redirect('index')  # Substitua pelo nome da URL desejada
    else:
        form = ReportsForm()
    return render(request, 'home/index.html', {'form': form})

def index2(request):
    if request.method == 'POST':
        form = ReportsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulário enviado com sucesso!')
            return redirect('index')  # Substitua pelo nome da URL desejada
    else:
        form = ReportsForm()
    return render(request, 'home/index2.html', {'form': form})


def drunkwiz(request):
    if request.method == 'POST':
        form = ReportsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulário enviado com sucesso!')
            return redirect('Drunk Wiz')  # Substitua pelo nome da URL desejada
    else:
        form = ReportsForm()
    return render(request,'home/drunkwiz.html',{'form': form})

def home(request):
    games = Game.objects.all()
    if request.method == 'POST':
        form = ReportsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formulário enviado com sucesso!')
            return redirect('home')  # Substitua pelo nome da URL desejada
    else:
        form = ReportsForm()
    context = {
        'games': games,
        'form': form,
    }
    return render(request, 'home/index2.html', context)

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    context = {
        'game': game,

    }
    return render(request, 'home/GameDetail.html', context)
def jogar(request, id):
    game = get_object_or_404(Game, id=id)
    context = {
        'URL_JOGO': game.play_url,

    }
    return render(request, 'home/includes/Jogar.html', context)