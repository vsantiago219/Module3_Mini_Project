import re
import os

# Dictionary to store contact information
contacts = {}

# Regular expressions for validation
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PHONE_REGEX = r'^\d{3}-\d{3}-\d{4}$'

def validate_email(email):
    """Validate email format using regex"""
    return re.match(EMAIL_REGEX, email)

def validate_phone(phone):
    """Validate phone format using regex"""
    return re.match(PHONE_REGEX, phone)

def add_contact():
    """Add a new contact to the system"""
    print("\n--- Add a New Contact ---")
    name = input("Enter the name: ")
    phone = input("Enter phone number (XXX-XXX-XXXX): ")
    email = input("Enter email address: ").lower()
    
    if not validate_email(email):
        print("Invalid email format!")
        return
    if not validate_phone(phone):
        print("Invalid phone number format!")
        return
    
    contacts[email] = {
        "name": name,
        "phone": phone,
        "email": email,
        "notes": input("Enter notes: ").lower()
    }
    print("Contact added successfully!")

def edit_contact():
    """Edit an existing contact's details"""
    print("\n--- Edit a Contact ---")
    email = input("Enter the email address of the contact you want to edit: ")
    if email not in contacts:
        print("Contact not found!")
        return
    
    print("Leave fields blank if you don't want to change them.")
    name = input(f"Enter new name (current: {contacts[email]['name']}): ") or contacts[email]['name']
    phone = input(f"Enter new phone (current: {contacts[email]['phone']}): ") or contacts[email]['phone']
    notes = input(f"Enter new notes (current: {contacts[email]['notes']}): ") or contacts[email]['notes']
    
    contacts[email].update({
        "name": name,
        "phone": phone,
        "notes": notes
    })
    print("Contact update successfully!")

def delete_contact():
    """Delete a contact from the system"""
    print("\n--- Delete a Contact ---")
    email = input("Enter the email address of the contact you want to delete: ")
    if email not in contacts:
        print("Contact not found!")
        return
    del contacts[email]
    print("Contact deleted successfully!")

def search_contact():
    """Search for a contact by email"""
    print("\n--- Search for a Contact ---")
    email = input("Enter the email address of the contact to search for: ")
    if email not in contacts:
        print("Contact not found!")
        return
    contact = contacts[email]
    print(f"\nName: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Notes: {contact['notes']}")

def display_contacts():
    """Display all contacts"""
    print("\n--- All Contacts ---")
    for email, contact in contacts.items():
        print(f"\nName: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Notes: {contact['notes']}")

def export_contacts():
    """Export contacts to a text file"""
    with open('contacts.txt', 'w') as file:
        for email, contact in contacts.items():
            file.write(f"{contact['name']},{contact['phone']},{contact['email']},{contact['address']},{contact['notes']}\n")
    print("Contacts exported to contacts.txt")

def import_contacts():
    """Import contacts from a text file"""
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                name, phone, email, address, notes = line.strip().split(',')
                contacts[email] = {
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "address": address,
                    "notes": notes
                }
        print("Contacts imported successfully!")
    except FileNotFoundError:
        print("contacts.txt file not found.")

def main():
    """Main function to display the menu and handle user input"""
    while True:
        print("\nWelcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text filey.p")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            import_contacts()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
