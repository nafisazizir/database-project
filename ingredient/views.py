from django.db import connection
from django.shortcuts import render, redirect

def create_ingredient(request):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute("""
            SELECT name
            FROM INGREDIENT 
            ORDER BY name DESC
        """)
        ingredient = int(cursor.fetchone()[0]) + 1
        context["name"] = ingredient

        if request.method == "POST":
            name = request.POST.get("name")
            cursor.execute(f"""
                    INSERT INTO INGREDIENT VALUES
                    ('{name}')
                """)
            return redirect("/ingredient/")

    return render(request, 'c_ingredient.html', context)

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

def delete_ingredient(request):
    name = request.session["name"]
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(f"""
        DELETE FROM INGREDIENT
        WHERE name = '{name}'""")
        return redirect(f"/ingredient/")