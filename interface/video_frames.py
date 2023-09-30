import cv2 as cv

def setImageDimension(frame):
    dimensions =  (150,150)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_CUBIC)

def captureFrames():
    frames = []
    videoStream = cv.VideoCapture(0)

    while len(frames) < 25:
        isRet, frame = videoStream.read()
        gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        frames.append(gray_frame)
    
    return frames

def get_faces(frames):
    faces = []
    # Loading face detector from opencv library
    face_detector_frontal = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    face_detector_profile = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_profileface.xml")

    for frame in frames:
        # Detecting Faces
        face_frontal = face_detector_frontal.detectMultiScale(frame, minNeighbors=10, minSize=(25,25))
        for (x, y, w, h) in face_frontal:
            face = frame[y:y+h, x:x+w]
            face = setImageDimension(face)
            faces.append(face)
        
        face_profile = face_detector_profile.detectMultiScale(frame, minNeighbors=10, minSize=(25,25))
        for (x, y, w, h) in face_profile:
            face = frame[y:y+h, x:x+w]
            face = setImageDimension(face)
            faces.append(face)

        flipped_frame = cv.flip(frame,1)
        face_profile = face_detector_profile.detectMultiScale(flipped_frame, minNeighbors=10, minSize=(25,25))
        for (x, y, w, h) in face_profile:
            face = flipped_frame[y:y+h, x:x+w]
            face = setImageDimension(face)
            face = cv.flip(face,1)
            faces.append(face)

        return faces

def getStudents(faces):
    student = set()

    for face in faces:
        recognizer = cv.face.EigenFaceRecognizer_create()
        recognizer.read("Face_Recognizer.xml")
        label,_  = recognizer.predict(face)
        student.add(label)

    return list(student)