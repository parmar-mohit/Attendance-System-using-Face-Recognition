import tkinter as tk
from interface.admin_login import showAdminLoginWindow
from interface.teacher_login import showTeacherLoginInterface

# Create the main window
root = tk.Tk()
root.title("Login Interface")

# Set the background color of the main window
root.configure(bg="#333333")
root.geometry('450x200')

def adminLoginButtonOnClick():
    root.destroy()
    showAdminLoginWindow()

def teacherLoginButtonOnClick():
    root.destroy()
    showTeacherLoginInterface()

# Create a custom font
custom_font = ("Arial", 16)

# Create a frame with the specified background color
frame = tk.Frame(root, bg="#333333")
frame.pack(padx=20, pady=20)

# Create the "Admin Login" button with the specified text and text color
admin_button = tk.Button(frame, text="Admin Login", font=custom_font,bg="#FF3399", fg="#FFFFFF",command = adminLoginButtonOnClick)
admin_button.pack(pady=10)

# Create the "Teacher Login" button with the specified text and text color
teacher_button = tk.Button(frame, text="Teacher Login", font=custom_font,bg="#FF3399", fg="#FFFFFF",command=teacherLoginButtonOnClick)
teacher_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()