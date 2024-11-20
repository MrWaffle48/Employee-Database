# Project P4 SQL DB Create
import sqlite3
import datetime

conn = sqlite3.connect('P4Employees.db')
c = conn.cursor()

c.execute('''CREATE TABLE tblEmployee(
EmployeeID INTEGER PRIMARY KEY,
FirstName TEXT,
LastName TEXT,
Salary REAL,
YearStarted INTEGER,
FullTime TEXT)''')

conn.commit()
print("P4Employees.db with table tblEmployee created.")
# function to add a new employee
def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    salary = float(input("Enter Salary: "))
    year_started = int(input("Enter Year Started: "))
    full_time = input("Full Time? (Y/N): ").upper()
    conn.execute("INSERT INTO tblEmployee (EmployeeID, FirstName, LastName, Salary, YearStarted, FullTime) \
                VALUES (?, ?, ?, ?, ?, ?)", (emp_id, first_name, last_name, salary, year_started, full_time))
    conn.commit()
    print("Employee added successfully")

# function to change full-time status for an employee
def change_employee_status():
    emp_id = int(input("Enter Employee ID: "))
    full_time = input("Full Time? (Y/N): ").upper()
    conn.execute("UPDATE tblEmployee SET FullTime = ? WHERE EmployeeID = ?", (full_time, emp_id))
    conn.commit()
    print("Employee status changed successfully")

# function to list all employees
def list_employees():
    cursor = conn.execute("SELECT EmployeeID, FirstName, LastName, Salary, YearStarted, FullTime FROM tblEmployee")
    print("{:<5} {:<10} {:<10} {:>10} {:>6} {:>6}".format("ID", "First", "Last", "Salary", "Year", "Full-Time"))
    print("-" * 50)
    for row in cursor:
        print("{:<5} {:<10} {:<10} {:>10,.2f} {:>6} {:>6}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

# function to list all full-time employees
def list_full_time_employees():
    cursor = conn.execute("SELECT EmployeeID, FirstName, LastName, Salary, YearStarted, FullTime FROM tblEmployee WHERE FullTime = 'Y'")
    print("{:<5} {:<10} {:<10} {:>10} {:>6} {:>6}".format("ID", "First", "Last", "Salary", "Year", "Full-Time"))
    print("-" * 50)
    for row in cursor:
        print("{:<5} {:<10} {:<10} {:>10,.2f} {:>6} {:>6}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

# function to list all part-time employees
def list_part_time_employees():
    cursor = conn.execute("SELECT EmployeeID, FirstName, LastName, Salary, YearStarted, FullTime FROM tblEmployee WHERE FullTime = 'N'")
    print("{:<5} {:<10} {:<10} {:>10} {:>6} {:>6}".format("ID", "First", "Last", "Salary", "Year", "Full-Time"))
    print("-" * 50)
    for row in cursor:
        print("{:<5} {:<10} {:<10} {:>10,.2f} {:>6} {:>6}".format(row[0]))