import datetime

from application.db.people import people
from application.salary import salary

if __name__ == "__main__":
    today = datetime.datetime.now()
    people(today)
    salary(today)
