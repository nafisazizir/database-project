
from django.shortcuts import render, redirect
from django.db import connection


def read_order_transaction_courier(request):
    # if not request.session.get("isLoggedIn"):
    #     return redirect('sirest:logout')
    # if not request.session.get("role") == 'courier':
    #     return redirect('sirest:logout')

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
    # if not request.session.get("isLoggedIn"):
    #     return redirect('sirest:logout')
    # if not request.session.get("role") == 'courier':
    #     return redirect('sirest:logout')

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

def show_order_summary(request, email, datetime):

    # For reporting errors; pass into context
    errors = []

    # Cursor to execute SQL commands
    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST")

    # Fetch reference tuple
    try:
        SQL = f"""
        SELECT T.Email, T.Datetime, fname, lname, T.Street, T.District, T.City, T.Province,
        R.RName, R.RBranch, R.Street, R.District, R.City, R.Province, T.TotalFood, T.TotalDiscount,
        T.DeliveryFee, T.TotalPrice, PM.Name, PS.Name, TS.Name, CourierId
        FROM TRANSACTION T
        JOIN USER_ACC U ON T.Email = U.Email
        JOIN TRANSACTION_FOOD TF ON T.Email = TF.Email AND T.Datetime = TF.Datetime
        JOIN RESTAURANT R ON TF.RName = R.RName AND TF.RBranch = R.RBranch
        JOIN TRANSACTION_HISTORY TH ON TF.Email = TH.Email AND TF.Datetime = TH.Datetime
        JOIN TRANSACTION_STATUS TS ON TH.TSId = TS.Id
        JOIN PAYMENT_METHOD PM ON T.PMId = PM.Id
        JOIN PAYMENT_STATUS PS ON T.PSId = PS.Id
        WHERE T.Email = '{email}' AND T.Datetime = '{datetime}'
        """
        cursor.execute(SQL)
    except:
        errors.append("Order not found.")
    order_complete = cursor.fetchone()

    # All information from tuple
    order_email = order_complete[0]
    order_datetime = order_complete[1]
    order_name = str(order_complete[2]) + str(order_complete[3])
    order_street = order_complete[4]
    order_district = order_complete[5]
    order_city = order_complete[6]
    order_province = order_complete[7]
    restaurant_name = order_complete[8]
    restaurant_branch = order_complete[9]
    restaurant_street = order_complete[10]
    restaurant_district = order_complete[11]
    restaurant_city = order_complete[12]
    restaurant_province = order_complete[13]
    total_food = order_complete[14]
    total_discount = order_complete[15]
    delivery_fee = order_complete[16]
    total_price = order_complete[17]
    payment_method = order_complete[18]
    payment_status = order_complete[19]
    transaction_status = order_complete[20]
    courier_email = order_complete[21]

    # Fetch food of order
    try:
        SQL = f"""
        SELECT FoodName, Amount, Notes
        FROM TRANSACTION_FOOD
        WHERE Email = '{order_email}' AND Datetime = '{order_datetime}'
        AND RName = '{restaurant_name}' AND RBranch = '{restaurant_branch}'
        """
        cursor.execute(SQL)
        food_list = cursor.fetchone()
    except:
        errors.append(f"Empty order from {email} at {datetime}.")
        food_list = []

    # Fetch courier's name, platenum, vehicletype, vehiclebrand
    if courier_email:
        SQL = f"""
        SELECT fname, lname, platenum, vehicletype, vehiclebrand
        FROM USER_ACC U
        JOIN COURIER C ON U.Email = C.Email
        WHERE C.Email='{courier_email}'
        """
        cursor.execute(SQL)
        courier_tuple = cursor.fetchone()
        courier_name = str(courier_tuple[0]) + str(courier_tuple[1])
        courier_platenum = courier_tuple[2]
        courier_vehicletype = courier_tuple[3]
        courier_vehiclebrand = courier_tuple[4]
    else:
        courier_name = "-"
        courier_platenum = "-"
        courier_vehicletype = "-"
        courier_vehiclebrand = "-"

    
    context = {
        'errors': errors,
        'order_datetime': order_datetime, 
        'order_name': order_name, 
        'order_street': order_street, 
        'order_district': order_district,
        'order_city': order_city, 
        'order_province': order_province, 
        'restaurant_name': restaurant_name, 
        'restaurant_street': restaurant_street,
        'restaurant_district': restaurant_district, 
        'restaurant_city': restaurant_city, 
        'restaurant_province': restaurant_province,
        'food_list': food_list, 
        'total_food': total_food, 
        'total_discount': total_discount, 
        'delivery_fee': delivery_fee, 
        'total_price': total_price,
        'payment_method': payment_method, 
        'payment_status': payment_status, 
        'transaction_status': transaction_status, 
        'courier_name': courier_name, 
        'courier_platenum': courier_platenum,
        'courier_vehicletype': courier_vehicletype, 
        'courier_vehiclebrand': courier_vehiclebrand,
    }

    return render(request, "order_summary.html", context)


def update_transaction_status(request, email, datetime):
    # For reporting errors; pass into context
    errors = []

    # Cursor to execute SQL commands
    cursor = connection.cursor()
    cursor.execute("SET search_path to SIREST")
    
    # Find transaction status of tuple
    SQL = f"""
    SELECT TSId
    FROM TRANSACTION_HISTORY
    WHERE email = '{email}' AND datetime = '{datetime}'
    """
    cursor.execute(SQL)
    status = cursor.fetchone()[0]

    status = str(int(status) + 1)

    # Update TSID
    SQL = f"""
    UPDATE TRANSACTION_HISTORY
    SET TSID = '{status}'
    WHERE email = '{email}' AND datetime = '{datetime}'
    """
    cursor.execute(SQL)

    return redirect("kaloosh:list_ongoing_order")