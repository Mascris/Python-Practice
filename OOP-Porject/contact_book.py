class Contact:
    def __init__(self,name: str, phone_number: str,email=None,address=None) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def update_info(self,phone_number=None,email=None,address=None):
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def display_info(self):
        print(f"M.{self.name},who's living in {self.address}, phone number:{self.phone_number}, email: {self.email}.")

class ContactBook:
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self,name: str,phone_number: str,email=None,address=None):
        if name in self.contacts:
            print("this name is already been taken")
            return
        new_contact = Contact(name,phone_number,email,address)
        self.contacts[name] = new_contact

    def find_contact(self,name):
        return self.contacts.get(name,None)

    def update_contact(self,name: str,new_phone=None,new_email=None):
        self.name = name
        self.phone_number = new_phone
        self.email = new_email
        
        contact = self.find_contact(name)
        
