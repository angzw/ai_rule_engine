import logging

import pandas as pd


def check_death_date(death_date):
    # Check for null or NaT (Not a Time)
    if pd.isna(death_date):
        return False

    # Check if the string is empty or blank
    if isinstance(death_date, str) and not death_date.strip():
        return False

    return True


def living_status_rule(data):
    logging.info("Living status rule >> Start")
    data["death_date_valid"] = data["death_date"].apply(check_death_date)
    data["living_status_rule_pass"] = (~data["death_date_valid"]).astype(int)
    logging.info("Living status rule >> End")
    return data
