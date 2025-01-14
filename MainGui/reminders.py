import time
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import threading

class ReminderManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Reminder Manager")

        self.reminders = []

        self.create_widgets()

        # Start a background thread to check for reminders
        self.background_thread = threading.Thread(target=self.check_reminders)
        self.background_thread.daemon = True  # Daemonize the thread so it stops when the main program exits
        self.background_thread.start()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Set Reminder:")
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

        self.submit_button = tk.Button(self.master, text="Set Reminder", command=self.set_reminder)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.reminder_listbox = tk.Listbox(self.master, width=50, height=10)
        self.reminder_listbox.grid(row=5, column=0, columnspan=2, pady=5)

    def set_reminder(self):
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()
        desc = self.desc_entry.get()

        try:
            reminder_time = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")
            now = datetime.now()
            if reminder_time < now:
                messagebox.showerror("Error", "Please enter a future date and time")
                return

            self.reminders.append((reminder_time, desc, False))
            self.update_reminder_list()
            messagebox.showinfo("Success", "Reminder set successfully")
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format")

    def check_reminders(self):
        while True:
            now = datetime.now()
            for i, (reminder_time, desc, completed) in enumerate(self.reminders):
                if not completed and now > reminder_time:
                    self.reminders[i] = (reminder_time, desc, True)
                    messagebox.showinfo("Reminder", f"Reminder: {desc}")
                    self.update_reminder_list()

            # Sleep for 1 second before checking again
            time.sleep(1)

    def update_reminder_list(self):
        self.reminder_listbox.delete(0, tk.END)
        for reminder_time, desc, completed in self.reminders:
            status = "Done" if completed else "Pending"
            self.reminder_listbox.insert(tk.END, f"{reminder_time.strftime('%Y-%m-%d %H:%M')} - {desc} ({status})")

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)


