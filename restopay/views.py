from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

# --------- RESTAURANT ---------
def read_restopay_restaurant(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'restaurant':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"select restopay from transaction_actor where email = '{email}'")
    restopay = cursor.fetchone()

    context = {'balance' : restopay[0]}

    return render(request, "read_restopay_restaurant.html", context)

@csrf_exempt
def topup_restaurant(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'restaurant':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"select restopay from transaction_actor where email = '{email}'")
    restopay = cursor.fetchone()

    cursor.execute(f"select bankname, accountno from transaction_actor where email = '{email}'")
    bankInfo = cursor.fetchone()

    context = {'balance' : restopay[0],
                'bankName' : bankInfo[0],
                'accountNo' : bankInfo[1]}
    
    if request.method == "POST":
        amount = request.POST.get("amount")

        cursor.execute(f"""
        update transaction_actor
        set restopay = restopay + {amount}
        where email = '{email}'
        """)

        return redirect('restopay:read_restopay_restaurant')

    return render(request, "update_topup_restaurant.html", context)

@csrf_exempt
def withdraw_restaurant(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'restaurant':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"select restopay from transaction_actor where email = '{email}'")
    restopay = cursor.fetchone()

    context = {'balance' : restopay[0]}

    if request.method == 'POST':
        amount = request.POST.get("amount")
        if int(amount) < int(context['balance']):
            cursor.execute(f"""
            select withdraw({amount}, '{email}')
            """)
            return redirect('restopay:read_restopay_restaurant')
        else:
            context['message'] = 'Your RestoPay Balance is not sufficient'
            return render(request, "update_withdraw_restaurant.html", context)

    return render(request, "update_withdraw_restaurant.html", context)

# --------- CUSTOMER ---------
def read_restopay_customer(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'customer':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"select restopay from transaction_actor where email = '{email}'")
    restopay = cursor.fetchone()

    context = {'balance' : restopay[0]}

    return render(request, "read_restopay_customer.html", context)

@csrf_exempt
def topup_customer(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'customer':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"select restopay from transaction_actor where email = '{email}'")
    restopay = cursor.fetchone()

    cursor.execute(f"select bankname, accountno from transaction_actor where email = '{email}'")
    bankInfo = cursor.fetchone()

    context = {'balance' : restopay[0],
                'bankName' : bankInfo[0],
                'accountNo' : bankInfo[1]}
    
    if request.method == "POST":
        amount = request.POST.get("amount")

        cursor.execute(f"""
        update transaction_actor
        set restopay = restopay + {amount}
        where email = '{email}'
        """)

        return redirect('restopay:read_restopay_customer')

    return render(request, "update_topup_customer.html", context)

@csrf_exempt
def withdraw_customer(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'customer':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"select restopay from transaction_actor where email = '{email}'")
    restopay = cursor.fetchone()

    context = {'balance' : restopay[0]}

    if request.method == 'POST':
        amount = request.POST.get("amount")
        if int(amount) < int(context['balance']):
            cursor.execute(f"""
            select withdraw({amount}, '{email}')
            """)
            return redirect('restopay:read_restopay_customer')
        else:
            context['message'] = 'Your RestoPay Balance is not sufficient'
            return render(request, "update_withdraw_customer.html", context)

    return render(request, "update_withdraw_customer.html", context)

# --------- COURIER ---------
def read_restopay_courier(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        print("nggak login")
        return redirect('sirest:logout')
    if not request.session.get("role") == 'courier':
        print("nggak kurir")
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"select restopay from transaction_actor where email = '{email}'")
    restopay = cursor.fetchone()

    context = {'balance' : restopay[0]}

    return render(request, "read_restopay_courier.html", context)

@csrf_exempt
def topup_courier(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'courier':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"select restopay from transaction_actor where email = '{email}'")
    restopay = cursor.fetchone()

    cursor.execute(f"select bankname, accountno from transaction_actor where email = '{email}'")
    bankInfo = cursor.fetchone()

    context = {'balance' : restopay[0],
                'bankName' : bankInfo[0],
                'accountNo' : bankInfo[1]}
    
    if request.method == "POST":
        amount = request.POST.get("amount")

        cursor.execute(f"""
        update transaction_actor
        set restopay = restopay + {amount}
        where email = '{email}'
        """)

        return redirect('restopay:read_restopay_courier')

    return render(request, "update_topup_courier.html", context)

@csrf_exempt
def withdraw_courier(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'courier':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"select restopay from transaction_actor where email = '{email}'")
    restopay = cursor.fetchone()

    context = {'balance' : restopay[0]}

    if request.method == 'POST':
        amount = request.POST.get("amount")
        if int(amount) < int(context['balance']):
            cursor.execute(f"""
            select withdraw({amount}, '{email}')
            """)
            return redirect('restopay:read_restopay_courier')
        else:
            context['message'] = 'Your RestoPay Balance is not sufficient'
            return render(request, "update_withdraw_courier.html", context)

    return render(request, "update_withdraw_courier.html", context)
