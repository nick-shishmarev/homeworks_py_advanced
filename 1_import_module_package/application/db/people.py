import art

def get_employees(date):
    print(f"Сегодня {date:%Y-%m-%d}. Выполняется get_employees")
    art.tprint("GET_EMPLOYEES", font="Block")
