import logging
from datetime import datetime

import pandas as pd


def calculate_age(date_of_birth):
    current_year = datetime.now().year
    date_of_birth = pd.to_datetime(date_of_birth)
    return current_year - date_of_birth.year


def age_rule(data):
    logging.info("Age rule >> Start")
    data["age"] = data["date_of_birth"].apply(calculate_age)
    data["age_rule_pass"] = (data["age"] >= 18).astype(int)
    logging.info("Age rule >> End")
    return data
