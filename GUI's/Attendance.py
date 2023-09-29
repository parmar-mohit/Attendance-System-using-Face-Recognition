# course id, date, capture attendance, generate report
import tkinter
from tkinter import ttk, messagebox
from tkcalendar import Calendar

window = tkinter.Tk()
window.title("Attendance Details")
window.geometry('600x660')
window.configure(bg='#333333')

def validate_course_id_input(event):
    entered_course_id = course_id_entry.get()
    # You can add validation logic here if needed

def capture_attendance():
    selected_date = cal.get_date()
    course_id = course_id_entry.get()
    # Add your logic to capture attendance for the selected date and course ID
    messagebox.showinfo("Attendance Captured", f"Attendance for Course ID {course_id} on {selected_date} captured successfully!")

def generate_report():
    # Add your logic to generate a report
    # For now, just show a message
    messagebox.showinfo("Generate Report", "Generating report...")

frame = tkinter.Frame(bg='#333333')

# Creating widgets
attendance_label = tkinter.Label(
    frame, text="Attendance Details", bg='#333333', fg="#FF3399", font=("Arial", 30))
course_id_label = tkinter.Label(
    frame, text="Course ID:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
course_id_entry = tkinter.Entry(frame, font=("Arial", 16))

date_label = tkinter.Label(
    frame, text="Date:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
cal = Calendar(frame, selectmode="day", date_pattern="dd/MM/yyyy", font=("Arial", 16))

capture_button = tkinter.Button(
    frame, text="Capture Attendance", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=capture_attendance)

generate_button = tkinter.Button(
    frame, text="Generate Report", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=generate_report)

# Bind the course_id_entry to the validate_course_id_input function
course_id_entry.bind('<KeyRelease>', validate_course_id_input)

# Placing widgets on the screen
attendance_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
course_id_label.grid(row=1, column=0)
course_id_entry.grid(row=1, column=1, pady=20)
date_label.grid(row=2, column=0)
cal.grid(row=2, column=1, pady=20)
capture_button.grid(row=3, column=0, columnspan=2, pady=10)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)
frame.pack()

window.mainloop()


