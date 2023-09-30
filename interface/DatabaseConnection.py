import mysql.connector


class DatabaseConnection:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            username="attendance_user",
            password="attendance_pass",
            database="attendance_system"
        )
        self.cursor = "Cursor"

    def __del__(self):
        # Closing Database Connection
        del self.cursor

    def executeReadQuery(self, query):
        self.cursor = self.db.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def executeUpdateQuery(self, query):
        self.cursor = self.db.cursor()
        self.cursor.execute(query)
        self.db.commit()
        self.cursor.close()

    def insertStudentDetails(self, roll_no,firstname, lastname, email,gr_no, year, division ):
        query = "INSERT INTO student VALUES(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\");".format(gr_no, roll_no,year,division, firstname,lastname,email)
        self.executeUpdateQuery(query)

    def insertTeacherDetails(self,username,firstname,lastname,password):
        query = "INSERT INTO teacher VALUES(\"{}\",\"{}\",\"{}\",\"{}\");".format(username,firstname,lastname,password)
        self.executeUpdateQuery(query)

    def getTeacherList(self):
        query = "SELECT username FROM teacher;"
        result = self.executeReadQuery(query)
        return [i[0] for i in result]
    
    def insertCourseDetails(self,course_id,course_name,year,division,teacher):
        query = "INSERT INTO course VALUES({},\"{}\",\"{}\",\"{}\",\"{}\");".format(course_id,course_name,year,division,teacher)
        self.executeUpdateQuery(query)

    def validateUser(self,username,password):
        query = "SELECT EXISTS( SELECT * FROM teacher WHERE username = \"{}\" AND password = \"{}\");".format(username,password)
        result = self.executeReadQuery(query)
        if result[0][0] == 1:
            return True
        return False
    
    def getCourseList(self,teacher):
        query = "SELECT course_id FROM course WHERE teacher = \"{}\";".format(teacher)
        result = self.executeReadQuery(query)
        return [i[0] for i in result]
    
    def addAttendance(self,students,course,date):
        day,month,year = date.split("/")
        fDate = str(year)+"-"+str(month)+"-"+str(day)
        for student in students:
            query = "INSERT INTO attendance VALUES({},{},\"{}\");".format(student,course,fDate)
            self.executeUpdateQuery(query)

    def getReportData(self,teacher):
        query = "SELECT course_id FROM course WHERE teacher = \"{}\";".format(teacher)
        result = self.executeReadQuery(query)
        courses = [i[0] for i in result]

        reportData = {}
        header = ["Name","Roll No","Attendance Count"]
        for course in courses:
            data = [header]
            query = "SELECT firstname,lastname,roll_no,COUNT(lec_date) FROM attendance JOIN student ON student.gr_no = attendance.student WHERE course_id = {} GROUP BY attendance.student;".format(course)
            result =  self.executeReadQuery(query)
            for row in result:
                data.append([row[0]+" "+row[1],row[2],row[3]])
            
            reportData[(course,self.getCourseName(course))] = data
        
        return reportData

    def getCourseName(self,course_id):
        query = "SELECT course_name FROM course WHERE course_id = {};".format(course_id)
        result = self.executeReadQuery(query)
        return result[0][0]