from django.db import connection
from django.shortcuts import render, redirect
import random, string

def create_restaurant_category(request):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")

        if request.method == "POST":
            random_id = "".join(('RC' + random.choice(string.digits)))
            category_name = request.POST.get("category_name")

            cursor.execute(f"""
                INSERT INTO RESTAURANT_CATEGORY VALUES
                ('{random_id}', '{category_name}')
            """)

            return redirect("/restaurant_category/")

    return render(request, "c_restaurant_category.html", context)

def read_restaurant_category(request):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("""
            SELECT name
            FROM RESTAURANT_CATEGORY 
        """)

        category = cursor.fetchall()
        context["category"] = category

    return render(request, "r_restaurant_category.html", context)

def delete_restaurant_category(request):
    context = {}
    name = request.session["nama"]
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        
        cursor.execute("""
            SELECT DISTINCT RC.Id
            FROM RESTAURANT_CATEGORY RC, RESTAURANT R
            WHERE RC.Id= R.RCategory
        """)

        reffered_id = cursor.fetchall()
        context["reffered_id"] = reffered_id

        if request.method == "POST":
            cursor.execute(f"""
                DELETE FROM RESTAURANT_CATEGORY
                WHERE name = '{name}'
            """)
            return redirect(f"/restaurant_category/")
    
    return render(request, 'read_restaurant_category.html', context)