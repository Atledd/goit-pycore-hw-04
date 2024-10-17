def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_contact(args, contacts):
    if len(args) != 1:
        return "Please, make sure that the following command was used: phone 'name'"
    name = args[0]
    return contacts.get(name, f"No contact for {name}")    #де f"No contact for {name}" - значення за замовчуванням

def change_contact(args, contacts):
    if len(args) != 2:
        return "Please, make sure that the following command was used: change 'name' 'new_number'"
    name, phone = args
    if name not in contacts:
        return f"No contact with name {name} was found"
    contacts[name] = phone
    return "Contact list updated."

def show_all(contacts):
    if not contacts:
        return "Error! No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def get_help(cmd_list):
    return "\n".join(f"{func_name}: {description}" for func_name, description in cmd_list.items())

def main():
    contacts = {}
    cmd_list = {"add_contact": "adds a new contact",
                "show_contatc": "shows a contatc if it exists",
                "change_contact": "allows to change existing contact",
                "show_all": "shows the full list of contatcs"}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(get_help(cmd_list))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()