# Contact Management System

# 📌 Overview

This project provides a lightweight contact management system powered by SQLite. It enables users to manage contacts through basic operations like adding, updating, deleting, and verifying contact details directly from the command line. The system is built using Python and leverages a dictionary for internal data handling alongside SQLite for persistent storage.

# 🗄️ Database Setup

The system uses a local SQLite database file named contacts.db.
It contains a single table contacts with the following schema:

Field	Type	Description

name	TEXT	Contact's name (Primary Key)
phone_number	TEXT	Contact's phone number

# ⚙️ Features

➕ Add New Contact
->Create a new contact by providing a name and phone number. Existing entries with the same name will be overwritten.

🗑️ Remove All Contacts
->Deletes all contacts from the database.

❌ Delete Specific Contact
->Deletes a contact using their name.

🔁 Add or Modify Contact
->Inserts a new contact or updates an existing contact’s phone number.

📄 Show All Contacts
->Displays the complete list of contacts stored in the database.

🔍 Search Contact by Name
->Checks if a contact exists by name and shows their number if found.

🚪 Exit Program
->Safely closes the database connection and exits the application.

# ▶️ How to Use

Run the Script
->Execute the Python script to start the system.

Select an Option from Menu
->A menu will display various operations. Enter the number corresponding to the desired action.

Follow On-Screen Prompts
->Based on your choice, provide the necessary inputs such as name or phone number.

Exit Gracefully
->To exit the system, select the exit option (7). This ensures all connections are properly closed.
