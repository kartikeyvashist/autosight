import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import logging
from datetime import datetime
logger = logging.getLogger(__name__)

def generate_revenue_chart(daily_data):
    logger.info("Starting generating graph")
    dates = [datetime.strptime(str(row[0]), "%Y-%m-%d") for row in daily_data]
    revenue = [float(row[1]) for row in daily_data]

    plt.figure(figsize=(10,5))
    plt.plot(dates,revenue, marker='o')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d-%b"))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())


    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.xlabel("Date", fontsize=8)
    plt.ylabel("Revenue", fontsize=8)
    plt.title("Daily Revenue Trend", fontsize=14, fontweight='bold')

    max_revenue = max(revenue)
    min_revenue = min(revenue)

    max_index = revenue.index(max_revenue)
    min_index = revenue.index(min_revenue)

    plt.scatter(dates[max_index], max_revenue)
    plt.scatter(dates[min_index], min_revenue)

    plt.text(dates[max_index], max_revenue, "Highest")
    plt.text(dates[min_index], min_revenue, "Lowest")

    plt.savefig("revenue.png")
    plt.close()

    logger.info("revenue chart saved as revenue.png")
