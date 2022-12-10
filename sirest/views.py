from django.shortcuts import render, redirect
from django.db import connection
from .forms import *

def homepage(request):
    return render(request, 'homepage.html')

def login_register(request):
    return render(request, 'login_register.html')

def logout(request):
    request.session.clear()
    return redirect("/login")


def login(request):
    context =  {}
    role = ''

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            cursor.execute(f"""
                SELECT password
                FROM USER_ACC
                WHERE email = '{email}'
            """)

            userPassLst = cursor.fetchall()

            if (len(userPassLst) == 0):
                context["message"] = "The account does not exist."
                return render(request, "login.html", context)

            if (len(userPassLst) != 0):
                retrievedPassword = userPassLst[0][0]
                if password != retrievedPassword:
                    context["message"] = "The password you entered is incorrect."
                    return render(request, "login.html", context)
                
                # check the role for admin
                cursor.execute(f"""
                SELECT *
                FROM ADMIN
                WHERE email = '{email}'
                """)
                adminLst = cursor.fetchall()
                if len(adminLst) != 0:
                    role = 'admin'

                # check the role for courier
                cursor.execute(f"""
                SELECT *
                FROM COURIER
                WHERE email = '{email}'
                """)
                courierLst = cursor.fetchall()
                if len(courierLst) != 0:
                    role = 'courier'

                # check the role for customer
                cursor.execute(f"""
                SELECT *
                FROM CUSTOMER
                WHERE email = '{email}'
                """)
                customerLst = cursor.fetchall()
                if len(customerLst) != 0:
                    role = 'customer'

                # check the role for restaurant
                cursor.execute(f"""
                SELECT *
                FROM RESTAURANT
                WHERE email = '{email}'
                """)
                restaurantLst = cursor.fetchall()
                if len(restaurantLst) != 0:
                    role = 'restaurant'
                
                cursor.execute("SET SEARCH_PATH TO PUBLIC")
                request.session["email"] = email
                request.session["role"] = role
                request.session['isLoggedIn'] = True

                if role == 'admin':
                    return redirect('user:show_admin_dash')
                elif role == 'courier':
                    return redirect('user:show_courier_dash')
                elif role == 'customer':
                    return redirect('user:show_customer_dash')
                elif role == 'restaurant':
                    return redirect('user:show_restaurant_dash')

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