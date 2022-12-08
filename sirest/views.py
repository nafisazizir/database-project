from django.shortcuts import render, redirect
from django.db import connection

def homepage(request):
    return render(request, 'homepage.html')

def login_register(request):
    return render(request, 'login_register.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    context = {}
    return render(request, 'register.html', context)

def register_admin(request):
    context = {}
    
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name")
            phonenum = request.POST.get("phonenumber")

            cursor.execute(f"""
                INSERT INTO ADMIN VALUES
                ('{email}', '{password}', '{name}', '{phonenum}')
            """)

            # return redirect("/systemadmin")        

    return render(request, "register_admin.html", context)

def register_customer(request):
    context = {}
    
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name")
            phonenum = request.POST.get("phonenumber")

            nik = request.POST.get("nik")
            bankname = request.POST.get("bankname")
            accountnumber = request.POST.get("accountnumber")
            dateofbirth = request.POST.get("dateofbirth")
            gender = request.POST.get("gender")
            
            cursor.execute(f"""
                INSERT INTO CUSTOMER VALUES
                ('{email}', '{password}', '{name}', '{phonenum}', '{nik}', '{bankname}', '{accountnumber}', '{dateofbirth}', '{gender}')
            """)

            return redirect("/login")        

    return render(request, 'register_customer.html', context)

def register_restaurant(request):
    context = {}
    
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name")
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


            cursor.execute(f"""
                INSERT INTO RESTAURANT VALUES
                ('{email}', '{password}', '{name}', '{phonenum}', '{nik}', '{bankname}', '{accountnumber}',
                '{restaurantname}', '{branch}', '{rphonenumber}', '{street}', '{district}', '{city}', '{province}', '{restaurantcategory}')
            """)

            return redirect("/login")

    return render(request, 'register_restaurant.html', context)

def register_courier(request):
    context = {}
    
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name")
            phonenum = request.POST.get("phonenumber")
            nik = request.POST.get("nik")
            bankname = request.POST.get("bankname")
            accountnumber = request.POST.get("accountnumber")

            numberplate = request.POST.get("numberplate")
            drivinglicensenumber = request.POST.get("drivinglicensenumber")
            vehicletype = request.POST.get("vehicletype")
            vehiclebrand = request.POST.get("vehiclebrand")


            cursor.execute(f"""
                INSERT INTO COURIER VALUES
                ('{email}', '{password}', '{name}', '{phonenum}', '{nik}', '{bankname}', '{accountnumber}',
                '{numberplate}', '{drivinglicensenumber}', '{vehicletype}', '{vehiclebrand}')
            """)

            return redirect("/login")

    return render(request, 'register_courier.html', context)