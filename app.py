from flask import Flask, jsonify
from db import get_connection
from analysis import analyze_daily_trend, predict_next_day_revenue

app = Flask(__name__)

@app.route("/predict")
def predict_data():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT sale_date, SUM(quantity*price)
        FROM sales_data
        GROUP BY sale_date
        ORDER BY sale_date
""")
    daily_data = cursor.fetchall()
    cursor.close()
    connection.close()

    predicted_revenue = predict_next_day_revenue(daily_data)
    return jsonify({"Predicted next day revenue": predicted_revenue})

@app.route("/")
def home():
    return "Welcome to Autosight API!"

@app.route("/summary")
def summary():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT product_name, SUM(quantity), SUM(quantity*price)
        FROM sales_data
        GROUP BY product_name
        ORDER BY SUM(quantity*price) DESC;        
""")
    data = cursor.fetchall()
    return jsonify(data)
@app.route("/full-report")
def full_report():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT product_name, SUM(quantity), SUM(quantity*price)
        FROM sales_data
        GROUP BY product_name
        ORDER BY SUM(quantity*price) DESC
""")
    product_records = cursor.fetchall()
    cursor.execute("""
        SELECT SUM(quantity), SUM(quantity*price)
        FROM sales_data;
    """)
    overall_data = cursor.fetchone()

    cursor.execute("""
        SELECT sale_date, SUM(quantity*price)
        FROM sales_data
        GROUP BY sale_date
        ORDER BY sale_date;
    """)
    daily_data = cursor.fetchall()
    cursor.close()
    connection.close()
    trend_results = analyze_daily_trend(daily_data)
    prediction = predict_next_day_revenue(daily_data)

    report = {
        "executive_summary": {
            "overall_quantity": overall_data[0],
            "overall_revenue": overall_data[1],
            "top_product": product_records[0][0],
            "top_revenue": product_records[0][2],
            "lowest_product": product_records[-1][0],
            "lowest_revenue": product_records[-1][2]
        },
        "trend_analysis": trend_results,
        "predicted_next_day_revenue": prediction
    }
    return jsonify(report)


if __name__ == "__main__":
    app.run(debug=True)