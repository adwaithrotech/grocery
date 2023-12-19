# Initialize an empty array to store employee dictionaries
employees = []

def add_employee():
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    position = input("Enter employee position: ")

    # Create a dictionary for the new employee
    new_employee = {
        "Name": name,
        "Age": age,
        "Position": position
    }

    # Add the new employee to the array
    employees.append(new_employee)
    print("Employee added successfully!")

def display_employees():
    print("\nEmployee List:")
    for employee in employees:
        print(f"Name: {employee['Name']}, Age: {employee['Age']}, Position: {employee['Position']}")

def search_employee():
    search_name = input("Enter the name to search: ")
    found = False

    for employee in employees:
        if employee['Name'].lower() == search_name.lower():
            print(f"\nEmployee found - Name: {employee['Name']}, Age: {employee['Age']}, Position: {employee['Position']}")
            found = True
            break

    if not found:
        print("Employee not found.")

def delete_employee():
    delete_name = input("Enter the name to delete: ")
    found = False

    for employee in employees:
        if employee['Name'].lower() == delete_name.lower():
            employees.remove(employee)
            print("Employee deleted successfully!")
            found = True
            break

    if not found:
        print("Employee not found.")

# Main program loop
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
