from django.shortcuts import render, redirect, get_object_or_404
from .models import Operateur
from .forms import OperateurForm

def voir(request):
    operateurs = Operateur.objects.all()
    return render(request, 'list.html', {'operateurs': operateurs})

def detail(request, id_operateur):
    operateur = get_object_or_404(Operateur, id_operateur=id_operateur)
    return render(request, 'detail.html', {'operateur': operateur})

def create(request):
    if request.method == 'POST':
        form = OperateurForm(request.POST)
        if form.is_valid():
            operateur = form.save()
            return redirect('detail', id_operateur=operateur.id_operateur)
    else:
        form = OperateurForm()
    return render(request, 'form.html', {'form': form})

def update(request, id_operateur):
    operateur = get_object_or_404(Operateur, id_operateur=id_operateur)
    if request.method == 'POST':
        form = OperateurForm(request.POST, instance=operateur)
        if form.is_valid():
            operateur = form.save()
            return redirect('detail', id_operateur=operateur.id_operateur)
    else:
        form = OperateurForm(instance=operateur)
    return render(request, 'form.html', {'form': form})

def delete(request, id_operateur):
    operateur = get_object_or_404(Operateur, id_operateur=id_operateur)
    operateur.delete()
    return redirect('list.html')