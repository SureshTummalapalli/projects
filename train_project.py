# This program simulates booking train tickets. It has four classes: Train, Passenger, Ticket and Account.

# The Train class represents a train with its train number, source, destination, and the number of seats available. It has methods to display the train information and book tickets.

# The Passenger class represents a passenger with their name, age, gender, and phone number. It has a method to display passenger information.

# The Ticket class represents a ticket with the train, source, destination, passengers, and PNR (Passenger Name Record) number. It has a method to display ticket information.

# Class called Account is defined with a constructor that takes two arguments: username and password. The class also defines a method called check_password which takes a single argument password and returns a boolean indicating whether the input password matches the stored password.

# --------------------- PROJECT : RAILWAY TICKET BOOKING -----------------------

import random
# We start by importing the random module, which we'll use to generate random PNRs for the tickets later on.

class Train:
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats

    def display_info(self):
        print(f"Train: {self.train_num}, Source: {self.source}, Destination: {self.destination}, Seats: {self.seats}")

    def book_tickets(self, num_tickets):
        if num_tickets > self.seats:
            return None
        self.seats -= num_tickets
        return [random.randint(100000, 999999) for _ in range(num_tickets)]

class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Phone: {self.phone}")

class Ticket:
    def __init__(self, train, passengers, pnr):
        self.train = train
        self.passengers = passengers
        self.pnr = pnr

    def display_info(self):
        print(f"Train: {self.train.train_num}, Source: {self.train.source}, Destination: {self.train.destination}, PNR: {self.pnr}")
        for passenger in self.passengers:
            passenger.display_info()

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

accounts = [Account("user1", "password1"), Account("user2", "password2")]
trains = [
    Train("12737", "Tadepalligudem", "Secunderabad", 40),
    Train("12728", "Tadepalligudem", "Visakhapatnam", 50),
    Train("22863", "Vijayawada", "Bangalore", 1),
]

# User Login or Account Creation
logged_in = None
while not logged_in:
    choice = input("1. Create an account\n2. Login\nEnter choice: ")
    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        accounts.append(Account(username, password))
        print("Account created successfully!")
    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        for account in accounts:
            if account.username == username and account.check_password(password):
                logged_in = account
                print(f"Welcome, {username}!\n")
                break
        else:
            print("Invalid credentials. Try again.")
    else:
        print("Invalid choice. Try again.")

# Display Trains
print("Available Trains:")
for train in trains:
    train.display_info()

# Booking Tickets
while True:
    train_num = input("Enter Train Number: ")
    selected_train = next((train for train in trains if train.train_num == train_num), None)
    if not selected_train:
        print("Invalid Train Number. Try again.")
        continue

    try:
        num_tickets = int(input("Enter Number of Tickets: "))
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be greater than 0.")
        pnr_list = selected_train.book_tickets(num_tickets)
        if not pnr_list:
            print("Not enough seats available.")
        else:
            passengers = []
            for i in range(num_tickets):
                print(f"Passenger {i + 1}:")
                name = input("  Name: ")
                age = int(input("  Age: "))
                gender = input("  Gender: ")
                phone = input("  Phone: ")
                passengers.append(Passenger(name, age, gender, phone))

            print("\nBooking Successful!\n")           
            for i, pnr in enumerate(pnr_list):
                ticket = Ticket(selected_train, [passengers[i]], pnr)
                ticket.display_info()
                print("Wish you a happy and safe journey!")

            break
    except ValueError as e:
        print(f"Error: {e}")
# If the tickets are successfully booked, the program prints "Booking Successful!" and creates a Ticket object for each passenger with the train, source, destination, passenger information, and PNR number. The program then calls the display_info method of each Ticket object to display the information to the user.