import matplotlib.pyplot as plt
import logging
logger = logging.getLogger(__name__)

def generate_revenue_chart(daily_data):
    logger.info("Starting generating graph")
    dates = [str(row[0]) for row in daily_data]
    revenue = [float(row[1]) for row in daily_data]

    plt.figure()
    plt.plot(dates,revenue, marker='o')

    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.title("Daily Revenue Trend")

    plt.xticks(rotation=45)
    plt.tight_layout()

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
