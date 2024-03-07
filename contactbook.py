import tkinter as tk
from tkinter import messagebox

class Contact:
    def _init_(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Contact Manager")

        self.contacts = []

        # Labels and Entry widgets for contact details
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for actions
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        search_term = self.name_entry.get().lower()

        if not search_term:
            messagebox.showwarning("Warning", "Enter a name or phone number to search.")
            return

        found_contacts = [contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone]
        if not found_contacts:
            messagebox.showinfo("Info", f"No contacts found for '{search_term}'.")
        else:
            contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in found_contacts])
            messagebox.showinfo("Search Results", contact_list)

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if not name or not phone:
            messagebox.showwarning("Warning", "Enter a name and phone number to update.")
            return

        for contact in self.contacts:
            if contact.name == name and contact.phone == phone:
                contact.email = self.email_entry.get()
                contact.address = self.address_entry.get()
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_entries()
                return

        messagebox.showinfo("Info", f"No contact found for {name} with phone number {phone}.")

    def delete_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if not name or not phone:
            messagebox.showwarning("Warning", "Enter a name and phone number to delete.")
            return

        for contact in self.contacts:
            if contact.name == name and contact.phone == phone:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.clear_entries()
                return

        messagebox.showinfo("Info", f"No contact found for {name} with phone number {phone}.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if _name_ == "_main_":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()