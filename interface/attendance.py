# course id, date, capture attendance, generate report
import tkinter
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from interface.DatabaseConnection import DatabaseConnection
from interface.video_frames import captureFrames,get_faces,getStudents
from interface.generate_pdf import generate_report

def showAttendanceInterface(teacher_username):
    window = tkinter.Tk()
    window.title("Attendance Details")
    window.geometry('600x660')
    window.configure(bg='#333333')

    def capture_attendance():
        selected_date = cal.get_date()
        course_id = course_combobox.get()

        if not selected_date or not course_id:
            messagebox.showerror(title="Enter Details",message="Please enter all details")
        else:
            frames = captureFrames()
            faces = get_faces(frames)
            student = getStudents(faces)
            db = DatabaseConnection()
            db.addAttendance(student,course_id,selected_date)
            messagebox.showinfo("Attendance Captured", f"Attendance for Course ID {course_id} on {selected_date} captured successfully!")
            course_combobox.set(courseList[0])

    def generate_report_button_on_click():
        generate_report(teacher_username)
        messagebox.showinfo("Report Generated", "Report had been generated successfully")

    frame = tkinter.Frame(bg='#333333')

    # Creating widgets
    attendance_label = tkinter.Label(
        frame, text="Attendance Details", bg='#333333', fg="#FF3399", font=("Arial", 30))
    course_id_label = tkinter.Label(
        frame, text="Course ID:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    db = DatabaseConnection()
    courseList = db.getCourseList(teacher_username)
    course_combobox = ttk.Combobox(frame,values=courseList,font=("Arial",16))

    date_label = tkinter.Label(
        frame, text="Date:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    cal = Calendar(frame, selectmode="day", date_pattern="dd/MM/yyyy", font=("Arial", 16))

    capture_button = tkinter.Button(
        frame, text="Capture Attendance", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=capture_attendance)

    generate_button = tkinter.Button(
        frame, text="Generate Report", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=generate_report_button_on_click)

    # Placing widgets on the screen
    attendance_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    course_id_label.grid(row=1, column=0)
    course_combobox.grid(row=1, column=1, pady=20)
    date_label.grid(row=2, column=0)
    cal.grid(row=2, column=1, pady=20)
    capture_button.grid(row=3, column=0, columnspan=2, pady=10)
    generate_button.grid(row=4, column=0, columnspan=2, pady=10)
    frame.pack()

    window.mainloop()