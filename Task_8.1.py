import csv

class Contact:
    def __init__(self, last_name, first_name, phone, description):
        self.last_name = last_name
        self.first_name = first_name
        self.phone = phone
        self.description = description

class PhoneBook:
    def __init__(self):
        self.contacts = []
        
    def create_contact(self, last_name, first_name, phone, description):
        contact = Contact(last_name, first_name, phone, description)
        self.contacts.append(contact)
        
    def read_contacts(self, last_name):
        found_contacts = []
        for contact in self.contacts:
            if contact.last_name.lower().startswith(last_name.lower()):
                found_contacts.append(contact)
        return found_contacts
        
    def update_contact(self, last_name, first_name, phone, description):
        for contact in self.contacts:
            if contact.last_name.lower() == last_name.lower() and contact.first_name.lower() == first_name.lower():
                contact.phone = phone
                contact.description = description
                return True
        return False
        
    def delete_contact(self, last_name, first_name):
        for contact in self.contacts:
            if contact.last_name.lower() == last_name.lower() and contact.first_name.lower() == first_name.lower():
                self.contacts.remove(contact)
                return True
        return False
        
    def export_to_csv(self, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for contact in self.contacts:
                writer.writerow([contact.last_name, contact.first_name, contact.phone, contact.description])
                
    def import_from_csv(self, file_path):
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.create_contact(row[0], row[1], row[2], row[3])