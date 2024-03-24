def input_error(func):                                      # Creation decorator for functions
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:                                  # Processing of ValueError
            return "Please, Enter Name and Phone."
        except KeyError:                                    # Processing of KeyError
            return "Contact is missing."
        except IndexError:                                  # Processing of IndexError
            return "Please, Enter Name"
    return inner


@input_error
def parse_input(user_input):                                # Function for creating commands and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):                            # Function for adding contact to dict
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):                         # Function for changing existing contact
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact is missing."

@input_error       
def show_phone(args, contacts):                             # Function for showing existing contact by username
    name = args[0]
    return contacts[name]



def main():                                                 # main function for output result
    contacts = {}
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
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

