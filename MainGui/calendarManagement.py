import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime

class AppointmentManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Appointment Scheduler")
        self.appointments = []

        # Load appointments from file if exists
        try:
            with open("appointments.pkl", "rb") as f:
                self.appointments = pickle.load(f)
        except FileNotFoundError:
            pass

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter Appointment Details:")
        self.label.grid(row=0, column=0, columnspan=2, pady=5)

        self.date_label = tk.Label(self.master, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=1, column=0, pady=5)
        self.date_entry = tk.Entry(self.master)
        self.date_entry.grid(row=1, column=1, pady=5)

        self.time_label = tk.Label(self.master, text="Time (HH:MM):")
        self.time_label.grid(row=2, column=0, pady=5)
        self.time_entry = tk.Entry(self.master)
        self.time_entry.grid(row=2, column=1, pady=5)

        self.desc_label = tk.Label(self.master, text="Description:")
        self.desc_label.grid(row=3, column=0, pady=5)
        self.desc_entry = tk.Entry(self.master)
        self.desc_entry.grid(row=3, column=1, pady=5)

        self.submit_button = tk.Button(self.master, text="Schedule Appointment", command=self.schedule_appointment)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Appointment", command=self.delete_selected_appointment)
        self.delete_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.display_appointments()

    def schedule_appointment(self):
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()
        desc = self.desc_entry.get()

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            time = datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format")
            return

        appointment = {"date": date, "time": time, "description": desc}
        self.appointments.append(appointment)
        self.save_appointments()

        messagebox.showinfo("Success", "Appointment scheduled successfully")
        self.clear_entries()
        self.display_appointments()

    def delete_selected_appointment(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.appointments[index]
            self.save_appointments()
            self.display_appointments()
        else:
            messagebox.showerror("Error", "Please select an appointment to delete")

    def display_appointments(self):
        if hasattr(self, "listbox"):
            self.listbox.destroy()

        self.listbox = tk.Listbox(self.master, width=50)
        self.listbox.grid(row=5, column=0, columnspan=2)

        for appointment in self.appointments:
            date_str = appointment["date"].strftime("%Y-%m-%d")
            time_str = appointment["time"].strftime("%H:%M")
            desc = appointment["description"]
            self.listbox.insert(tk.END, f"{date_str} {time_str} - {desc}")

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def save_appointments(self):
        with open("appointments.pkl", "wb") as f:
            pickle.dump(self.appointments, f)
