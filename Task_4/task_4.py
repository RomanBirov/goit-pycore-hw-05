def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError:
            return "This contact does not exist."

        except ValueError:
            return "Give me name and phone please."

        except IndexError:
            return "Enter user name."

    return inner


@input_error
def add_contact(args, contacts):
    # waiting for: [name, phone]
    name, phone = args  # кине ValueError якщо не 2 аргументи
    if name in contacts:
        return "This contact already exists. Use 'change' to update."
    contacts[name] = phone
    return f"Contact '{name}' added."


@input_error
def change_contact(args, contacts):
    # waiting for: [name, phone]
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Phone number for '{name}' updated."


@input_error
def show_phone(args, contacts):
    # waiting for: [name]
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def parse_input(line: str):
    """Повертає (command, args_list). Напр.: 'add Bob 123' -> ('add', ['Bob','123'])"""
    parts = line.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    print("Available commands: add, change, phone, all, exit/close, hello")

    while True:
        raw = input("Enter a command: ")
        command, args = parse_input(raw)

        if command in ("exit", "close"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            # якщо аргументів немає — попросимо їх окремо
            if not args:
                args = input("Enter name and phone: ").split()
            print(add_contact(args, contacts))

        elif command == "change":
            if not args:
                args = input("Enter name and new phone: ").split()
            print(change_contact(args, contacts))

        elif command == "phone":
            if not args:
                args = input("Enter user name: ").split()
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Unknown command. Try again.")


if __name__ == "__main__":
    main()