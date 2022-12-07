from django.shortcuts import render, redirect
from django.db import connection
from .forms import *

def homepage(request):
    return render(request, 'homepage.html')

def login_register(request):
    return render(request, 'login_register.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register_admin(request):
    return render(request, 'register_admin.html')

def insert_user_registration(email, password, phonenum, fname, name):
    return """
    INSERT INTO SIREST.USER_ACC(email, password, phonenum, fname, name)
    VALUES ('{}', '{}', '{}', '{}', '{}')
    """.format(email, password, phonenum, fname, name)

def insert_customer_registration(email, birthdate, sex):
    return """
    INSERT INTO SIREST.CUSTOMER(email, birthdate, sex)
    VALUES ('{}', '{}', '{}')
    """

def insert_transaction_actor_registration(email, nik, bankname, accountno, restopay):
    return """
    INSERT INTO SIREST.TRANSACTION_ACTOR(email, nik, bankname, accountno, restopay)
    VALUES ('{}', '{}', '{}', '{}', '{}')
    """

def register_customer(request):
    try:
        form = customer_form(request.POST or None)

        if request.method == "POST" and form.is_valid():
            
            cursor = connection.cursor()
            cursor.execute(insert_user_registration(request.POST['email'], request.POST['password'], request.POST['phonenum'], request.POST['fname'], request.POST['name']))
            cursor.execute(insert_transaction_actor_registration(request.POST['email'], request.POST['nik'], request.POST['bankname'], request.POST['accountno'], request.POST['restopay']))
            cursor.execute(insert_customer_registration(request.POST['email'], request.POST['birthdate'], request.POST['sex']))

            if connection:
                connection.commit()
                cursor.close()
                connection.close()

            request.session['email'] = request.POST['email']
            request.session['password'] = request.POST['password']
            request.session['phonenum'] = request.POST['phonenum']
            request.session['fname'] = request.POST['fname']
            request.session['name'] = request.POST['name']
            request.session['nik'] = request.POST['nik']
            request.session['bankname'] = request.POST['bankname']
            request.session['accountno'] = request.POST['accountno']
            request.session['restopay'] = request.POST['restopay']
            request.session['birthdate'] = request.POST['birthdate']
            request.session['sex'] = request.POST['sex']
            request.session['role'] = "Customer"

            return redirect("/home")

        context = {'form' : form, 'fail_message' : ""}

        return render(request, 'sirest/register_customer.html', context)
    
    except Exception as e:
        return redirect('/')


def register_restaurant(request):
    return render(request, 'register_restaurant.html')

def register_courier(request):
    return render(request, 'register_courier.html')