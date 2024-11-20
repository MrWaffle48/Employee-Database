#P4-Hanna
import sqlite3

def main():
    conn = sqlite3.connect('P4Employees.db')
    c = conn.cursor()

    while True:
        print("\n  Menu Options")
        print("1. Add an employee to the database.")
        print("2. Change full-time status for an employee.")
        print("3. List all employees.")
        print("4. Show all part-time employees.")
        print("5. Show all full-time employees.")
        print("6. Show all employees who started their job on/or after a given date.")
        print("7. Exit.")
        
        option = input("Enter option: ")

        if option == "7" or len(option) == 0:
            break

        elif option == "1":
            print("\n1. Add an employee to the database.")
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
            
        elif option == "2":
            print("\n2. Change full-time status for an employee.")
            emp_id = int(input("Enter Employee ID: "))
            full_time = input("Full Time? (Y/N): ").upper()
            conn.execute("UPDATE tblEmployee SET FullTime = ? WHERE EmployeeID = ?", (full_time, emp_id))
            conn.commit()
            print("Employee status changed successfully")
        elif option == "3":
            print("\n3. List all employees.")
            cursor = conn.execute("SELECT EmployeeID, FirstName, LastName, Salary, YearStarted, FullTime FROM tblEmployee")
            print("{:<5} {:<10} {:<10} {:>10} {:>6} {:>6}".format("ID", "First", "Last", "Salary", "Year", "Full-Time"))
            print("-" * 50)
            for row in cursor:
                print("{:<5} {:<10} {:<10} {:>10,.2f} {:>6} {:>6}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        elif option == "4":
            print("\n4. Show all part-time employees.")
            cursor = conn.execute("SELECT EmployeeID, FirstName, LastName, Salary, YearStarted, FullTime FROM tblEmployee WHERE FullTime = 'N'")
            print("{:<5} {:<10} {:<10} {:>10} {:>6} {:>6}".format("ID", "First", "Last", "Salary", "Year", "Full-Time"))
            print("-" * 50)
            for row in cursor:
                print("{:<5} {:<10} {:<10} {:>10,.2f} {:>6} {:>6}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        elif option == "5":
            print("\n5. Show all full-time employees.")
            cursor = conn.execute("SELECT EmployeeID, FirstName, LastName, Salary, YearStarted, FullTime FROM tblEmployee WHERE FullTime = 'Y'")
            print("{:<5} {:<10} {:<10} {:>10} {:>6} {:>6}".format("ID", "First", "Last", "Salary", "Year", "Full-Time"))
            print("-" * 50)
            for row in cursor:
                print("{:<5} {:<10} {:<10} {:>10,.2f} {:>6} {:>6}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        elif option == "6":
            print("\n6. Show all employees who started their job on/or after a given year.")
            date = int(input("Enter a year: "))
            cursor = conn.execute(("SELECT EmployeeID, FirstName, LastName, Salary, YearStarted, FullTime FROM tblEmployee WHERE YearStarted >= '{:0}'").format(date))
            print("{:<5} {:<10} {:<10} {:>10} {:>6} {:>6}".format("ID", "First", "Last", "Salary", "Year", "Full-Time"))
            print("-" * 50)
            for row in cursor:
                print("{:<5} {:<10} {:<10} {:>10,.2f} {:>6} {:>6}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        else:
            print("Invalid option.")

    conn.close()

    print("\nGood-Bye.")

main()
