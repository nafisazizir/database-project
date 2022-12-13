
from django.shortcuts import render, redirect
from django.db import connection


def read_order_transaction_courier(request):
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'courier':
        return redirect('sirest:logout')

    context = {}
    with connection.cursor() as cursor:
        cursor.execute(f"SET SEARCH_PATH TO SIREST")
        cursor.execute(
            f"""
            SELECT DISTINCT TF.RBranch, CONCAT(U.FName, ' ', U.LName), TH.Datetime, TS.Name
            FROM USER_ACC U, TRANSACTION_FOOD TF, TRANSACTION_HISTORY TH, TRANSACTION_STATUS TS, CUSTOMER C, TRANSACTION_ACTOR TA, TRANSACTION T
            WHERE U.Email = TA.Email 
            AND T.Email = C.Email 
            AND C.Email = T.Email
            AND T.Email = TF.Email
            AND TF.Datetime = TH.Datetime
            AND TH.TSId = TS.Id
        """
        )

        transaction_status = cursor.fetchall()
        context["transaction_status"] = transaction_status

    return render(request, "r_order_transaction_courier.html", context)


def summary_order_transaction_courier(request, restaurant_branch):
    if not request.session.get("isLoggedIn"):
        return redirect('sirest:logout')
    if not request.session.get("role") == 'courier':
        return redirect('sirest:logout')

    context = {}

    with connection.cursor() as cursor:
        cursor.execute(f"SET SEARCH_PATH TO SIREST")

        cursor.execute(
            f"""
            SELECT DISTINCT TF.RBranch, CONCAT(U.FName, ' ', U.LName), TH.Datetime, TS.Name
            FROM USER_ACC U, TRANSACTION_FOOD TF, TRANSACTION_HISTORY TH, TRANSACTION_STATUS TS, CUSTOMER C, TRANSACTION_ACTOR TA, TRANSACTION T
            WHERE U.Email = TA.Email 
            AND T.Email = C.Email 
            AND C.Email = T.Email
            AND T.Email = TF.Email
            AND TF.Datetime = TH.Datetime
            AND TH.TSId = TS.Id
        """
        )

        ongoing_order = cursor.fetchone()
        customer_email = ongoing_order[1]
        context["restaurant_branch"] = ongoing_order[0]

        cursor.execute(f"""
            SELECT CONCAT(U.FName, ' ', U.LName), T.Street, T.District, T.City, T.Province
            FROM USER_ACC U
            JOIN CUSTOMER C ON U.Email = C.Email
            JOIN TRANSACTION T ON C.Email = T.Email
            WHERE C.Email = '{customer_email}'
        """)

        cursor.execute(f"""
            SELECT R.RBranch, R.Street, R.District, R.City, R.Province
            FROM RESTAURANT R
            WHERE R.RBranch = '{restaurant_branch}'
        """)

        # cursor.execute(f"""
        #     SELECT CONCAT(U.FName, ' ', U.LName), C.Platenum, C.VehicleType, C.VehicleBrand
        #     FROM USER_ACC
        #     JOIN TRANSACTION T
        #     JOIN COURIER C
        #     WHERE 
        #     C.Email = T.CourierID
        # """)

        customer_detail = cursor.fetchone()
        context["customer_detail"] = customer_detail

        restaurant_detail = cursor.fetchone()
        context["restaurant_detail"] = restaurant_detail

        # courier_detail = cursor.fetchone()
        # context["courier_detail"] = courier_detail

    return render(request, "summary_order_transaction_courier.html", context)
