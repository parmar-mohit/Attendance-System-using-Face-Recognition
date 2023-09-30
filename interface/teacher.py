import tkinter
from tkinter import messagebox
from interface.DatabaseConnection import DatabaseConnection

def showTeacherDetailsInterface():
    window = tkinter.Tk()
    window.title("Teacher Details")
    window.geometry('600x560')  # Adjusted the window height to fit the removed section
    window.configure(bg='#333333')

    def save_details_button_on_click():
        username = username_entry.get()
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        password = password_entry.get()
            
        if username == "" or firstname == "" or lastname == "" or password == "":
            messagebox.showerror(title="Enter Details",message="Please Enter all detail before saving")
        else:
            db = DatabaseConnection()
            db.insertTeacherDetails(username,firstname,lastname,password)
            messagebox.showinfo(title="Success", message="Details Stored Successfully")

            # Reset values in the GUI
            username_entry.delete(0, tkinter.END)
            first_name_entry.delete(0, tkinter.END)
            last_name_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

    frame = tkinter.Frame(bg='#333333')

    # Creating widgets
    login_label = tkinter.Label(
        frame, text="Teacher Details", bg='#333333', fg="#FF3399", font=("Arial", 30))
    first_name_label = tkinter.Label(
        frame, text="First Name:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    last_name_label = tkinter.Label(
        frame, text="Last Name:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    username_label = tkinter.Label(
        frame, text="Username:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    password_label = tkinter.Label(
        frame, text="Password:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

    first_name_entry = tkinter.Entry(frame, font=("Arial", 16))
    last_name_entry = tkinter.Entry(frame, font=("Arial", 16))
    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))

    save_details = tkinter.Button(
        frame, text="Save Details", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=save_details_button_on_click)

    # Placing widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    first_name_label.grid(row=1, column=0)
    last_name_label.grid(row=2, column=0)
    username_label.grid(row=3, column=0)
    password_label.grid(row=4, column=0)

    first_name_entry.grid(row=1, column=1, pady=20)
    last_name_entry.grid(row=2, column=1, pady=20)
    username_entry.grid(row=3, column=1, pady=20)
    password_entry.grid(row=4, column=1, pady=20)

    save_details.grid(row=5, column=0, columnspan=2, pady=30)
    window_width = 600
    frame.pack()

    window.mainloop()