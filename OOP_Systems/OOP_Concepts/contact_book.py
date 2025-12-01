class Contact:
    def __init__(self, name: str, phone_number: str, email=None, address=None) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def update_info(self, phone_number=None, email=None, address=None):
        if phone_number is not None:
            self.phone_number = phone_number
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address

    def display_info(self):
        print(f"M.{self.name}, living in {self.address}, phone: {self.phone_number}, email: {self.email}.")

class ContactBook:
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self, name: str, phone_number: str, email=None, address=None):
        if name in self.contacts:
            print("This name is already taken.")
            return

        new_contact = Contact(name, phone_number, email, address)
        self.contacts[name] = new_contact

    def find_contact(self, name):
        return self.contacts.get(name, None)

    def update_contact(self, name: str, new_phone=None, new_email=None, new_address=None):
        contact = self.find_contact(name)
        if not contact:
            print("Contact not found!")
            return


        contact.update_info(new_phone, new_email, new_address)

        print(f"{name} has been updated successfully")

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if not contact:
            print(f"{name} not found!")
            return

        del self.contacts[name]
        print(f"{name} got deleted with success.")

    def list_all_contacts(self):
        if not self.contacts:
            print("contacts book is empty!")
            return

        for contact in self.contacts.values():
            contact.display_info()

def main_menu(contactbook):
    while True:
        print("\n=== GradeBook Menu ===")
        print("1 - Add a new contact")
        print("2 - find contact")
        print("3 - Update contact")
        print("4 - delete contact")
        print("5 - list all contacts")
        print("6 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Contact name: ")
            phone_number = input("Phone number: ")
            email = input("email: ")
            address = input("address: ")
            contactbook.add_contact(name,phone_number,email,address)

        elif choice == "2":
            name = input("Contact name:")
            contact = contactbook.find_contact(name)
            if contact:
                contact.display_info()
            else:
                print("contact not found")

        elif choice == "3":
            name = input("Contact: ")
            phone_number = input("Phone number: ") or None
            email = input("email: ") or None
            address = input("address: ") or None
            contactbook.update_contact(name,phone_number,email,address)

        elif choice == "4":
            name = input("Contact: ")
            contactbook.delete_contact(name)

        elif choice == "5":
            contactbook.list_all_contacts()

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid input.")

if __name__ == "__main__":
    contactbook = ContactBook()
    main_menu(contactbook)


