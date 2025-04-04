import csv
import re


def make_phone(ph: str):
    # Приведение номеров телефонов к виду +7(999)999-99-99 доб.9999
    if ph == "phone":
        return ph
    pattern = r'(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d\d)[-\s]*(\d\d)\s*\(?(доб.)?\s*(\d*)\)?'
    repl_pattern = r'+7(\2)\3-\4-\5 \6\7'

    if re.match(pattern, ph):
        ph = ph.replace(" ", "")
        res = re.sub(pattern, repl_pattern, ph).strip()
    else:
        res = ''

    return res


def pack_lst_by_nam(lst_in: list[str]):
    # Сжатие списка по Фамилии и Имени

    l_name_fix, f_name_fix, s_name_fix, org_fix, pos_fix, phone_fix, email_fix = lst_in[0]
    out_lst = []
    for pers in lst_in:
        l_name_cur, f_name_cur, s_name_cur, org_cur, pos_cur, phone_cur, email_cur = pers
        if l_name_fix == l_name_cur and f_name_fix == f_name_cur:
            s_name_fix = s_name_fix or s_name_cur
            org_fix = org_fix or org_cur
            pos_fix = pos_fix or pos_cur
            phone_fix = phone_fix or phone_cur
            email_fix = email_fix or email_cur
        else:
            if l_name_fix:
                out_lst.append([l_name_fix, f_name_fix, s_name_fix, org_fix, pos_fix, phone_fix, email_fix])
            l_name_fix, f_name_fix, s_name_fix, org_fix, pos_fix, phone_fix, email_fix = (
                l_name_cur, f_name_cur, s_name_cur, org_cur, pos_cur, phone_cur, email_cur
            )
    out_lst.append([l_name_fix, f_name_fix, s_name_fix, org_fix, pos_fix, phone_fix, email_fix])
    return out_lst


def main(file_name_in: str, file_name_out: str):

    with open(file_name_in, encoding="utf-8") as f:
        contacts_list = list(csv.reader(f, delimiter=","))

    # TODO 1: выполните пункты 1-3 ДЗ

    # 1. Обработка ФИО
    fio_lst = [' '.join(a[:3]).split() for a in contacts_list]
    for a in fio_lst:
        if len(a) < 3:
            a.append('')
    tail_lst = [a[3:] for a in contacts_list]
    # 2. Обработка номеров телефонов
    for c in tail_lst:
        c[2] = make_phone(c[2])
    result_lst = [a + b for a, b in zip(fio_lst, tail_lst)]
    result_lst.sort(key=lambda x: x[0] + x[1] + x[2])

    # 3. Сжатие списка по Фамилии и Имени
    lst = pack_lst_by_nam(result_lst)

    for line in lst:
        l1, l2, l3, l4, l5, l6, l7 = line
        print(f"{l1:20}{l2:20}{l3:20}{l4:20}{l6:30}{l7:30}{l5}")

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open(file_name_out, "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',', lineterminator="\r")
        datawriter.writerows(lst)


if __name__ == "__main__":
    file_in = "phonebook_raw.csv"
    file_out = "phonebook.csv"
    main(file_in, file_out)
