from django.shortcuts import render


def create_food_category(request):
    context = {}

    if not request.session.get("isLoggedIn"):
        return redirect("sirest:logout")
    if not request.session.get("role") == "admin":
        return redirect("sirest:logout")

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")

        if request.method == "POST":
            # generate random ID
            randomnum = "".join(random.choice(string.digits) for i in range(2))
            i = "FC"
            random_id = i + randomnum

            food_category_name = request.POST.get("food_category_name")

            cursor.execute(
                f"""
                INSERT INTO FOOD_CATEGORY VALUES
                ('{random_id}', '{food_category_name}')
            """
            )

            return redirect("/food_category/")

    return render(request, "c_food_category.html", context)


def read_food_category(request):
    context = {}

    if not request.session.get("isLoggedIn"):
        return redirect("sirest:logout")
    if not request.session.get("role") == "admin":
        return redirect("sirest:logout")

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(
            """
            SELECT name
            FROM FOOD_CATEGORY 
        """
        )

        food_category = cursor.fetchall()
        context["food_category"] = food_category

    return render(request, "r_food_category.html", context)


def delete_food_category(request, food_category_name):
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(
            f"""
            DELETE FROM FOOD_CATEGORY
            WHERE name = '{food_category_name}'
        """
        )

        return redirect("/food_category/")
