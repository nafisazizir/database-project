from django.shortcuts import render, redirect
from django.db import connection
import random, string


def create_order_transaction_customer_1(request):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(
            f"""
            SELECT DISTINCT province
            FROM RESTAURANT
        """
        )

        provinces = cursor.fetchall()
        context["provinces"] = provinces
    return render(request, "c_delivery_address.html", context)


def create_order_transaction_customer_2(request):
    context = {}

    # with connection.cursor() as cursor:
    #     cursor.execute("SET SEARCH_PATH TO SIREST")
    #     cursor.execute(
    #         f"""
    #         SELECT DISTINCT province
    #         FROM RESTAURANT
    #     """
    #     )

    #     restaurants = cursor.fetchall()
    #     context["restaurants"] = restaurants
    return render(request, "c_restaurant_selection.html", context)


def create_order_transaction_customer_3(request):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(
            f"""
            SELECT name
            FROM PAYMENT_METHOD
        """
        )

        payment_method = cursor.fetchall()
        context["payment_method"] = payment_method
    return render(request, "c_selection.html", context)


def create_order_transaction_customer_4(request):
    return render(request, "c_order_list.html")


def create_order_transaction_customer_5(request):
    return render(request, "c_payment_confirmation.html")


def read_order_transaction_customer_1(request):
    context = {}

    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIREST")
        cursor.execute(
            f"""
            SELECT DISTINCT CONCAT(TF.RName, ' ', TF.RBranch), TH.Datetime, TS.Name
            FROM USER_ACC U, TRANSACTION_FOOD TF, TRANSACTION_HISTORY TH, TRANSACTION_STATUS TS, CUSTOMER C, TRANSACTION_ACTOR TA, TRANSACTION T
            WHERE U.Email = TA.Email 
            AND T.Email = C.Email 
            AND C.Email = T.Email
            AND T.Email = TF.Email
            AND TF.Datetime = TH.Datetime
            AND TH.TSId = TS.Id
        """
        )

        ongoing_orders = cursor.fetchall()
        context["ongoing_orders"] = ongoing_orders

    return render(request, "r_ongoing_orders.html", context)


def read_order_transaction_customer_2(request):
    return render(request, "r_order_summary.html")
