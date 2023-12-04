import streamlit as st
import subprocess
import os
import pandas as pd

class StudentAttendanceApp:
    def __init__(self):
        self.current_process = None

    def register(self):
        if self.current_process:
            self.current_process.terminate()
        self.current_process = subprocess.Popen(['python', 'register_student.py'])

    def attendance(self):
        if self.current_process:
            self.current_process.terminate()
        self.current_process = subprocess.Popen(['python', 'attendance.py'])

    def stop(self):
        if self.current_process:
            self.current_process.terminate()

    def read_attendance_data(self):
        attendance_data_path = 'attendance.csv'
        try:
            data = pd.read_csv(attendance_data_path)
            return data.to_string(index=False)
        except FileNotFoundError:
            return 'attendance.csv not found.'
        except Exception as e:
            return f'An error occurred: {e}'

def main():
    st.title("Student Attendance System")

    app = StudentAttendanceApp()

    register_btn = st.button('Register')
    attendance_btn = st.button('Attendance')
    stop_btn = st.button('Stop')
    show_data_btn = st.button('Show Data')

    if register_btn:
        app.register()

    if attendance_btn:
        app.attendance()

    if stop_btn:
        app.stop()

    if show_data_btn:
        data = app.read_attendance_data()
        st.text_area('Attendance Data', data)

if __name__ == '__main__':
    main()
