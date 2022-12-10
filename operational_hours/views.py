from django.shortcuts import render, redirect
from django.db import connection

def create(request):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'restaurant':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')

    if request.method == 'POST':
        day = request.POST.get("day")
        open = request.POST.get("openTime")
        close = request.POST.get("closeTime")
        
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(f"""
        select rname, rbranch from restaurant where email = '{email}'
        """)
        data = cursor.fetchone()

        cursor.execute(f"""
        insert into restaurant_operating_hours values
        ('{data[0]}', '{data[1]}', '{day}', '{open}', '{close}')
        """)

        return redirect('operational_hours:read')
    
    return render(request, 'create_operational_hours.html')

def read(request):
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
    data = cursor.fetchall()

    context = {'data' : data}

    return render(request, 'read_operational_hours.html', context)

def update(request, rname, rbranch, day):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'restaurant':
        return redirect('sirest:logout')
    # end of login required

    email = request.session.get('email')
    context = {'day' : day}

    if request.method == 'POST':
        open = request.POST.get("openTime")
        close = request.POST.get("closeTime")

        if close < open:
            context['message'] = 'The close time should be after open time'
            render(request, 'update_operational_hours.html', context)
        else:
            cursor.execute("SET SEARCH_PATH TO SIREST")
            cursor.execute(f"""
            update restaurant_operating_hours
            set starthours = '{open}', endhours = '{close}'
            where name = '{rname}' and
                branch = '{rbranch}' and
                day = '{day}'
            """)

            return redirect('operational_hours:read')

    return render(request, 'update_operational_hours.html', context)

def delete(request, rname, rbranch, day):
    # login required
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO PUBLIC")

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'restaurant':
        return redirect('sirest:logout')
    # end of login required

    cursor.execute("SET SEARCH_PATH TO SIREST")
    cursor.execute(f"""
    delete from restaurant_operating_hours
    where name = '{rname}' and
        branch = '{rbranch}' and
        day = '{day}'
    """)

    return redirect('operational_hours:read')