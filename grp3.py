import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class PatientRecord:
    def __init__(self, name, appointment_date, age, condition, gender, dob):
        self.name = name
        self.appointment_date = appointment_date
        self.age = age
        self.condition = condition
        self.gender = gender
        self.dob = dob

    def __str__(self):
        return f"Name: {self.name}, Appointment Date: {self.appointment_date}, Age: {self.age}, " \
               f"Condition: {self.condition}, Gender: {self.gender}, Date of Birth: {self.dob}"


# Sorting functions
def bubble_sort_by_name(records):
    n = len(records)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if records[j].name > records[j + 1].name:
                records[j], records[j + 1] = records[j + 1], records[j]


def selection_sort_by_dob(records):
    n = len(records)
    for i in range(n):
        max_index = i  # Change from min_index to max_index
        for j in range(i + 1, n):
            if records[j].dob > records[max_index].dob:  # Sort in descending order (most recent first)
                max_index = j
        records[i], records[max_index] = records[max_index], records[i]


def insertion_sort_by_appointment_date(records):
    for i in range(1, len(records)):
        key = records[i]
        j = i - 1
        # Compare and place the key record in descending order of appointment date
        while j >= 0 and records[j].appointment_date < key.appointment_date:  # Changed the '<' to '>'
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key


# Main Application
class PatientRecordsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Records Management System")

        # Set the size and background color of the window
        self.root.geometry("800x600")
        self.root.config(bg="#F4F6F7")  # Light gray background for the main window

        # List to hold patient records
        self.records = []

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Title label with a color
        self.title_label = tk.Label(self.root, text="Patient Records Management", font=("Arial", 20, "bold"),
                                    fg="#333333", bg="#F4F6F7")
        self.title_label.pack(pady=20)

        # Add Patient Record button with colors
        self.btn_add_record = tk.Button(self.root, text="Add Patient Record", width=25, height=3, font=("Arial", 14),
                                        command=self.add_patient_record, bg="#4CAF50", fg="white",
                                        activebackground="#388E3C")
        self.btn_add_record.pack(pady=15)

        # View Records button with colors
        self.btn_view_records = tk.Button(self.root, text="View Records", width=25, height=3, font=("Arial", 14),
                                          command=self.view_records, bg="#2196F3", fg="white",
                                          activebackground="#1976D2")
        self.btn_view_records.pack(pady=15)

        # Search by Name button with colors
        self.btn_search_name = tk.Button(self.root, text="Search by Name", width=25, height=3, font=("Arial", 14),
                                         command=self.search_by_name, bg="#FF9800", fg="white",
                                         activebackground="#F57C00")
        self.btn_search_name.pack(pady=15)

        # Search by Appointment Date button with colors
        self.btn_search_appointment = tk.Button(self.root, text="Search by Appointment Date", width=25, height=3,
                                                font=("Arial", 14),
                                                command=self.search_by_appointment_date, bg="#8BC34A", fg="white",
                                                activebackground="#7CB342")
        self.btn_search_appointment.pack(pady=15)

        # Exit button with colors
        self.btn_exit = tk.Button(self.root, text="Exit", width=25, height=3, font=("Arial", 14),
                                  command=self.exit_program,
                                  bg="#F44336", fg="white", activebackground="#D32F2F")
        self.btn_exit.pack(pady=15)

    def add_patient_record(self):
        name = simpledialog.askstring("Input", "Enter Name (Surname, Firstname MI):", parent=self.root)
        if not name:
            return

        appointment_date = simpledialog.askstring("Input", "Enter Appointment Date (MM-DD-YY):", parent=self.root)
        age = simpledialog.askinteger("Input", "Enter Age:", parent=self.root)
        condition = simpledialog.askstring("Input", "Enter Condition/Diagnosis:", parent=self.root)
        gender = simpledialog.askstring("Input", "Enter Gender (F/M):", parent=self.root)
        dob = simpledialog.askstring("Input", "Enter Date of Birth (MM-DD-YY):", parent=self.root)

        # Add the record to the list
        self.records.append(PatientRecord(name, appointment_date, age, condition, gender, dob))
        messagebox.showinfo("Success", "Patient record added.", parent=self.root)

    def view_records(self):
        if not self.records:
            messagebox.showinfo("No Records", "No records available.", parent=self.root)
            return

        # Ask user for sorting option
        sort_choice = simpledialog.askinteger("Sort Options",
                                              "Choose sorting option:\n1. Sort by Name (A-Z)\n2. Sort by Date of Birth\n3. Sort by Appointment Date\nEnter 1, 2, or 3:",
                                              parent=self.root)

        if sort_choice == 1:
            bubble_sort_by_name(self.records)
            messagebox.showinfo("Sorted", "Sorted by Name (A-Z).", parent=self.root)
        elif sort_choice == 2:
            selection_sort_by_dob(self.records)
            messagebox.showinfo("Sorted", "Sorted by Date of Birth (Most Recent First).", parent=self.root)
        elif sort_choice == 3:
            insertion_sort_by_appointment_date(self.records)
            messagebox.showinfo("Sorted", "Sorted by Appointment Date (Most Recent First).", parent=self.root)
        else:
            messagebox.showwarning("Invalid Choice", "Invalid choice. Returning to main menu.", parent=self.root)
            return

        # Display sorted records in a message box
        records_str = "\n\n".join(str(record) for record in self.records)
        messagebox.showinfo("Patient Records", records_str, parent=self.root)

    def search_by_name(self):
        name = simpledialog.askstring("Search by Name", "Enter the patient's name to search:", parent=self.root)
        if not name:
            return

        found_records = [record for record in self.records if name.lower() in record.name.lower()]

        if found_records:
            records_str = "\n\n".join(str(record) for record in found_records)
            messagebox.showinfo("Search Results", f"Records found:\n\n{records_str}", parent=self.root)
        else:
            messagebox.showinfo("No Results", "No records found for this name.", parent=self.root)

    def search_by_appointment_date(self):
        appointment_date = simpledialog.askstring("Search by Appointment Date",
                                                  "Enter the appointment date to search (MM-DD-YY):", parent=self.root)
        if not appointment_date:
            return

        found_records = [record for record in self.records if record.appointment_date == appointment_date]

        if found_records:
            records_str = "\n\n".join(str(record) for record in found_records)
            messagebox.showinfo("Search Results", f"Records found:\n\n{records_str}", parent=self.root)
        else:
            messagebox.showinfo("No Results", "No records found for this appointment date.", parent=self.root)

    def exit_program(self):
        result = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.root)
        if result:
            self.root.quit()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PatientRecordsApp(root)
    root.mainloop()


