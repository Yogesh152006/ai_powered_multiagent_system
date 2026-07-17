def predict_growth(title):

    title = title.lower()

    if "series c" in title:
        return "Late Stage"

    elif "series b" in title:
        return "Growth Stage"

    elif "series a" in title:
        return "Early Growth"

    elif "seed" in title:
        return "Seed"

    else:
        return "Unknown"