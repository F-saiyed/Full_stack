#Step 1: Setting Up the Contact Class

from datetime import datetime  #Importing the date and time library for this class
import re

class Contact:
    #Defining the initialize method
    def __init__(self, first_name, last_name, phone_number, email=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

#Defining the update method
    def update(self, first_name=None, last_name=None, phone_number=None, email=None, address=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"
