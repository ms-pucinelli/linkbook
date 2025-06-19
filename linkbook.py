# Gerenciador de contatos - Abril 2025 - Pamela Gomes

# {chave para dicionário} #[colchete para lista]

contacts = [] #starting my empty list
while True: 
    user_input = int(input("What do you want to do? Please, select a number -  (1) Add, (2) View all, (3) Search, (4) Delete, (5) Update, (6) Exit: "))

    if user_input == 1: # Add info (1)
        name = str(input("Name: ")).lower()
        email = str(input("Email: ")).lower()
        phone = str(input("Phone: "))
        profession = str(input("Profession: ")).title()
        print() 

        person_info = {
            "name" : name,
            "email" : email,
            "phone" : phone,
            "profession" : profession,
        }
        contacts.append(person_info)

    elif user_input == 2: # view all (2)
        if len(contacts) == 0:
            print("Oh now. We don't have any contacts to display.")
            print()
        else:
            for contact in contacts:
                print(f"Name: {contact.get("name").title()}")
                print(f"Email: {contact.get("email")}")
                print(f"Phone Number: {contact.get("phone")}")
                print(f"Profession: {contact.get("profession").title()}")
                print()

    elif user_input == 3: # Search (3)
        want_to_search = input("Who are you looking for? ").lower()
        found = False
        for contact in contacts:
            if want_to_search == contact.get("name").lower():
                print(f"Name: {contact.get("name").title()}")
                print(f"Email: {contact.get("email")}")
                print(f"Phone Number: {contact.get("phone")}")
                print(f"Profession: {contact.get("profession").title()}")
                found = True
                print()
                break

        if not found:
            print("Unable to locate this contact. Please, try again.")

    elif user_input == 4: # Delete (4)
            want_to_delete = input("Who do you want delete? ").lower()
            found = False #flag
            for contact in contacts:
                if want_to_delete == contact.get("name").lower():
                    contacts.remove(contact)
                    print("Contact successfully removed.")
                    print()
                    found = True
                    break

            if not found:
                print("Unable to locate and delete this contact. Please, try again.")
                print()

    elif user_input == 5: # Update (5)
        want_to_update = input("Who do you want to update the information? ").lower()
        found = False
        for contact in contacts:
            if want_to_update == contact.get("name").lower():
                new_name = str(input("Name: ")).lower()
                new_email = str(input("Email: ")).lower()
                new_phone = str(input("Phone: "))
                new_profession = str(input("Profession: ")).title()

                contact["name"] = new_name.title()
                contact["email"] = new_email
                contact["phone"] = new_phone
                contact["profession"] = new_profession.title()
                found = True
                print("Information successfully updated.")
                print()
                break
        if not found:
                print("Unable to locate and update this contact. Please, try again.")
                print()
            
    elif user_input == 6: # Exit (6)
        print("Thanks for using our program!")
        print()
        break