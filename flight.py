# Airport Management System

# Nested dictionary to store flight details
flights = {}

# Function to add a flight
def add_flight():
    flight_number = input("Enter flight number: ")
    destination = input("Enter destination: ")
    departure_time = input("Enter departure time: ")

    # Create a dictionary for the flight details
    flight_info = {'Destination': destination, 'Departure Time': departure_time, 'Passengers': {}}

    # Add the flight to the main dictionary
    flights[flight_number] = flight_info
    print(f"Flight {flight_number} added successfully!")

# Function to display all flight details
def display_flights():
    print("\nFlight Details:")
    for flight_number, info in flights.items():
        print(f"Flight Number: {flight_number}, Destination: {info['Destination']}, Departure Time: {info['Departure Time']}")
        print("Passengers:")
        for passenger_name in info['Passengers']:
            print(f"  - {passenger_name}")

# Function to add a passenger to a flight
def add_passenger():
    flight_number = input("Enter flight number: ")

    if flight_number in flights:
        passenger_name = input("Enter passenger name: ")
        flights[flight_number]['Passengers'][passenger_name] = True
        print(f"Passenger {passenger_name} added to Flight {flight_number} successfully!")
    else:
        print(f"No flight found with number {flight_number}.")

# Main loop
while True:
    print("\nAirport Management System Options:")
    print("1. Add Flight")
    print("2. Display Flights")
    print("3. Add Passenger to Flight")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_flight()
    elif choice == '2':
        display_flights()
    elif choice == '3':
        add_passenger()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
