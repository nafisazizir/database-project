from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
    return render(request, 'homepage.html')

def login_register(request):
    return render(request, 'login_register.html')

def logout(request):
    request.session.clear()
    return redirect("/login")

@csrf_exempt
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

                print("admin", adminLst)
                print("courier", courierLst)
                print("customer", customerLst)
                print("restaurant", restaurantLst)

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
    context = {}
    return render(request, 'register.html', context)

@csrf_exempt
def register_admin(request):
    context = {}
    
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name").split()
            phonenum = request.POST.get("phonenumber")

            fname = name[0]
            lname = ''
            for i in range(len(name)):
                lname = lname + name[i+1] + ' '
                if i == len(name)-2:
                    break
            lname = lname[:-1]

            try:
                cursor.execute(f"""
                    INSERT INTO USER_ACC VALUES
                    ('{email}', '{password}', '{phonenum}', '{fname}', '{lname}');
                    INSERT INTO ADMIN VALUES
                    ('{email}');
                """)

                cursor.execute("SET SEARCH_PATH TO PUBLIC")
                request.session["email"] = email
                request.session["role"] = 'admin'
                request.session['isLoggedIn'] = True
                return redirect('user:show_admin_dash')
            
            except Exception as e:
                mess = str(e).split('\n')[0]
                if 'password' in mess:
                    context['message'] = mess
                elif 'unique' in mess:
                    context['message'] = 'Email already exists!'
                print(mess)

    return render(request, "register_admin.html", context)

@csrf_exempt
def register_customer(request):
    context = {}
    
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name").split()
            phonenum = request.POST.get("phonenumber")

            nik = request.POST.get("nik")
            bankname = request.POST.get("bankname")
            accountnumber = request.POST.get("accountnumber")
            dateofbirth = request.POST.get("dateofbirth")
            gender = request.POST.get("gender")
            
            fname = name[0]
            lname = ''
            for i in range(len(name)):
                lname = lname + name[i+1] + ' '
                if i == len(name)-2:
                    break
            lname = lname[:-1]

            if gender == 'Male':
                gender = 'M'
            else:
                gender = 'F'

            try:
                cursor.execute(f"""
                    INSERT INTO USER_ACC VALUES
                    ('{email}', '{password}', '{phonenum}', '{fname}', '{lname}');
                    INSERT INTO TRANSACTION_ACTOR VALUES
                    ('{email}', '{nik}', '{bankname}', '{accountnumber}');
                    INSERT INTO CUSTOMER VALUES
                    ('{email}', '{dateofbirth}', '{gender}')
                """)

                cursor.execute("SET SEARCH_PATH TO PUBLIC")
                request.session["email"] = email
                request.session["role"] = 'customer'
                request.session['isLoggedIn'] = True
                return redirect('user:show_customer_dash')
            
            except Exception as e:
                mess = str(e).split('\n')[0]
                if 'password' in mess:
                    context['message'] = mess
                elif 'unique' in mess:
                    context['message'] = 'Email already exists!'
                else:
                    context['message'] = e

    return render(request, 'register_customer.html', context)

@csrf_exempt
def register_restaurant(request):
    context = {}
    
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")

        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name").split()
            phonenum = request.POST.get("phonenumber")
            nik = request.POST.get("nik")
            bankname = request.POST.get("bankname")
            accountnumber = request.POST.get("accountnumber")
            
            restaurantname = request.POST.get("restaurantname")
            branch = request.POST.get("branch")
            rphonenumber = request.POST.get("rphonenumber")
            street = request.POST.get("street")
            district = request.POST.get("district")
            city = request.POST.get("city")
            province = request.POST.get("province")
            restaurantcategory = request.POST.get("restaurantcategory")

            fname = name[0]
            lname = ''
            for i in range(len(name)):
                lname = lname + name[i+1] + ' '
                if i == len(name)-2:
                    break
            lname = lname[:-1]

            try:
                cursor.execute(f"""
                    INSERT INTO USER_ACC VALUES
                    ('{email}', '{password}', '{phonenum}', '{fname}', '{lname}');
                    INSERT INTO TRANSACTION_ACTOR VALUES
                    ('{email}', '{nik}', '{bankname}', '{accountnumber}');
                    INSERT INTO RESTAURANT VALUES
                    ('{restaurantname}', '{branch}', '{email}', '{rphonenumber}', '{street}',
                    '{district}', '{city}', '{province}', 0, '{restaurantcategory}')
                """)

                cursor.execute("SET SEARCH_PATH TO PUBLIC")
                request.session["email"] = email
                request.session["role"] = 'restaurant'
                request.session['isLoggedIn'] = True
                return redirect('user:show_restaurant_dash')
            
            except Exception as e:
                mess = str(e).split('\n')[0]
                if 'password' in mess:
                    context['message'] = mess
                elif 'unique' in mess:
                    context['message'] = 'Email already exists!'
                else:
                    context['message'] = e
        
        
        cursor.execute(f"""
        select *
        from restaurant_category
        """)
        context['category'] = cursor.fetchall()

    return render(request, 'register_restaurant.html', context)

@csrf_exempt
def register_courier(request):
    context = {}
    
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name").split()
            phonenum = request.POST.get("phonenumber")
            nik = request.POST.get("nik")
            bankname = request.POST.get("bankname")
            accountnumber = request.POST.get("accountnumber")

            numberplate = request.POST.get("numberplate")
            drivinglicensenumber = request.POST.get("drivinglicensenumber")
            vehicletype = request.POST.get("vehicletype")
            vehiclebrand = request.POST.get("vehiclebrand")

            fname = name[0]
            lname = ''
            for i in range(len(name)):
                lname = lname + name[i+1] + ' '
                if i == len(name)-2:
                    break
            lname = lname[:-1]

            try:
                cursor.execute(f"""
                    INSERT INTO USER_ACC VALUES
                    ('{email}', '{password}', '{phonenum}', '{fname}', '{lname}');
                    INSERT INTO TRANSACTION_ACTOR VALUES
                    ('{email}', '{nik}', '{bankname}', '{accountnumber}');
                    INSERT INTO COURIER VALUES
                    ('{email}', '{numberplate}', '{drivinglicensenumber}', '{vehicletype}', '{vehiclebrand}')
                """)

                cursor.execute("SET SEARCH_PATH TO PUBLIC")
                request.session["email"] = email
                request.session["role"] = 'courier'
                request.session['isLoggedIn'] = True
                return redirect('user:show_courier_dash')
            
            except Exception as e:
                mess = str(e).split('\n')[0]
                if 'password' in mess:
                    context['message'] = mess
                elif 'unique' in mess:
                    context['message'] = 'Email already exists!'
                else:
                    context['message'] = e

    return render(request, 'register_courier.html', context)