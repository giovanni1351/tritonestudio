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

def get_client_ip(request):
    """
    Função auxiliar para obter o endereço IP real do cliente,
    mesmo quando atrás de proxies ou balanceadores de carga.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # Pega o primeiro IP na lista (o original)
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        # Sem proxy, pega o IP diretamente
        ip = request.META.get('REMOTE_ADDR')
    return ip




def home(request):
    games = Game.objects.all()
    if request.method == 'POST':
        form = ReportsForm(request.POST)
        if form.is_valid():
            # Não salva o objeto imediatamente para podermos modificá-lo
            report = form.save(commit=False)
            # Adiciona o endereço IP ao objeto
            report.ip_address = get_client_ip(request)
            # Agora salva o objeto com o endereço IP
            report.save()
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