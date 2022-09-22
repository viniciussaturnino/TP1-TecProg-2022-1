from datetime import datetime


def get_formated_datetime(date : str, format :str = "%H:%M:%S"):
    return datetime.strptime(date, format)