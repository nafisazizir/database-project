from django.shortcuts import render, redirect
from django.db import connection
from datetime import *

def read_transaction(request):
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
    select email, fname, lname, createdDate, ts2.name
    from (
    select u.email, Fname, Lname,
            min(th.datetime) as createdDate,
            max(ts.id) as tsId
        from user_acc u, transaction_history th, transaction_status ts, transaction_food tf, restaurant r
        where th.tsid = ts.id and
        th.email = tf.email and
        th.datetime = tf.datetime and
        tf.email = u.email and
        tf.rname = r.rname and
        tf.rbranch = r.rbranch and
        r.email = '{email}'
        group by u.email, fname, lname
    ) as temp, transaction_status ts2
    where tsId = ts2.id
    """)
    data = cursor.fetchall()
    # print(data) # comment when debug is completed

    cursor.execute(f"""
    select rname, rbranch
    from restaurant
    where email = '{email}'
    """)
    restaurant = cursor.fetchone()

    context = {'data' : data,
                'rname' : restaurant[0],
                'rbranch' : restaurant[1]}

    return render(request, 'read_transaction.html', context)

def details(request, custEmail, timestamp, rname, rbranch):
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
    select datetime, fname, lname, street, district, city, province
    from user_acc u, transaction t
    where t.email = u.email and
        t.email = '{custEmail}' and
        t.datetime = '{timestamp}'
    """)
    customer = cursor.fetchall()

    cursor.execute(f"""
    select rname, rbranch, street, district, city, province
    from restaurant
    where email = '{email}'
    """)
    restaurant = cursor.fetchall()

    cursor.execute(f"""
    select foodname, amount, note
    from transaction_food
    where email = '{custEmail}' and
        datetime = '{timestamp}' and
        rname = '{rname}' and
        rbranch = '{rbranch}'
    """)
    food = cursor.fetchall()

    cursor.execute(f"""
    select totalfood, totaldiscount, deliveryfee, totalprice, pm.name, ps.name
    from transaction t, payment_method pm, payment_status ps
    where t.pmid = pm.id and
        t.psid = ps.id and
        t.email = '{custEmail}' and
        t.datetime = '{timestamp}'
    """)
    payment = cursor.fetchall()

    cursor.execute(f"""
    select name
    from(
        select max(tsid) as tsid_max
        from transaction_history th, transaction_status ts
        where th.tsid = ts.id and
            th.email = '{custEmail}' and
            th.datetime = '{timestamp}'
        group by email, datetime
    ) as temp, transaction_status ts
    where ts.id = tsid_max
    """)
    transaction_status = cursor.fetchone()

    cursor.execute(f"""
    select u.fname, u.lname, platenum, c.vehicletype, vehiclebrand
    from user_acc u, courier c, transaction t
    where t.courierid = c.email and
        c.email = u.email and
        t.email = '{custEmail}' and
        t.datetime = '{timestamp}'
    """)
    courier = cursor.fetchone()

    context = {'datetime' : customer[0][0],
            'customer' : customer[0][1:],
            'restaurant' : restaurant[0], 
            'food' : food,
            'payment' : payment[0],
            'transaction_status' : transaction_status[0],
            'courier' : courier}

    return render(request, 'details_transaction_restaurant.html', context)