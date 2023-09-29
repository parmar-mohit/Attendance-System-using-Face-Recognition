## MySQL Setup

### About
This file contains all the queries that must be executed in MySQL to setup the database for proper functioning of the program.

1. Login into root account of MySQl to create a new Database, New MySQL Account and grant all permission to newly created account on newly created database.Execute the commands given below;
```
CREATE DATABASE attendance_system;

CREATE USER 'attendance_user' IDENTIFIED BY 'attendance_pass';

GRANT ALL PRIVILEGES ON attendance_system.* TO 'attendance_user';

FLUSH PRIVILEGES;
```

2. Login into MySQl using newly created Account and then execute the command given below to define database schema.
```
USE attendance_system;

CREATE TABLE student(
    gr_no VARCHAR(9) PRIMARY KEY,
    roll_no VARCHAR(3),
    year VARCHAR(2),
    division VARCHAR(1),
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    email VARCHAR(50),
    CHECK( division IN ("A","B") ),
    CHECK( year IN ("FE","SE","TE","BE") )
);

CREATE TABLE teacher(
    username VARCHAR(50) PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE course(
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    year VARCHAR(2),
    division VARCHAR(1),
    teacher VARCHAR(50),
    FOREIGN KEY(teacher) REFERENCES teacher(username) ON DELETE CASCADE,
    CHECK( division IN ("A","B") ),
    CHECK( year IN ("FE","SE","TE","BE") )
);

CREATE TABLE attendace(
    student VARCHAR(9),
    course_id INT,
    lec_date DATE,
    FOREIGN KEY(student) REFERENCES student(gr_no) ON DELETE CASCADE,
    FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE CASCADE
);
```

After these commands are executed successfully the mysql is setup and ready for the program.