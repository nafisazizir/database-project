from django.shortcuts import render


def create_order_transaction_customer_1(request):
    return render(request, "c_delivery_address.html")


def create_order_transaction_customer_2(request):
    return render(request, "c_restaurant_selection.html")


def create_order_transaction_customer_3(request):
    return render(request, "c_selection.html")


def create_order_transaction_customer_4(request):
    return render(request, "c_order_list.html")


def create_order_transaction_customer_5(request):
    return render(request, "c_payment_confirmation.html")


def read_order_transaction_customer_1(request):
    return render(request, "r_ongoing_orders.html")


def read_order_transaction_customer_2(request):
    return render(request, "r_order_summary.html")


def login(request):
    context = {}
    role = ""

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")

            cursor.execute(
                f"""
                SELECT password
                FROM USER_ACC
                WHERE email = '{email}'
            """
            )

            userPassLst = cursor.fetchall()

            if len(userPassLst) == 0:
                context["message"] = "The account does not exist."
                return render(request, "login.html", context)

            if len(userPassLst) != 0:
                retrievedPassword = userPassLst[0][0]
                if password != retrievedPassword:
                    context["message"] = "The password you entered is incorrect."
                    return render(request, "login.html", context)

                # check the role for admin
                cursor.execute(
                    f"""
                SELECT *
                FROM ADMIN
                WHERE email = '{email}'
                """
                )
                adminLst = cursor.fetchall()
                if len(adminLst) != 0:
                    role = "admin"

                # check the role for courier
                cursor.execute(
                    f"""
                SELECT *
                FROM COURIER
                WHERE email = '{email}'
                """
                )
                courierLst = cursor.fetchall()
                if len(courierLst) != 0:
                    role = "courier"

                # check the role for customer
                cursor.execute(
                    f"""
                SELECT *
                FROM CUSTOMER
                WHERE email = '{email}'
                """
                )
                customerLst = cursor.fetchall()
                if len(customerLst) != 0:
                    role = "customer"

                # check the role for restaurant
                cursor.execute(
                    f"""
                SELECT *
                FROM RESTAURANT
                WHERE email = '{email}'
                """
                )
                restaurantLst = cursor.fetchall()
                if len(restaurantLst) != 0:
                    role = "restaurant"

                cursor.execute("SET SEARCH_PATH TO PUBLIC")
                request.session["email"] = email
                request.session["role"] = role
                request.session["isLoggedIn"] = True

                if role == "admin":
                    return redirect("user:show_admin_dash")
                elif role == "courier":
                    return redirect("user:show_courier_dash")
                elif role == "customer":
                    return redirect("user:show_customer_dash")
                elif role == "restaurant":
                    return redirect("user:show_restaurant_dash")

    return render(request, "login.html")


def register(request):
    context = {}
    return render(request, "register.html", context)


def register_admin(request):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name")
            phonenum = request.POST.get("phonenumber")

            cursor.execute(
                f"""
                INSERT INTO ADMIN VALUES
                ('{email}', '{password}', '{name}', '{phonenum}')
            """
            )

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

            cursor.execute(
                f"""
                INSERT INTO CUSTOMER VALUES
                ('{email}', '{password}', '{name}', '{phonenum}', '{nik}', '{bankname}', '{accountnumber}', '{dateofbirth}', '{gender}')
            """
            )

            return redirect("/login")

    return render(request, "register_customer.html", context)


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

            cursor.execute(
                f"""
                INSERT INTO RESTAURANT VALUES
                ('{email}', '{password}', '{name}', '{phonenum}', '{nik}', '{bankname}', '{accountnumber}',
                '{restaurantname}', '{branch}', '{rphonenumber}', '{street}', '{district}', '{city}', '{province}', '{restaurantcategory}')
            """
            )

            return redirect("/login")

    return render(request, "register_restaurant.html", context)


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

            cursor.execute(
                f"""
                INSERT INTO COURIER VALUES
                ('{email}', '{password}', '{name}', '{phonenum}', '{nik}', '{bankname}', '{accountnumber}',
                '{numberplate}', '{drivinglicensenumber}', '{vehicletype}', '{vehiclebrand}')
            """
            )

            return redirect("/login")

    return render(request, "register_courier.html", context)
