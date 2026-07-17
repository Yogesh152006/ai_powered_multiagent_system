def generate_insight(info):

    insights = []

    if "Funding" in info:
        insights.append("Company has secured funding.")

    if "Hiring" in info:
        insights.append("Company is expanding.")

    if "Launch" in info:
        insights.append("Recently launched a product.")

    if "Partnership" in info:
        insights.append("Building strategic partnerships.")

    if "Acquisition" in info:
        insights.append("Expanding through acquisitions.")

    if len(insights) == 0:
        insights.append("Monitor startup for future developments.")

    return " ".join(insights)