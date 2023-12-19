# Employee Management System

# Nested dictionary to store employee details
employees = {}

# Function to add an employee
def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))

    # Create a dictionary for the employee details
    employee_info = {'Name': name, 'Position': position, 'Salary': salary}

    # Add the employee to the main dictionary
    employees[emp_id] = employee_info
    print(f"Employee ID {emp_id} added successfully!")

# Function to display all employee details
def display_employees():
    print("\nEmployee Details:")
    for emp_id, info in employees.items():
        print(f"Employee ID: {emp_id}, Name: {info['Name']}, Position: {info['Position']}, Salary: {info['Salary']}")

# Function to search for an employee
def search_employee():
    emp_id_to_search = input("Enter employee ID to search: ")
    
    if emp_id_to_search in employees:
        info = employees[emp_id_to_search]
        print(f"\nEmployee ID: {emp_id_to_search}, Name: {info['Name']}, Position: {info['Position']}, Salary: {info['Salary']}")
    else:
        print(f"No employee found with ID {emp_id_to_search}.")

# Function to delete an employee
def delete_employee():
    emp_id_to_delete = input("Enter employee ID to delete: ")
    
    if emp_id_to_delete in employees:
        del employees[emp_id_to_delete]
        print(f"Employee ID {emp_id_to_delete} deleted successfully!")
    else:
        print(f"No employee found with ID {emp_id_to_delete}.")

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
