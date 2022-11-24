from django.shortcuts import render

# Create your views here.
def show_restopromos(request):
    return render(request, "restopromos.html")

def min_trans_rform(request):
    return render(request, "min_trans_rform.html")

def special_day_rform(request):
    return render(request, "special_day_rform.html")

def special_day_rdetails(request):
    return render(request, "special_day_rdetails.html")

def min_trans_rdetails(request):
    return render(request, "min_trans_rdetails.html")

def special_edit_rdetails(request):
    return render(request, "special_edit_rdetails.html")

def min_edit_rdetails(request):
    return render(request, "min_edit_rdetails.html")