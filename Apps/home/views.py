from django.shortcuts import render,redirect
from .forms import ReportsForm
from django.contrib import messages
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