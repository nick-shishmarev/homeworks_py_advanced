import datetime

from application.db.people import *
from application.salary import *

if __name__ == "__main__":
    today = datetime.datetime.now()
    get_employees(today)
    calculate_salary(today)