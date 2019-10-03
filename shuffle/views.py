from django.shortcuts import render
from shuffle.models import Teams
import random

# Create your views here.
def test(request):
    tms = Teams.objects.all().order_by('?')[:32]
    return render(request, "index.html", {'tms':tms})

def showallteams(request):
    tms = Teams.objects.all().order_by('?')[:32]    
    return render(request,"test.html",{"tms":tms})

    
    
    
'''for i in range(500):
    tms = random.choice(tms)'''