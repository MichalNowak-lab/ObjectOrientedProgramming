
class Contact_list:
    def __init__(self):
        self.contacts=[]
    def add_contact(self,contact):
        self.contacts.append(contact)
    def display(self):
        for data in self.contacts:
            print(data)