from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_age_given_birthdate_and_current_date(birth_date, current_date):
    first, last = datetime.strptime(birth_date, "%Y-%m-%d"), datetime.strptime(current_date, "%Y-%m-%d")
    return relativedelta(last, first).years
