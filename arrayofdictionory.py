# Employee Management System

# List to store employee details (each element is a dictionary)
employees = []

# Function to add an employee
def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))

    # Create a dictionary for the employee details
    employee_info = {'ID': emp_id, 'Name': name, 'Position': position, 'Salary': salary}

    # Add the employee dictionary to the list
    employees.append(employee_info)
    print(f"Employee ID {emp_id} added successfully!")

# Function to display all employee details
def display_employees():
    print("\nEmployee Details:")
    for emp_info in employees:
        print(f"Employee ID: {emp_info['ID']}, Name: {emp_info['Name']}, Position: {emp_info['Position']}, Salary: {emp_info['Salary']}")

# Function to search for an employee
def search_employee():
    emp_id_to_search = input("Enter employee ID to search: ")

    # Find the employee dictionary with the specified ID
    found_employee = next((emp_info for emp_info in employees ), None)

    if found_employee:
        print(f"\nEmployee ID: {found_employee['ID']}, Name: {found_employee['Name']}, Position: {found_employee['Position']}, Salary: {found_employee['Salary']}")
    else:
        print(f"No employee found with ID {emp_id_to_search}.")

# Function to delete an employee
def delete_employee():
    delete_name = input("Enter the name to delete: ")
    

    for employee in employees:
        if employee['Name'].lower() == delete_name.lower():
            employees.remove(employee)
            print("Employee deleted successfully!")
            
            break
# Main loop
while True:
    print("\nOptions:")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        display_employees()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
