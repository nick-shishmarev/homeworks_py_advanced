import datetime

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == "__main__":
    today = datetime.datetime.now()
    get_employees(today)
    calculate_salary(today)
