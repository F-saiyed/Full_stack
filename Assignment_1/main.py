#Step 3: Command-Line Interface

from phonebook import PhoneBook
from contact import Contact
import csv

class Contact:
    def __init__(self, first_name, last_name, phone, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def list_contacts(self):
        return self.contacts
    
    def import_contacts_from_csv(self, file_path):
        try:
            with open(file_path, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    contact = Contact(
                        first_name=row['First_Name'],
                        last_name=row['Last_Name'],
                        phone=row['Phone_Number'],
                        email=row['Email_Address'],
                        address=row['Address']
                    )
                    self.add_contact(contact)
            print(f"{len(self.contacts)} contacts added successfully from {file_path}.")
        except Exception as e:
            print(f"Error importing contacts from CSV: {e}")

    def find_contact(self, **kwargs):
        results = []
        for contact in self.contacts:
            match = True
            for key, value in kwargs.items():
                if getattr(contact, key, None) != value:
                    match = False
                    break
            if match:
                results.append(contact)
        return results

    def update_contact(self, contact, **kwargs):
        for key, value in kwargs.items():
            if value:
                setattr(contact, key, value)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Phone Number':<15} {'Email':<25} {'Address':<30}")
        print("="*105)
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx:<5} {contact.first_name:<15} {contact.last_name:<15} {contact.phone:<15} {contact.email:<25} {contact.address:<30}")
        print(f"\nTotal contacts: {len(contacts)}")

def main():
    phonebook = PhoneBook() #Instance of Phonebook class

    while True:
        print("\nPhone Book Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Import Contacts from CSV")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(first_name, last_name, phone, email, address)
            phonebook.add_contact(contact)
            print("Contact added successfully.")
            
        elif choice == '2':
            contacts = phonebook.list_contacts()
            display_contacts(contacts)

        elif choice == '3':
            search_field = input("Search by (first_name, last_name, phone): ")
            search_value = input(f"Enter {search_field}: ")
            results = phonebook.find_contact(**{search_field: search_value})
            display_contacts(results)

        elif choice == '4':
            search_field = input("Search by (first_name, last_name, phone): ")
            search_value = input(f"Enter {search_field}: ")
            results = phonebook.find_contact(**{search_field: search_value})
            if results:
                contact = results[0]
                print(f"Updating contact: {contact.first_name} {contact.last_name}")
                first_name = input("First Name (leave blank to keep current): ")
                last_name = input("Last Name (leave blank to keep current): ")
                phone_number = input("Phone Number (leave blank to keep current): ")
                email = input("Email (leave blank to keep current): ")
                address = input("Address (leave blank to keep current): ")
                phonebook.update_contact(contact, first_name=first_name, last_name=last_name, phone=phone_number, email=email, address=address)
                print("Contact updated.")
            else:
                print("Contact not found.")

        elif choice == '5':
            search_field = input("Search by (first_name, last_name, phone): ")
            search_value = input(f"Enter {search_field}: ")
            results = phonebook.find_contact(**{search_field: search_value})
            if results:
                contact = results[0]
                phonebook.delete_contact(contact)
                print("Contact deleted.")
            else:
                print("Contact not found.")

        elif choice == '6':
            file_path = input("Enter CSV file path: ")
            phonebook.import_contacts_from_csv(file_path)

        elif choice == '7':
            print("Exiting Phone Book Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
