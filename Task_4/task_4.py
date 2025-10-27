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
    name, phone = args
    if name in contacts:
        return "This contact already exists. Use 'change' to update."
    contacts[name] = phone
    return f"Contact '{name}' added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Phone number for '{name}' updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    print("Available commands: add, change, phone, all, exit")

    while True:
        command = input("Enter a command: ").strip().lower()

        if command == "exit":
            print("Good bye!")
            break

        elif command == "close":
            print("Good bye!")
            break

        elif command == "add":
            args = input("Enter name and phone: ").split()
            print(add_contact(args, contacts))

        elif command == "change":
            args = input("Enter name and new phone: ").split()
            print(change_contact(args, contacts))

        elif command == "phone":
            args = input("Enter user name: ").split()
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Unknown command. Try again.")


if __name__ == "__main__":
    main()