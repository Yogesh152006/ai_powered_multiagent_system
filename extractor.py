import re

def extract_information(title):

    info = {}

    title_lower = title.lower()

    if "raised" in title_lower:

        funding = re.findall(r"\$\d+[A-Za-z ]*", title)

        info["Funding"] = funding[0] if funding else "Detected"

    if "hire" in title_lower:

        info["Hiring"] = "Yes"

    if "launch" in title_lower:

        info["Launch"] = "Yes"

    if "partner" in title_lower:

        info["Partnership"] = "Yes"

    if "acquire" in title_lower:

        info["Acquisition"] = "Yes"

    return info