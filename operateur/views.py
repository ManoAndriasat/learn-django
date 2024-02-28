from django.shortcuts import render, get_object_or_404, redirect
from .models import Operateur
from django.http import HttpResponseBadRequest

def voir(request):
    operateurs = Operateur.objects.all()
    return render(request, 'list.html', {'operateurs': operateurs})

def create(request):
    if request.method == 'POST':
        id_operateur = request.POST.get('id_operateur')
        nom = request.POST.get('nom')
        Operateur.objects.create(id_operateur=id_operateur, nom=nom)
    return redirect('/operateur/list/')

def update(request , id_operateur):
    operateur = get_object_or_404(Operateur, id_operateur=id_operateur)
    if request.method == 'POST':
        operateur.nom = request.POST.get('nom')
        operateur.save()
    return redirect('/operateur/list/')

def delete(request):
    operateur = get_object_or_404(Operateur, id_operateur=request.GET.get('id_operateur'))
    operateur.delete()
    return redirect('/operateur/list/')

def update_get(request):
    operateur = get_object_or_404(Operateur, id_operateur=request.GET.get('id_operateur'))
    operateur.nom = request.GET.get('nom')
    operateur.save()
    return redirect('/operateur/list/')
