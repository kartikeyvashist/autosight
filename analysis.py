import logging
logger = logging.getLogger(__name__)
def analyze_daily_trend(daily_data):
    logger.info("Starting Daily trends analysis")
    trend_results = []                  #   here we have created a result empty list to store the values of the data

    for i in range(1, len(daily_data)):         #   here we itrate into daily data with a range 1 beacuse date cant be start from 0, 1-now
        previous_day = daily_data[i - 1]        #   here we have i which is the current date we do -1 which automatically gives us pre
        current_day = daily_data[i]             #   and i is our current date

        previous_revenue = float(previous_day[1])   #   here we will store revenue into days, day wise (prev_rev)   
        current_revenue = float(current_day[1])     #   here we have current rev into current day

        change = current_revenue - previous_revenue     #   then we need to analyze if something changed in revenue or not if yes then how much
        percentage_change = (change / previous_revenue) * 100 if previous_revenue != 0 else 0   #   here we just calculate the percentage 

#   here we have typed (if previous_revenue != 0 else 0) That raises ZeroDivisionError In production systems, one unhandled division by zero can:
#   Break scheduled jobs
#   Stop dashboards from updating
#   Corrupt automation workflows
#   Trigger monitoring alerts

        if percentage_change > 20:      #    now we apply the condition which is if percentage is higher than 0 then show +ive 
            insight = "Strong upward growth detected."
        elif percentage_change > 0:    #    and if lower which is obviously would be a -ive number
            insight = "Moderate growth observed."
        elif percentage_change < -20:
            insight = "Significant revenue drop. Immediate attention required."
        elif percentage_change < 0:
            insight = "Slight revenue decline."
        else:
            insight = "Stable"           #    else we say it is stable no change (low chance)

        trend_results.append({
            "from": str(previous_day[0]),
            "to": str(current_day[0]),
            "percentage_change": round(percentage_change, 2),   #   we learnt round which just slice the number after decimal till we provide num
            "insight": insight
        })
    logger.info("Daily trend analysis completed successfully")
    return trend_results    #   now we just simply return our trend result list outside the function


def predict_next_day_revenue(daily_data):       #   in data-engineering models according to F-ML predicting next day revenue is possible mathametically     
    logger.info("starting predicting revenue")                    
    revenues = [float(day[1]) for day in daily_data]    #   so we created revenue varible and store only the date and we know our daily data is in daily data function

    if len(revenues) < 2:
        return "Not enough data"

    changes = []
    for i in range(1, len(revenues)):
        changes.append(revenues[i] - revenues[i - 1])
    recent_changes = changes[-2:] if len(changes) >= 2 else changes
    avg_change = sum(recent_changes) / len(recent_changes)
    predicted_revenue = revenues[-1] + avg_change

    if predicted_revenue < 0:
        predicted_revenue = 0

    logger.info(f"Predicting generated: {predicted_revenue}")
    return round(predicted_revenue, 2)