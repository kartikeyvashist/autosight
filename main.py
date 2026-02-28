from db import get_connection
from ingestion import ingest_csv
from analysis import analyze_daily_trend, predict_next_day_revenue
from reporting import export_report
from Visualization import generate_revenue_chart
from logger_config import setup_logger
import argparse

logger = setup_logger()
def main():
    parser = argparse.ArgumentParser(description="AutoSight CLI Controller")
    parser.add_argument("--ingest", action="store_true", help="Run CSV ingestion")
    parser.add_argument("--analyze", action="store_true", help="Run analytics")
    parser.add_argument("--visualize", action="store_true", help="Generate revenue chart")
    parser.add_argument("--report", action="store_true", help="Export JSON report")
    parser.add_argument("--full", action="store_true", help="Run full pipeline")
    args = parser.parse_args()
    logger.info("Starting Autosight Pipeline")
    connection = get_connection()
    if args.full:
        print("Running full pipeline...")
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
    generate_revenue_chart(daily_data)

    # 6️ Export JSON Report
    export_report(product_records, overall_data, trend_results, prediction)
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()