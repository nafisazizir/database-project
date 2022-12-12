from django.db import connection
from django.shortcuts import render, redirect
import random, string

def create_ingredient(request):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        
        if request.method == "POST":
            random_id = "".join(('I' + random.choice(string.digits)))
            ingredient_name = request.POST.get("ingredient_name")

            cursor.execute(f"""
                INSERT INTO INGREDIENT VALUES
                ('{random_id}', '{ingredient_name}')
            """)

            return redirect("/ingredient/")
        
    return render(request, "c_ingredient.html", context)

def read_ingredient(request):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("""
            SELECT name
            FROM INGREDIENT 
        """)

        ingredient = cursor.fetchall()
        context["ingredient"] = ingredient

    return render(request, 'r_ingredient.html', context)

# def delete_ingredient(request):
#     name = request.session["name"]
#     with connection.cursor() as cursor:
#         cursor.execute("SET SEARCH_PATH TO SIREST")
#         cursor.execute(f"""
#         DELETE FROM INGREDIENT
#         WHERE name = '{name}'""")
#         return redirect(f"/ingredient/")

def delete_ingredient(request):
    context = {}
    nama = request.session["nama"]

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        
        if request.method == "POST":
            cursor.execute(f"""
                DELETE FROM INGREDIENT
                WHERE name = '{nama}'
            """)

            return redirect("/ingredient/")
    return render(request, "r_ingredient.html", context)