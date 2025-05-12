import sqlite3

# Database setup
conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS contacts (name TEXT PRIMARY KEY, phone_number TEXT)''')
conn.commit()

# Functional modules
def insert_contact(name, phone_number):
    c.execute("INSERT OR REPLACE INTO contacts (name, phone_number) VALUES (?, ?)", (name, phone_number))
    conn.commit()
    print("\n✅ Contact added or updated successfully.")

def clear_contacts():
    c.execute("DELETE FROM contacts")
    conn.commit()
    print("\n🗑️ All contacts cleared.")

def delete_contact(name):
    c.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()
    print("\n❌ Contact deleted successfully.")

def display_contacts():
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    print("\n📋 Contacts:")
    if contacts:
        for contact in contacts:
            print(f"➡️ {contact[0]} : {contact[1]}")
    else:
        print("No contacts found.")

def check_contact(name):
    c.execute("SELECT phone_number FROM contacts WHERE name=?", (name,))
    result = c.fetchone()
    if result:
        print(f"\n📞 Found: {name} : {result[0]}")
    else:
        print(f"\n⚠️ No contact found for {name}.")

def show_menu():
    print("\n========= Contact Manager =========")
    print("1. Insert contact")
    print("2. Clear all contacts")
    print("3. Delete a contact")
    print("4. Add or update contact details")
    print("5. Display all contacts")
    print("6. Check contact by name")
    print("7. Exit")
    print("====================================")

# Main loop with error handling
def main():
    try:
        while True:
            show_menu()
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                name = input("Enter name: ").strip()
                phone_number = input("Enter phone number: ").strip()
                insert_contact(name, phone_number)
            elif choice == '2':
                clear_contacts()
            elif choice == '3':
                name = input("Enter name to delete: ").strip()
                delete_contact(name)
            elif choice == '4':
                name = input("Enter name: ").strip()
                phone_number = input("Enter phone number: ").strip()
                insert_contact(name, phone_number)
            elif choice == '5':
                display_contacts()
            elif choice == '6':
                name = input("Enter name to check: ").strip()
                check_contact(name)
            elif choice == '7':
                print("\n👋 Exiting program...")
                break
            else:
                print("\n❗ Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\n\n🚨 Program interrupted by user. Exiting gracefully...")
    finally:
        conn.close()

# Run the app
if __name__ == "__main__":
    main()
