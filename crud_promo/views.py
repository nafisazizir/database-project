from django.shortcuts import render

# Create your views here.
def show_promos(request):
    return render(request, "promos.html")

def show_rpromos(request):
    return render(request, "rpromos.html")

def min_trans_pform(request):
    return render(request, "min_trans_pform.html")

def special_day_pform(request):
    return render(request, "special_day_pform.html")

def special_day_details(request):
    return render(request, "special_day_details.html")

def special_edit_details(request):
    return render(request, "special_edit_details.html")

def min_trans_details(request):
    return render(request, "min_trans_details.html")

def min_edit_details(request):
    return render(request, "min_edit_details.html")
