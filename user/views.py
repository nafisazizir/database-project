from django.shortcuts import render, redirect
from django.db import connection

def show_admin_dash(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"""
    select email, password, fname, lname, phonenum
    from user_acc
    where email = '{email}'
    """)
    user_acc = cursor.fetchone()

    cursor.execute(f"""
    select u.email, fname, lname,
    case
        when t.email in (select email from restaurant) then 'Restaurant'
        when t.email in (select email from courier) then 'Courier'
        when t.email in (select email from customer) then 'Customer'
    end as role, adminid
    from transaction_actor t
    left join user_acc u 
        on t.email = u.email
    left join restaurant r 
        on r.email = t.email
    left join courier c 
        on c.email = t.email
    left join customer cr 
        on cr.email = t.email
    order by adminid desc
    """)
    transaction_actor = cursor.fetchall()

    context = {'user_acc' : user_acc,
                'transaction_actor' : transaction_actor}
    
    return render(request, "User_Admin_Dashboard.html", context)

def show_courier_dash(request):
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
    cursor.execute(f"""
    select email, password, fname, lname, phonenum
    from user_acc
    where email = '{email}'
    """)
    user_acc = cursor.fetchone()

    cursor.execute(f"""
    select nik, bankname, accountno, adminid, restopay
    from transaction_actor
    where email = '{email}'
    """)
    transaction_actor = cursor.fetchone()

    cursor.execute(f"""
    select platenum, drivinglicensenum, vehicletype, vehiclebrand
    from courier
    where email = '{email}'
    """)
    courier_data = cursor.fetchone()

    cursor.execute(f"""
    select adminid, fname, lname
    from transaction_actor t, user_acc u
    where adminid = u.email and
        t.email = '{email}'
    """)
    verificator = cursor.fetchone()

    context = {'user_acc' : user_acc,
                'transaction_actor' : transaction_actor,
                'courier_data' : courier_data,
                'verificator': verificator}

    return render(request, "User_Courier_Dashboard.html", context)

def show_customer_dash(request):
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
    cursor.execute(f"""
    select email, password, fname, lname, phonenum
    from user_acc
    where email = '{email}'
    """)
    user_acc = cursor.fetchone()

    cursor.execute(f"""
    select nik, bankname, accountno, adminid, restopay
    from transaction_actor
    where email = '{email}'
    """)
    transaction_actor = cursor.fetchone()

    cursor.execute(f"""
    select birthdate, sex
    from customer
    where email = '{email}'
    """)
    customer_data = cursor.fetchone()

    cursor.execute(f"""
    select adminid, fname, lname
    from transaction_actor t, user_acc u
    where adminid = u.email and
        t.email = '{email}'
    """)
    verificator = cursor.fetchone()

    context = {'user_acc' : user_acc,
                'transaction_actor' : transaction_actor,
                'customer_data' : customer_data,
                'verificator': verificator}
    
    return render(request, "User_Customer_Dashboard.html", context)

def show_restaurant_dash(request):
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
    cursor.execute(f"""
    select email, password, fname, lname, phonenum
    from user_acc
    where email = '{email}'
    """)
    user_acc = cursor.fetchone()

    cursor.execute(f"""
    select nik, bankname, accountno, adminid, restopay
    from transaction_actor
    where email = '{email}'
    """)
    transaction_actor = cursor.fetchone()

    cursor.execute(f"""
    select rname, rbranch, rphonenum, street, district, city, province, rating, name
    from restaurant r, restaurant_category c
    where email = '{email}' and
    rcategory = c.id
    """)
    restaurant_data = cursor.fetchone()

    cursor.execute(f"""
    select adminid, fname, lname
    from transaction_actor t, user_acc u
    where adminid = u.email and
        t.email = '{email}'
    """)
    verificator = cursor.fetchone()

    cursor.execute(f"""
    select day, starthours, endhours, r.rname, r.rbranch
    from restaurant r, restaurant_operating_hours ro
    where ro.name = r.rname and
        ro.branch = r.rbranch
        and r.email = '{email}'
    ORDER BY 
     CASE
          WHEN Day = 'Sunday' THEN 1
          WHEN Day = 'Monday' THEN 2
          WHEN Day = 'Tuesday' THEN 3
          WHEN Day = 'Wednesday' THEN 4
          WHEN Day = 'Thursday' THEN 5
          WHEN Day = 'Friday' THEN 6
          WHEN Day = 'Saturday' THEN 7
     END ASC
    """)
    opHours = cursor.fetchall()

    context = {'user_acc' : user_acc,
                'transaction_actor' : transaction_actor,
                'restaurant_data' : restaurant_data,
                'verificator': verificator,
                'opHours' : opHours}
    
    return render(request, "User_Restaurant_Dashboard.html", context)

