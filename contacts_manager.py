# Contact Management System
# Name: Shreya Mundhe

import json
import re
import csv
from datetime import datetime

FILE_NAME = "contacts_data.json"


# ---------------- VALIDATION FUNCTIONS ---------------- #

def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None


def validate_email(email):
    if email == "":
        return True
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


# ---------------- FILE OPERATIONS ---------------- #

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ---------------- CRUD FUNCTIONS ---------------- #

def add_contact(contacts):
    print("\n--- ADD CONTACT ---")

    while True:
        name = input("Enter name: ").strip()
        if name:
            if name in contacts:
                print("Contact already exists!")
                return contacts
            break
        print("Name cannot be empty!")

    while True:
        phone = input("Enter phone: ")
        valid, phone = validate_phone(phone)
        if valid:
            break
        print("Invalid phone! Enter 10-15 digits.")

    while True:
        email = input("Enter email (optional): ").strip()
        if validate_email(email):
            break
        print("Invalid email!")

    address = input("Enter address (optional): ").strip()
    group = input("Enter group (Friends/Family/Work): ").strip() or "Other"

    contacts[name] = {
        "phone": phone,
        "email": email if email else None,
        "address": address if address else None,
        "group": group,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    save_contacts(contacts)
    print("✅ Contact added successfully!")
    return contacts


def search_contact(contacts):
    term = input("Enter name to search: ").lower()
    results = {}

    for name, data in contacts.items():
        if term in name.lower():
            results[name] = data

    if not results:
        print("No contacts found.")
        return

    for name, data in results.items():
        print(f"\n{name}")
        print(f"Phone: {data['phone']}")
        print(f"Email: {data['email']}")
        print(f"Address: {data['address']}")
        print(f"Group: {data['group']}")


def update_contact(contacts):
    name = input("Enter name to update: ").strip()

    if name not in contacts:
        print("Contact not found!")
        return contacts

    print("Leave blank to keep old value.")

    phone = input("New phone: ")
    if phone:
        valid, phone = validate_phone(phone)
        if valid:
            contacts[name]['phone'] = phone

    email = input("New email: ")
    if email and validate_email(email):
        contacts[name]['email'] = email

    address = input("New address: ")
    if address:
        contacts[name]['address'] = address

    group = input("New group: ")
    if group:
        contacts[name]['group'] = group

    contacts[name]['updated_at'] = datetime.now().isoformat()

    save_contacts(contacts)
    print("✅ Contact updated!")
    return contacts


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name not in contacts:
        print("Contact not found!")
        return contacts

    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() == 'y':
        del contacts[name]
        save_contacts(contacts)
        print("✅ Contact deleted!")

    return contacts


def display_all(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- ALL CONTACTS ---")
    for name, data in contacts.items():
        print(f"\n{name}")
        print(f"Phone: {data['phone']}")
        print(f"Email: {data['email']}")
        print(f"Address: {data['address']}")
        print(f"Group: {data['group']}")


# ---------------- EXTRA FEATURES ---------------- #

def export_csv(contacts):
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Address", "Group"])

        for name, data in contacts.items():
            writer.writerow([
                name,
                data['phone'],
                data['email'],
                data['address'],
                data['group']
            ])

    print("✅ Exported to contacts.csv")


def show_stats(contacts):
    print("\n--- STATISTICS ---")
    print(f"Total Contacts: {len(contacts)}")

    groups = {}
    for c in contacts.values():
        g = c['group']
        groups[g] = groups.get(g, 0) + 1

    print("Contacts by group:")
    for g, count in groups.items():
        print(f"{g}: {count}")


# ---------------- MAIN MENU ---------------- #

def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Export to CSV")
        print("7. View Statistics")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            contacts = add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            contacts = update_contact(contacts)
        elif choice == '4':
            contacts = delete_contact(contacts)
        elif choice == '5':
            display_all(contacts)
        elif choice == '6':
            export_csv(contacts)
        elif choice == '7':
            show_stats(contacts)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
