from django.shortcuts import render, redirect
from django.db import connection

def read_order_transaction_courier(request):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute(f"SET SEARCH_PATH TO SIREST")
        cursor.execute(f"""
            SELECT DISTINCT TF.RBranch, CONCAT(U.FName, ' ', U.LName), TH.Datetime, TS.Name
            FROM USER_ACC U, TRANSACTION_FOOD TF, TRANSACTION_HISTORY TH, TRANSACTION_STATUS TS, CUSTOMER C, TRANSACTION_ACTOR TA, TRANSACTION T
            WHERE U.Email = TA.Email 
            AND T.Email = C.Email 
            AND C.Email = T.Email
            AND T.Email = TF.Email
            AND TF.Datetime = TH.Datetime
            AND TH.TSId = TS.Id
        """)

        transaction_status = cursor.fetchall()
        context["transaction_status"] = transaction_status

    return render(request, 'r_order_transaction_courier.html', context)

def summary_order_transaction_courier(request):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute(f"SET SEARCH_PATH TO SIREST")
        cursor.execute(f"""
            SELECT TH.Datetime, U.FName, U.LName, T.Street, T.District, T.City, T.Province, 
            R.RName, R.Street, R.District, R.City, R.Province, 
        """)

    return render(request, 'summary_order_transaction_courier.html', context)