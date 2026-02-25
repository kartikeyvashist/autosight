from sqlite3 import Cursor

import psycopg2
import csv 
from datetime import date
def analyze_daily_trend(daily_data):
    trend_results = []
    for i in range(1, len(daily_data)):
        previous_day = daily_data[i - 1]
        current_day = daily_data[i]

        previous_revenue = float(previous_day[1])
        current_revenue = float(current_day[1])

        change = current_revenue - previous_revenue
        Percentage_change = (change/previous_revenue) * 100

        if Percentage_change > 0:
            trend = "UP"
        elif Percentage_change < 0:
           trend = "Down"
        else:
            trend =  "Stable"

        trend_results.append({
            "From": str(previous_day[0]),
            "to": str(current_day[0]),
            "percentage_change": round(Percentage_change,2),
            "trend": trend,
            "insight": "Revenue dropped significantly. immediate investigation recommended."
        })
    return trend_results

def predict_next_day_revenue(daily_data):
    revenues = [float(day[1]) for day in daily_data]

    if len(revenues) < 2:
        return "Not enough data to predict"
    
    changes = []
    for i in range(1, len(revenues)):
        changes.append(revenues[i] - revenues[i-1])
    
    avg_change = sum(changes) / len(changes)

    predicted_revenue = revenues[-1] + avg_change

    if predicted_revenue < 0:
        predicted_revenue = 0

    return round(predicted_revenue, 2)

try:
    connection = psycopg2.connect(
        host="localhost",
        database="autoinsight_db",
        user="postgres",
        password="postgres",
        port="5432"
    )


    cursor = connection.cursor() # it is the remote control for the 
    cursor.execute("""
    SELECT 
        product_name,
        SUM(quantity) AS total_quantity,
        SUM(quantity * price) AS total_revenue
    FROM sales_data
    GROUP BY product_name
    ORDER BY total_revenue DESC;
""")
    product_records = cursor.fetchall()
    print("Product Performance: ")
    print("="*40)
    for product, total_quan, total_rev in product_records:
        print(f"Product: {product}")
        print(f"Total Quantity Sold: {total_quan}")
        print(f"Total Revenue: {total_rev}")
        print("-"*40)
    
    cursor.execute("""
    SELECT
        SUM(quantity),
        SUM(quantity*price)
    FROM sales_data;
""")

    overall_qty, overall_rev = cursor.fetchone()

    print("\nOverall Performance")
    print("="*40)
    print(f"Overall Quantity Sold: {overall_qty}")
    print(f"Overall Revenue: {overall_rev}")
    print("="*40)

    top_product = product_records[0][0]
    top_revenue = product_records[0][2]

    lowest_product = product_records[-1][0]
    lowest_revenue = product_records[-1][2]

    print("\nExcecutive Summary")
    print("="*40)
    print(f"Top Performing Product: {top_product}")
    print(f"Top Revenue Product: {float(top_revenue)}")
    print("-"*40)
    print(f"Lowest Performing Product: {lowest_product}")
    print(f"Lowest Revenue: {float(lowest_revenue)}")
    print("="*40)

    with open("sales_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO sales_data(sale_date, product_name, quantity, price)
                VALUES (%s, %s, %s, %s)
""", (          
            row["sale_date"],
            row["product_name"],
            int(row["quantity"]),
            float(row["price"])
        ))
    connection.commit()
    print("CSV data inserted successfully")

    cursor.execute("""
        SELECT
            sale_date,
            sum(quantity * price) AS daily_revenue
        FROM sales_data
        GROUP BY sale_date
        ORDER BY sale_date;    
""")
    

    
    daily_data = cursor.fetchall()
    results=analyze_daily_trend(daily_data)
    predict_revenue = predict_next_day_revenue(daily_data)
    print(results)
    cursor.close()
    connection.close()

except Exception as error:
    print("Error:", error)