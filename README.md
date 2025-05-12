# Contact Management System Documentation

# Overview
This project implements a basic contact management system using SQLite as the backend database. It allows users to perform various operations such as adding, deleting, and updating contacts, as well as checking if a contact exists by name. All actions are performed using a Python dictionary. The system is designed for simplicity and utilizes the command line as the user interface.

# Database Setup
The project uses an SQLite database named contacts.db to store contact information. The database contains a single table called contacts, with the following schema:

name: The contact's name (Primary Key)

phone_number: The contact's phone number

# Features
The following operations are available for managing contacts:

Insert Contact: Adds a new contact with a specified name and phone number. If a contact with the same name already exists, it replaces the old phone number with the new one.

Clear All Contacts: Deletes all contacts from the database.

Delete a Contact: Removes a contact by name.

Add or Update Contact: Adds a new contact or updates the phone number of an existing one.

Display All Contacts: Displays a list of all contacts in the database.

Check Contact by Name: Checks if a contact with the given name exists, and if found, displays the phone number.

Exit: Closes the database connection and exits the program.

# How to Use

Run the Script: Execute the Python script to start the contact management system.

Select an Option: A menu will appear with different operations. Enter the number corresponding to the desired action.

Perform the Operation: Depending on the selected option, follow the prompts to enter information or confirm the action.

Exit: To exit the program, select option 7. This will safely close the database connection.
