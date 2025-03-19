import datetime

from application.db.people import *
from application.salary import *

if __name__ == "__main__":
    today = datetime.datetime.now()
    people(today)
    salary(today)