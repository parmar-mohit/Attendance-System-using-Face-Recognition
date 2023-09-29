# course id, name, div, year, teacher id,
# should open after clicking course details
import tkinter
from tkinter import ttk, messagebox

window = tkinter.Tk()
window.title("Course Details")
window.geometry('600x660')
window.configure(bg='#333333')

def validate_course_id_input(event):
    entered_course_id = course_id_entry.get()
    # You can add validation logic here if needed

def validate_year_input(event):
    entered_year = year_combobox.get()
    if entered_year not in year_values:
        year_combobox.set(year_values[0])
        
def login():
    entered_course_id = course_id_entry.get()
    entered_name = name_entry.get()
    entered_division = division_combobox.get()
    entered_year = year_combobox.get()
    entered_teacher_id = teacher_id_entry.get()

    if not entered_course_id or not entered_name or not entered_division or not entered_year or not entered_teacher_id:
        messagebox.showerror(title="Error", message="Please enter all details.")
    else:
        # Simulate storing student details in the database
        # You can add your database logic here
        # For now, just show a message
        messagebox.showinfo(title="Database Info", message="Student details stored successfully.")

        # Reset values in the GUI
        course_id_entry.delete(0, tkinter.END)
        name_entry.delete(0, tkinter.END)
        division_combobox.set("")  # Reset the Combobox value
        year_combobox.set(year_values[0])  # Reset to the default value
        teacher_id_entry.delete(0, tkinter.END)

frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Course Details:", bg='#333333', fg="#FF3399", font=("Arial", 30))
course_id_label = tkinter.Label(
    frame, text="Course ID:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
course_id_entry = tkinter.Entry(frame, font=("Arial", 16))
name_label = tkinter.Label(
    frame, text="Name:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
name_entry = tkinter.Entry(frame, font=("Arial", 16))
division_label = tkinter.Label(
    frame, text="Division:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
division_values = ["A", "B"]
division_combobox = ttk.Combobox(frame, values=division_values, font=("Arial", 16))
division_combobox.set("")  # Set the default value
year_label = tkinter.Label(
    frame, text="Year:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
year_values = ["FE", "SE", "TE", "BE"]
year_combobox = ttk.Combobox(frame, values=year_values, font=("Arial", 16))
year_combobox.set(year_values[0])  # Set the default value
teacher_id_label = tkinter.Label(
    frame, text="Teacher ID:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
teacher_id_entry = tkinter.Entry(frame, font=("Arial", 16))
submit_button = tkinter.Button(
    frame, text="Submit:", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Bind the course_id_entry to the validate_course_id_input function
course_id_entry.bind('<KeyRelease>', validate_course_id_input)

# Bind the year_combobox to the validate_year_input function
year_combobox.bind('<<ComboboxSelected>>', validate_year_input)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
course_id_label.grid(row=1, column=0)
course_id_entry.grid(row=1, column=1, pady=20)
name_label.grid(row=2, column=0)
name_entry.grid(row=2, column=1, pady=20)
division_label.grid(row=3, column=0)
division_combobox.grid(row=3, column=1, pady=20)
year_label.grid(row=4, column=0)
year_combobox.grid(row=4, column=1, pady=20)
teacher_id_label.grid(row=5, column=0)
teacher_id_entry.grid(row=5, column=1, pady=20)
submit_button.grid(row=6, column=0, columnspan=2, pady=30)
frame.pack()

window.mainloop()




