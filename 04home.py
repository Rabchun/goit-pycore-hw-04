import sys

contacts = {}

def parse_input(command):

    parts = command.lower().split()
    return parts[0], parts[1:]

def add_contact(name, phone):
    """Додає контакт до словника."""
    contacts[name] = phone
    print(f"Контакт {name} з номером {phone} додано.")

def change_contact(name, new_phone):

    if name in contacts:
        contacts[name] = new_phone
        print(f"Номер телефону для {name} змінено на {new_phone}.")
    else:
        print(f"Контакт {name} не знайдено.")

def show_phone(name):

    if name in contacts:
        print(f"Номер телефону для {name}: {contacts[name]}")
    else:
        print(f"Контакт {name} не знайдено.")

def show_all_contacts():

    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Список контактів пустий.")

def main():
    while True:
        command = input("Введіть команду (add, change, show, show_all, exit): ")
        command, args = parse_input(command)

        if command == "add":
            if len(args) == 2:
                add_contact(args[0], args[1])
            else:
                print("Неправильний формат команди. Використовуйте: add <ім'я> <номер>")
        elif command == "change":
            if len(args) == 2:
                change_contact(args[0], args[1])
            else:
                print("Неправильний формат команди. Використовуйте: change <ім'я> <новий номер>")
        elif command == "show":
            if len(args) == 1:
                show_phone(args[0])
            else:
                print("Неправильний формат команди. Використовуйте: show <ім'я>")
        elif command == "show_all":
            show_all_contacts()
        elif command in ["exit", "close"]:
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()