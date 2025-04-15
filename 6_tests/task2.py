documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }


def get_name(doc_number):
    name = 'Документ не найден'
    for document in documents:
        if doc_number == document["number"]:
            name = document["name"]
    return name


def get_directory(doc_number):
    directory_number = 'Полки с таким документом не найдено'
    for number, directory in directories.items():
        if doc_number in directory:
            directory_number = number
    return directory_number


def add(document_type, number, name, shelf_number):
    directories[str(shelf_number)].append(number)
    dict_document = {
        "type": document_type,
        "number": number,
        "name": name,
    }
    documents.append(dict_document)

if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))