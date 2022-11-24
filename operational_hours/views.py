from django.shortcuts import render

def create(request):
    return render(request, 'create_operational_hours.html')

def read(request):
    return render(request, 'read_operational_hours.html')

def update(request):
    return render(request, 'update_operational_hours.html')
