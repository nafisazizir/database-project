from django.db import connection
from django.shortcuts import render, redirect

def create_restaurant_category(request):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("""
            SELECT name
            FROM RESTAURANT_CATEGORY 
            ORDER BY name DESC
        """)
        category = int(cursor.fetchone()[0]) + 1
        context["name"] = category

        if request.method == "POST":
            name = request.POST.get("name")
            cursor.execute(f"""
                    INSERT INTO RESTAURANT_CATEGORY VALUES
                    ('{name}')
                """)
            return redirect("/r_restaurant_category/")
            
    return render(request, "c_restaurant_category.html", context)

def read_restaurant_category(request):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("""
            SELECT name
            FROM RESTAURANT_CATEGORY 
        """)

        category = cursor.fetchone()
        context["category"] = category[0]

    return render(request, "r_restaurant_category.html", context)

def delete_restaurant_category(request):
    name = request.session["name"]
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(f"""
        DELETE FROM RESTAURANT_CATEGORY
        WHERE name = '{name}'""")
        return redirect(f"/restaurant_category/")