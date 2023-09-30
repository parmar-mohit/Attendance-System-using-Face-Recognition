# should open after clicking student details
import tkinter
from tkinter import ttk, messagebox
import cv2 as cv
import os
from interface.DatabaseConnection import DatabaseConnection

def showStudentDetailsInterface():
    window = tkinter.Tk()
    window.title("Student Details")
    window.geometry('620x730')
    window.configure(bg='#333333')

    # Create a global variable to store the captured image
    captured_image = []

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

    def validate_year_input(event):
        entered_year = year_combobox.get()
        if entered_year not in year_values:
            year_combobox.set(year_values[0])  # Reset to the default value

    def submitButtonOnClick():
        # Retrieve values from entry fields and the Combobox
        entered_roll_number = roll_number_entry.get()
        entered_first_name = first_name_entry.get()
        entered_last_name = last_name_entry.get()
        entered_email = email_entry.get()
        entered_gr_number = gr_number_entry.get()
        entered_year = year_combobox.get()
        entered_division = division_combobox.get()

        if not entered_roll_number.isdigit() or len(entered_roll_number) != 3:
            messagebox.showerror(title="Error", message="Roll number must be a 3-digit integer.")
        elif not entered_first_name or not entered_last_name or not entered_email or len(entered_gr_number) != 9 or not entered_year or not entered_division:
            messagebox.showerror(title="Error", message="Please enter all details.")
        elif len(captured_image) == 0:
            messagebox.showerror(title="Error", message="Please Capture Images")
        else:
            db = DatabaseConnection()
            db.insertStudentDetails(entered_roll_number,entered_first_name,entered_last_name,entered_email,entered_gr_number,entered_year,entered_division)
            
            # Storing Images
            path = "./Dataset/"+entered_gr_number+"/"

            # Checking if directory exist and creating new if it doesn't exit
            if not os.path.isdir(path[:-1]):
                os.makedirs(path[:-1])
            else:
                # Delelting files if directory already exist
                try:
                    files = os.listdir(path[:-1])
                    for file in files:
                        file_path = os.path.join(path, file)
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                except OSError:
                    pass
                
            for i in range(len(captured_image)):
                cv.imwrite(path+"Image_"+str(i)+".jpg",captured_image[i])


            messagebox.showinfo(title="Database Info", message="Student details stored successfully.")

            # Reset values in the GUI
            roll_number_entry.delete(0, tkinter.END)
            first_name_entry.delete(0, tkinter.END)
            last_name_entry.delete(0, tkinter.END)
            email_entry.delete(0, tkinter.END)
            gr_number_entry.delete(0, tkinter.END)
            year_combobox.set(year_values[0])  # Reset the Year Combobox
            division_combobox.set("A")  # Reset the Division Combobox

    def capture_image():
        def faceBox(image,profile,frameNumber,x,y,width,height):
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv.putText(image, 'Profile : {}, Frame : {}'.format(profile,frameNumber), (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            return image
        
        def scaleFrame(imageFrame,scale):
            width = int(imageFrame.shape[1] * scale)
            height = int(imageFrame.shape[0] * scale)
            dimensions =  (width,height)
            return cv.resize(imageFrame,dimensions,interpolation = cv.INTER_CUBIC)
        
        def setImageDimension(imageFrame):
            dimensions =  (150,150)
            return cv.resize(imageFrame,dimensions,interpolation = cv.INTER_CUBIC)

        videoStream = cv.VideoCapture(0)
        frontalFrameNumber = 1
        leftFrameNumber = 1
        rightFrameNumber = 1

        # Getting Frontal Frame
        while True:
            # Getting frames from camera
            isRet, imageFrame = videoStream.read()

            # Converting frames to gray scale
            gray_frame = cv.cvtColor(imageFrame,cv.COLOR_BGR2GRAY)

            # Loading face detector from opencv library
            face_detector_frontal = cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_frontalface_default.xml")

            # Detecting Faces
            face_frontal = face_detector_frontal.detectMultiScale(gray_frame,minNeighbors=10,minSize=(30,30))

            # Getting height and width of frame
            height,width = imageFrame.shape[:2]

            # Creating Box Around Face and Saving Image
            if len(face_frontal) == 1:
                for (x, y, w, h) in face_frontal:
                    face = gray_frame[y:y+h, x:x+w]
                    face = setImageDimension(face)
                    if frontalFrameNumber <= 50:
                        captured_image.append(face)
                        frontalFrameNumber += 1
                    imageFrame = faceBox(imageFrame,"Front",frontalFrameNumber,x,y,w,h)

            # Writing Text
            message = 'Please Look Straight'
            textSize = cv.getTextSize(message,cv.FONT_HERSHEY_SIMPLEX, 1.2,2)[0]
            imageFrame = cv.putText(imageFrame, message, ((width//2) - (textSize[0] // 2), height-textSize[1]), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
                    
            # Displaying Image
            imageFrame = scaleFrame(imageFrame,1.35)
            cv.imshow("Saving Images",imageFrame)

            # Checking for keyboard input to 
            if cv.waitKey(10) & 0xFF == ord('q'):
                break
            if frontalFrameNumber > 50:
                break

        # Getting Left Profile Frame
        while True:
            # Getting frames from camera
            isRet, imageFrame = videoStream.read()

            # Converting frames to gray scale
            gray_frame = cv.cvtColor(imageFrame,cv.COLOR_BGR2GRAY)

            # Loading face detector from opencv library
            face_detector_profile = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_profileface.xml")

            # Detecting Faces
            face_profile = face_detector_profile.detectMultiScale(gray_frame, minNeighbors=10, minSize=(30,30))

            # Getting height and width of frame
            height,width = imageFrame.shape[:2]

            # Creating Box Around Face and Saving Image
            if len(face_profile) == 1:
                for (x, y, w, h) in face_profile:
                    face = gray_frame[y:y+h, x:x+w]
                    face = setImageDimension(face)
                    if leftFrameNumber <= 50:
                        captured_image.append(face)
                        leftFrameNumber += 1
                    imageFrame = faceBox(imageFrame,"Left",leftFrameNumber,x,y,w,h)

            # Writing Text
            message = 'Please Look Right'
            textSize = cv.getTextSize(message,cv.FONT_HERSHEY_SIMPLEX, 1.2,2)[0]
            imageFrame = cv.putText(imageFrame, message, ((width//2) - (textSize[0] // 2), height-textSize[1]), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
                    
            # Displaying Image
            imageFrame = scaleFrame(imageFrame,1.35)
            cv.imshow("Saving Images",imageFrame)

            # Checking for keyboard input to 
            if cv.waitKey(10) & 0xFF == ord('q'):
                break
            if leftFrameNumber > 50:
                break

        # Getting Right Frame
        while True:
            # Getting frames from camera
            isRet, imageFrame = videoStream.read()

            # Converting frames to gray scale
            gray_frame = cv.cvtColor(imageFrame,cv.COLOR_BGR2GRAY)

            # profile detector model can only detect left profiles so we will have to flip the image to detect right profile
            gray_frame = cv.flip(gray_frame,1)

            # Loading face detector from opencv library
            face_detector_profile = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_profileface.xml")

            # Detecting Faces
            face_profile = face_detector_profile.detectMultiScale(gray_frame, minNeighbors=10, minSize=(30,30))

            # Getting height and width of frame
            height,width = imageFrame.shape[:2]

            # Creating Box Around Face and Saving Image
            if len(face_profile) == 1:
                for (x, y, w, h) in face_profile:
                    face = gray_frame[y:y+h, x:x+w]
                    face = setImageDimension(face)
                    face = cv.flip(face,1)
                    if rightFrameNumber <= 50:
                        captured_image.append(face)
                        rightFrameNumber += 1
                    imageFrame = faceBox(imageFrame,"Right",rightFrameNumber,width-x-w,y,w,h)

            # Writing Text
            message = 'Please Look Left'
            textSize = cv.getTextSize(message,cv.FONT_HERSHEY_SIMPLEX, 1.2,2)[0]
            imageFrame = cv.putText(imageFrame, message, ((width//2) - (textSize[0] // 2), height-textSize[1]), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
                    
            # Displaying Image
            imageFrame = scaleFrame(imageFrame,1.35)
            cv.imshow("Saving Images",imageFrame)

            # Checking for keyboard input to 
            if cv.waitKey(10) & 0xFF == ord('q'):
                break
            if rightFrameNumber > 50:
                break

        videoStream.release()
        cv.destroyAllWindows()

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
    year_label = tkinter.Label(
        frame, text="Year", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    year_values = ["FE", "SE", "TE", "BE"]
    year_combobox = ttk.Combobox(frame, values=year_values, font=("Arial", 16))
    year_combobox.set(year_values[0])  # Set the default value
    division_label = tkinter.Label(
        frame, text="Division", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    division_values = ["A", "B"]
    division_combobox = ttk.Combobox(frame, values=division_values, font=("Arial", 16))
    division_combobox.set("A")  # Set the default value
    submit_button = tkinter.Button(
        frame, text="Submit", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=submitButtonOnClick)

    capture_image_button = tkinter.Button(
        frame, text="Capture Image", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=capture_image)

    # Bind the roll_number_entry to the validate_roll_number_input function
    roll_number_entry.bind('<KeyRelease>', validate_roll_number_input)

    # Bind the gr_number_entry to the validate_gr_number_input function
    gr_number_entry.bind('<KeyRelease>', validate_gr_number_input)

    # Bind the year_combobox to the validate_year_input function
    year_combobox.bind('<<ComboboxSelected>>', validate_year_input)

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
    year_label.grid(row=6, column=0)
    year_combobox.grid(row=6, column=1, pady=20)
    division_label.grid(row=7, column=0)
    division_combobox.grid(row=7, column=1, pady=20)
    capture_image_button.grid(row=8, column=0, columnspan=2, pady=10)
    submit_button.grid(row=9, column=0, columnspan=2, pady=10)
    frame.pack()

    window.mainloop()