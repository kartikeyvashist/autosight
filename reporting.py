import json
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

def export_report(product_data, overall_data, trend_data, prediction):
    logger.info("Starting generating Report")
    report = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "executive_summary": {
            "top_product": product_data[0][0] if product_data else None,
            "top_revenue": float(product_data[0][2]) if product_data else 0,
            "lowest_product": product_data[-1][0] if product_data else None,
            "lowest_revenue": float(product_data[-1][2]) if product_data else 0,
            "overall_quantity": overall_data[0],
            "overall_revenue": float(overall_data[1])
        },

        "product_performance": [
            {
                "product": p,
                "total_quantity": q,
                "total_revenue": float(r)
            }
            for p, q, r in product_data
        ],

        "daily_trends": trend_data,

        "next_day_prediction": prediction
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    logger.info("Report exported successfully → report.json")