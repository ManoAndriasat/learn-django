from django.shortcuts import render, redirect, get_object_or_404
from .models import Operateur

def voir(request):
    operateurs = Operateur.objects.all()
    return render(request, 'list.html', {'operateurs': operateurs})

def detail(request, id_operateur):
    operateur = get_object_or_404(Operateur, id_operateur=id_operateur)
    return render(request, 'detail.html', {'operateur': operateur})

def create(request):
    if request.method == 'POST':
        id_operateur = request.POST.get('id_operateur')
        nom = request.POST.get('nom')
        operateur = Operateur.objects.create(id_operateur=id_operateur, nom=nom)
        return redirect('detail', id_operateur=operateur.id_operateur)
    else:
        return render(request, 'form.html')

def update(request, id_operateur):
    operateur = get_object_or_404(Operateur, id_operateur=id_operateur)
    if request.method == 'POST':
        nom = request.POST.get('nom')
        operateur.nom = nom
        operateur.save()
        return redirect('detail', id_operateur=operateur.id_operateur)
    else:
        return render(request, 'form.html')

def delete(request, id_operateur):
    operateur = get_object_or_404(Operateur, id_operateur=id_operateur)
    operateur.delete()
    return redirect('list.html')
