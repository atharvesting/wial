from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_age_given_birthdate_and_current_date(birth_date, current_date):
    first, last = datetime.strptime(birth_date, "%Y-%m-%d"), datetime.strptime(current_date, "%Y-%m-%d")
    return relativedelta(last, first).years

def one_element_tuple_list_to_normal_list(my_list: list) -> list:
    return [tup[0] for tup in my_list]

def check_rating_validity(rating: int):
    if rating in range(-2, 3) and "." not in str(rating):
        return True
    return False