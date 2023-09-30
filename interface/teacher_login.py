import tkinter
from tkinter import messagebox
from interface.DatabaseConnection import DatabaseConnection
from interface.attendance import showAttendanceInterface

def showTeacherLoginInterface():
    window = tkinter.Tk()
    window.title("Teacher Login")
    window.geometry('600x360')
    window.configure(bg='#333333')

    def login():
        username = username_entry.get()
        password = password_entry.get()
        
        db = DatabaseConnection()
        if db.validateUser(username, password):
            window.destroy()
            showAttendanceInterface(username)
        else:
            messagebox.showerror(title="Authentication Failed",message="Invalid username or password")

    frame = tkinter.Frame(bg='#333333')

    # Creating widgets
    login_label = tkinter.Label(
        frame, text="Teacher Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
    username_label = tkinter.Label(
        frame, text="Username:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    password_label = tkinter.Label(
        frame, text="Password:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

    username_entry = tkinter.Entry(frame, font=("Arial", 16))
    password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))

    login_button = tkinter.Button(
        frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

    # Placing widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
    username_label.grid(row=1, column=0)
    password_label.grid(row=2, column=0)
    username_entry.grid(row=1, column=1, pady=10)
    password_entry.grid(row=2, column=1, pady=10)
    login_button.grid(row=3, column=0, columnspan=2, pady=20)
    window_width = 400
    frame.pack()

    window.mainloop()
