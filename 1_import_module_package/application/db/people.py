import art

def people(date):
    print(f"Сегодня {date:%Y-%m-%d}. Выполняется people")
    art.tprint("PEOPLE", font="Block")
