from django.shortcuts import render

def read_transaction(request):
    return render(request, 'read_transaction.html')

def details(request):
    return render(request, 'details.html')