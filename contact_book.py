# Contact Book using List of Dictionaries

contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)
        print("Contact added successfully!")

    # View Contacts
    elif choice == '2':
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    # Search Contact
    elif choice == '3':
        search_name = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact['name'].lower() == search_name.lower():
                print(f"Found -> Name: {contact['name']}, Phone: {contact['phone']}")
                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete Contact
    elif choice == '4':
        delete_name = input("Enter name to delete: ")

        found = False

        for contact in contacts:
            if contact['name'].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    # Exit
    elif choice == '5':
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Please try again.")