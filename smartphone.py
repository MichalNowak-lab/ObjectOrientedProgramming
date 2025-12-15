import contact, contact_list
contacts = contact_list.Contact_list()
contacts.add_contact(contact.Contact('John Brown', 'brown@onet.pl',555234000))
contacts.add_contact(contact.Contact('Anna May', 'am@o2.pl',232000199))
contacts.add_contact(contact.Contact('George Small', 'smallg@google.pl ',222999100))
contacts.add_contact(contact.Contact('Paola Big', 'bigpaola@poczta.pl',100200300))
contacts.display()