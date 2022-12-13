from django.db import connection
from django.shortcuts import render, redirect, HttpResponseRedirect
import random, string

def create_restaurant_category(request):
    context = {}

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("""
            SELECT Name
            FROM RESTAURANT_CATEGORY
        """)

        category_table = cursor.fetchall()
        context["category_table"] = category_table

        if request.method == "POST":
            category_name = request.POST.get("category_name")

            # generate random ID
            randomnum = ''.join(random.choice(string.digits) for i in range(2))
            rc = "RC"
            random_id = rc + randomnum

            cursor.execute(f"""
                INSERT INTO RESTAURANT_CATEGORY VALUES
                ('{random_id}', '{category_name}')
            """)

            return redirect("/restaurant_category/")

    return render(request, "c_restaurant_category.html", context)

def read_restaurant_category(request):
    context = {}
    
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("""
            SELECT DISTINCT RC.Id, R.RCategory, RC.Name
            FROM RESTAURANT_CATEGORY RC
            LEFT OUTER JOIN RESTAURANT R
            ON RC.Id = R.RCategory;
        """)

        category = cursor.fetchall()
        context["category"] = category

    return render(request, "r_restaurant_category.html", context)

def delete_restaurant_category(request, category_name):
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(f"""
            DELETE FROM RESTAURANT_CATEGORY
            WHERE name = '{category_name}'
        """)

        return redirect("/restaurant_category/")