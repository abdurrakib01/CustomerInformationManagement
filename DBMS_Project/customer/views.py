from django.db import connection
from django.shortcuts import render
# Create your views here.
from .models import CustomerInformation

def homepage(request):
    query = request.POST.get('query')
    data = CustomerInformation.objects.raw(query)
    context = {
        'result' : data
    }
    return render(request, 'homepage.html', context)