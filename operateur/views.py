from django.shortcuts import render
from .models import Operateur

def voir(request):
    operateurs = Operateur.objects.all()
    return render(request, 'list.html', {'operateurs': operateurs})
