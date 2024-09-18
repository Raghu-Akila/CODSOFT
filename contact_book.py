import tkinter as tk
from tkinter import messagebox
import json
import os

# contacts.json
# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from JSON file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save contacts to JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts = load_contacts()
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact {name} added successfully!")
        clear_entries()
        refresh_contacts_list()
    else:
        messagebox.showerror("Error", "Name and phone are required!")

# View all contacts
def refresh_contacts_list():
    listbox_contacts.delete(0, tk.END)
    contacts = load_contacts()
    if contacts:
        for contact in contacts:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    else:
        listbox_contacts.insert(tk.END, "No contacts found.")

# Search for a contact
def search_contact():
    query = entry_search.get().lower()
    contacts = load_contacts()
    listbox_contacts.delete(0, tk.END)
    found = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]

    if found:
        for contact in found:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")
    else:
        listbox_contacts.insert(tk.END, "No contact found.")

# Clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Delete a contact
def delete_contact():
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contacts = load_contacts()
        contact_name = contacts[index]['name']
        del contacts[index]
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact {contact_name} deleted successfully!")
        refresh_contacts_list()
    else:
        messagebox.showerror("Error", "No contact selected!")

# Update selected contact
def update_contact():
    selected = listbox_contacts.curselection()
    if selected:
        index = selected[0]
        contacts = load_contacts()
        contact = contacts[index]
        contact['name'] = entry_name.get() or contact['name']
        contact['phone'] = entry_phone.get() or contact['phone']
        contact['email'] = entry_email.get() or contact['email']
        contact['address'] = entry_address.get() or contact['address']
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact {contact['name']} updated successfully!")
        refresh_contacts_list()
    else:
        messagebox.showerror("Error", "No contact selected!")

# Create main window
window = tk.Tk()
window.title("Contact Book")

# Labels and entry fields
label_name = tk.Label(window, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_phone = tk.Label(window, text="Phone:")
label_phone.grid(row=1, column=0, padx=10, pady=5)
entry_phone = tk.Entry(window)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(window, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(window)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_address = tk.Label(window, text="Address:")
label_address.grid(row=3, column=0, padx=10, pady=5)
entry_address = tk.Entry(window)
entry_address.grid(row=3, column=1, padx=10, pady=5)

# Buttons
btn_add = tk.Button(window, text="Add Contact", command=add_contact)
btn_add.grid(row=4, column=0, padx=10, pady=10)

btn_update = tk.Button(window, text="Update Contact", command=update_contact)
btn_update.grid(row=4, column=1, padx=10, pady=10)

btn_delete = tk.Button(window, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=4, column=2, padx=10, pady=10)

# Contact listbox
listbox_contacts = tk.Listbox(window, height=10, width=40)
listbox_contacts.grid(row=5, column=0, columnspan=3, padx=10, pady=5)
refresh_contacts_list()

# Search field and button
label_search = tk.Label(window, text="Search by Name/Phone:")
label_search.grid(row=6, column=0, padx=10, pady=5)
entry_search = tk.Entry(window)
entry_search.grid(row=6, column=1, padx=10, pady=5)

btn_search = tk.Button(window, text="Search", command=search_contact)
btn_search.grid(row=6, column=2, padx=10, pady=5)

# Main loop
window.mainloop()
