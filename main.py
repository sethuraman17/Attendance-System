import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
import os
import subprocess

class StudentAttendanceApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Global variable to store the subprocess object
        self.current_process = None

        self.register_btn = ttk.Button(window, text='Register', command=self.register)
        self.attendance_btn = ttk.Button(window, text='Attendance', command=self.attendance)
        self.show_data_btn = ttk.Button(window, text='Show Data', command=self.show_data)
        self.stop_btn = ttk.Button(window, text='Stop', command=self.stop)

        self.register_btn.pack(padx=10, pady=5)
        self.attendance_btn.pack(padx=10, pady=5)
        self.show_data_btn.pack(padx=10, pady=5)
        self.stop_btn.pack(padx=10, pady=5)

    def register(self):
        # Terminate the current subprocess if any
        if self.current_process:
            self.current_process.terminate()
        self.current_process = subprocess.Popen(['python', 'register_student.py'])

    def attendance(self):
        # Terminate the current subprocess if any
        if self.current_process:
            self.current_process.terminate()
        self.current_process = subprocess.Popen(['python', 'attendance.py'])

    def stop(self):
        # Terminate the current subprocess if any
        if self.current_process:
            self.current_process.terminate()

    def show_data(self):
        data = self.read_attendance_data()
        self.display_data(data, 'Attendance Data')

    def read_attendance_data(self):
        attendance_data_path = 'attendance.csv'
        data = ''
        try:
            with open(attendance_data_path, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            messagebox.showinfo('File Not Found', 'attendance.csv not found.')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')
        return data

    def display_data(self, data, title):
        data_window = tk.Toplevel(self.window)
        data_window.title(title)

        text_widget = tk.Text(data_window, wrap='word', width=40, height=20)
        text_widget.pack(padx=10, pady=10)

        text_widget.insert(tk.END, data)

if __name__ == '__main__':
    root = tk.Tk()
    app = StudentAttendanceApp(root, 'Student Attendance System')
    root.mainloop()
