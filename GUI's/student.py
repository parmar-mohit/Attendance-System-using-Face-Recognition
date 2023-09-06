import tkinter
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title("Student Details")
window.geometry('600x660')
window.configure(bg='#333333')

# Create a global variable to store the captured image
captured_image = None

def validate_roll_number_input(event):
    entered_roll_number = roll_number_entry.get()
    if len(entered_roll_number) >= 3:
        roll_number_entry.delete(3, tkinter.END)  # Delete any extra characters

def validate_gr_number_input(event):
    entered_gr_number = gr_number_entry.get()
    if len(entered_gr_number) > 9:
        gr_number_entry.delete(9, tkinter.END)  # Truncate excess characters
    elif len(entered_gr_number) < 9:
        # You can choose to handle this case differently if needed
        pass

def login():
    # Retrieve values from entry fields and the Combobox
    entered_roll_number = roll_number_entry.get()
    entered_first_name = first_name_entry.get()
    entered_last_name = last_name_entry.get()
    entered_email = email_entry.get()
    entered_gr_number = gr_number_entry.get()
    entered_division = division_combobox.get()

    if not entered_roll_number.isdigit() or len(entered_roll_number) != 3:
        messagebox.showerror(title="Error", message="Roll number must be a 3-digit integer.")
    elif not entered_first_name or not entered_last_name or not entered_email or len(entered_gr_number) != 9 or not entered_division:
        messagebox.showerror(title="Error", message="Please enter all details.")
    else:
        # Simulate storing student details in the database
        # You can add your database logic here
        # For now, just show a message
        messagebox.showinfo(title="Database Info", message="Student details stored successfully.")

        # Reset values in the GUI
        roll_number_entry.delete(0, tkinter.END)
        first_name_entry.delete(0, tkinter.END)
        last_name_entry.delete(0, tkinter.END)
        email_entry.delete(0, tkinter.END)
        gr_number_entry.delete(0, tkinter.END)
        division_combobox.set("A")  # Reset the Combobox value

def capture_image():
    pass

frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Student Details", bg='#333333', fg="#FF3399", font=("Arial", 30))
roll_number_label = tkinter.Label(
    frame, text="Roll Number", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
roll_number_entry = tkinter.Entry(frame, font=("Arial", 16))
first_name_label = tkinter.Label(
    frame, text="First Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
first_name_entry = tkinter.Entry(frame, font=("Arial", 16))
last_name_label = tkinter.Label(
    frame, text="Last Name", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
last_name_entry = tkinter.Entry(frame, font=("Arial", 16))
email_label = tkinter.Label(
    frame, text="Email", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
email_entry = tkinter.Entry(frame, font=("Arial", 16))
gr_number_label = tkinter.Label(
    frame, text="GR Number", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
gr_number_entry = tkinter.Entry(frame, font=("Arial", 16))
division_label = tkinter.Label(
    frame, text="Division", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
division_values = ["A", "B"]
division_combobox = ttk.Combobox(frame, values=division_values, font=("Arial", 16))
division_combobox.set("A")  # Set the default value
submit_button = tkinter.Button(
    frame, text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

capture_image_button = tkinter.Button(
    frame, text="Capture Image", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=capture_image)

# Bind the roll_number_entry to the validate_roll_number_input function
roll_number_entry.bind('<KeyRelease>', validate_roll_number_input)

# Bind the gr_number_entry to the validate_gr_number_input function
gr_number_entry.bind('<KeyRelease>', validate_gr_number_input)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
roll_number_label.grid(row=1, column=0)
roll_number_entry.grid(row=1, column=1, pady=20)
first_name_label.grid(row=2, column=0)
first_name_entry.grid(row=2, column=1, pady=20)
last_name_label.grid(row=3, column=0)
last_name_entry.grid(row=3, column=1, pady=20)
email_label.grid(row=4, column=0)
email_entry.grid(row=4, column=1, pady=20)
gr_number_label.grid(row=5, column=0)
gr_number_entry.grid(row=5, column=1, pady=20)
division_label.grid(row=6, column=0)
division_combobox.grid(row=6, column=1, pady=20)
capture_image_button.grid(row=7, column=0, columnspan=2, pady=10)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)
frame.pack()

window.mainloop()
