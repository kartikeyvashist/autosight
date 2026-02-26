from db import get_connection
from ingestion import ingest_csv
from analysis import analyze_daily_trend, predict_next_day_revenue
from reporting import export_report

def main():

    connection = get_connection()
    cursor = connection.cursor()

    # 1️ Ingest CSV
    ingest_csv(cursor, connection)

    # 2️ Product Performance
    cursor.execute("""
        SELECT product_name,
               SUM(quantity),
               SUM(quantity * price)
        FROM sales_data
        GROUP BY product_name
        ORDER BY SUM(quantity * price) DESC;
    """)
    product_records = cursor.fetchall()

    # 3️ Overall Performance
    cursor.execute("""
        SELECT SUM(quantity),
               SUM(quantity * price)
        FROM sales_data;
    """)
    overall_data = cursor.fetchone()

    # 4️ Daily Revenue
    cursor.execute("""
        SELECT sale_date,
               SUM(quantity * price)
        FROM sales_data
        GROUP BY sale_date
        ORDER BY sale_date;
    """)
    daily_data = cursor.fetchall()

    # 5️ Analysis
    trend_results = analyze_daily_trend(daily_data)
    prediction = predict_next_day_revenue(daily_data)

    # 6️ Export JSON Report
    export_report(product_records, overall_data, trend_results, prediction)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()