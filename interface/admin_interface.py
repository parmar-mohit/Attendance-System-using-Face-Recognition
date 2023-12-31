import tkinter
from tkinter import messagebox
from interface.student import showStudentDetailsInterface
from interface.teacher import showTeacherDetailsInterface
from interface.course import showCourseDetailsInterface

def showAdminInterface():
    # Function to handle button clicks
    def show_details(category):
        if category == "Students":
            window.destroy()
            showStudentDetailsInterface()
            showAdminInterface()
        elif category == "Teachers":
            window.destroy()
            showTeacherDetailsInterface()
            showAdminInterface()
        elif category == "Courses":
            window.destroy()
            showCourseDetailsInterface()
            showAdminInterface()

    # Create the main window
    window = tkinter.Tk()
    window.title("Details Panel")
    window.geometry('600x550')
    window.configure(bg='#333333')

    # Create a frame
    frame = tkinter.Frame(bg='#333333')

    # Create widgets
    title_label = tkinter.Label(frame, text="Details Panel", bg='#333333', fg="#FF3399", font=("Arial", 30))
    students_button = tkinter.Button(frame, text="Students Details", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=lambda: show_details("Students"))
    teachers_button = tkinter.Button(frame, text="Teachers Details", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=lambda: show_details("Teachers"))
    courses_button = tkinter.Button(frame, text="Course Details", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=lambda: show_details("Courses"))

    # Place widgets on the screen
    title_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    students_button.grid(row=1, column=0, pady=20)
    teachers_button.grid(row=2, column=0, pady=20)
    courses_button.grid(row=3, column=0, pady=20)

    frame.pack()
    window.mainloop()