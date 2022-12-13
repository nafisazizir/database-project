from django.db import connection
from django.shortcuts import render, redirect
import random, string

def create_ingredient(request):
    context = {}

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        
        if request.method == "POST":
            # generate random ID
            randomnum = ''.join(random.choice(string.digits) for i in range(2))
            i = "I"
            random_id = i + randomnum

            ingredient_name = request.POST.get("ingredient_name")

            cursor.execute(f"""
                INSERT INTO INGREDIENT VALUES
                ('{random_id}', '{ingredient_name}')
            """)

            return redirect("/ingredient/")
        
    return render(request, "c_ingredient.html", context)

def read_ingredient(request):
    context = {}

    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'admin':
        return redirect('sirest:logout')
    
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("""
            SELECT DISTINCT I.Id, FI.Ingredient, I.Name
            FROM INGREDIENT I
            LEFT OUTER JOIN FOOD_INGREDIENT FI
            ON I.Id = FI.Ingredient; 
        """)

        ingredient = cursor.fetchall()
        context["ingredient"] = ingredient

    return render(request, 'r_ingredient.html', context)

def delete_ingredient(request, ingredient_name):
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(f"""
            DELETE FROM INGREDIENT
            WHERE name = '{ingredient_name}'
        """)

        return redirect("/ingredient/")