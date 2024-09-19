#Step 2: Setting Up the PhoneBook Class

from datetime import datetime
import csv

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Debug: Current contacts list: {self.contacts}")


    def import_contacts_from_csv(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contact = Contact(row['First Name'], row['Last Name'], row['Phone Number'], row.get('Email'), row.get('Address'))
                self.add_contact(contact)

    def find_contact(self, **kwargs):
        results = []
        for contact in self.contacts:
            match = True
            for key, value in kwargs.items():
                if not getattr(contact, key).lower().startswith(value.lower()):
                    match = False
                    break
            if match:
                results.append(contact)
        return results

    def update_contact(self, contact, **kwargs):
        contact.update(**kwargs)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def list_contacts(self):
        return sorted(self.contacts, key=lambda x: x.last_name)

    def log_operation(self, operation):
        with open('phonebook.log', 'a') as logfile:
            logfile.write(f"{datetime.now()}: {operation}\n")
    