def show_courier_profile(request, email):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')
    # end of login required

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"""
    select email, password, fname, lname, phonenum
    from user_acc
    where email = '{email}'
    """)
    user_acc = cursor.fetchone()

    cursor.execute(f"""
    select nik, bankname, accountno, adminid, restopay
    from transaction_actor
    where email = '{email}'
    """)
    transaction_actor = cursor.fetchone()

    cursor.execute(f"""
    select platenum, drivinglicensenum, vehicletype, vehiclebrand
    from courier
    where email = '{email}'
    """)
    courier_data = cursor.fetchone()

    cursor.execute(f"""
    select adminid, fname, lname
    from transaction_actor t, user_acc u
    where adminid = u.email and
        t.email = '{email}'
    """)
    verificator = cursor.fetchone()

    context = {'user_acc' : user_acc,
                'transaction_actor' : transaction_actor,
                'courier_data' : courier_data,
                'verificator': verificator}
    
    return render(request, "User_Courier_Profile.html", context)

def show_customer_profile(request, email):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')
    # end of login required

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"""
    select email, password, fname, lname, phonenum
    from user_acc
    where email = '{email}'
    """)
    user_acc = cursor.fetchone()

    cursor.execute(f"""
    select nik, bankname, accountno, adminid, restopay
    from transaction_actor
    where email = '{email}'
    """)
    transaction_actor = cursor.fetchone()

    cursor.execute(f"""
    select birthdate, sex
    from customer
    where email = '{email}'
    """)
    customer_data = cursor.fetchone()

    cursor.execute(f"""
    select adminid, fname, lname
    from transaction_actor t, user_acc u
    where adminid = u.email and
        t.email = '{email}'
    """)
    verificator = cursor.fetchone()

    context = {'user_acc' : user_acc,
                'transaction_actor' : transaction_actor,
                'customer_data' : customer_data,
                'verificator': verificator}
    
    return render(request, "User_Customer_Profile.html", context)

def show_restaurant_profile(request, email):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')
    # end of login required

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"""
    select email, password, fname, lname, phonenum
    from user_acc
    where email = '{email}'
    """)
    user_acc = cursor.fetchone()

    cursor.execute(f"""
    select nik, bankname, accountno, adminid, restopay
    from transaction_actor
    where email = '{email}'
    """)
    transaction_actor = cursor.fetchone()

    cursor.execute(f"""
    select rname, rbranch, rphonenum, street, district, city, province, rating, name
    from restaurant r, restaurant_category c
    where email = '{email}' and
    rcategory = c.id
    """)
    restaurant_data = cursor.fetchone()

    cursor.execute(f"""
    select adminid, fname, lname
    from transaction_actor t, user_acc u
    where adminid = u.email and
        t.email = '{email}'
    """)
    verificator = cursor.fetchone()

    cursor.execute(f"""
    select day, starthours, endhours, r.rname, r.rbranch
    from restaurant r, restaurant_operating_hours ro
    where ro.name = r.rname and
        ro.branch = r.rbranch
        and r.email = '{email}'
    ORDER BY 
     CASE
          WHEN Day = 'Sunday' THEN 1
          WHEN Day = 'Monday' THEN 2
          WHEN Day = 'Tuesday' THEN 3
          WHEN Day = 'Wednesday' THEN 4
          WHEN Day = 'Thursday' THEN 5
          WHEN Day = 'Friday' THEN 6
          WHEN Day = 'Saturday' THEN 7
     END ASC
    """)
    opHours = cursor.fetchall()

    cursor.execute(f"""
    select *
    from restaurant_promo
    where rname = '{restaurant_data[0]}' and
        rbranch = '{restaurant_data[1]}' and
        end_time > now() and
        start_time < now()
    """)
    curr_promo = cursor.fetchall()

    context = {'user_acc' : user_acc,
                'transaction_actor' : transaction_actor,
                'restaurant_data' : restaurant_data,
                'verificator': verificator,
                'opHours' : opHours,
                'curr_promo' : curr_promo}
    
    return render(request, "User_Restaurant_Profile.html", context)

def update(request, custEmail):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"""
    update transaction_actor
    set adminid = '{email}'
    where email = '{custEmail}'
    """)

    return redirect('user:show_admin_dash')

def details(request, email, role):
    if role == 'Restaurant':
        return redirect(f'/user/restaurant_profile/{email}')
    elif role == 'Customer':
        return redirect(f'/user/customer_profile/{email}')
    elif role == 'Courier':
        return redirect(f'/user/courier_profile/{email}')