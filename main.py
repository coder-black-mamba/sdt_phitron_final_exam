FARE=500


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus

    def __repr__(self):
        return f"Passenger : {self.name} , Age : {self.phone} , Bus NUmber : {self.bus.number} "


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__bus_system = None


    def set_bus_system(self,bus_system):
        self.__bus_system = bus_system

    def login(self, username, password):
        return self.username == username and self.password == password

    def add_bus(self,  bus):
        self.__bus_system.add_bus(bus)

    def add_passenger(self, passenger):
        self.__bus_system.add_passenger(passenger)


    def book_seat(self,  bus_number):
        self.__bus_system.book_seat(bus_number)

    def display_available_seats(self):
        self.__bus_system.display_available_seats()

    def display_passengers(self):
        self.__bus_system.display_passengers()


from User import Passenger


class Bus:
    def __init__(self,number , route,total_seats,booked_seats=0):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = booked_seats


    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            print("Seat booked successfully!")
            return True
        else :
            print("Sorry, no seats available.")
            return False


    def __repr__(self):
        return f"Bus : {self.number} , Route : {self.route} , Available Seats : {self.available_seats()} "




class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []

    def add_bus(self, bus):
        self.buses.append(bus)
        print(f"Bus {bus} added successfully!")

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def book_seat(self, bus_number):
        for bus in self.buses:
            if bus.number == bus_number:
                bus.book_seat()
                return
        print("Bus not found.")

    def show_buses(self):
        if not self.buses:
            print("No buses available.")
            return
        for bus in self.buses:
            print(bus)

    def book_ticket(self,bus_number, name, phone):


        bus_wanted_to_book=None

        for bus in self.buses:
            if bus.number == bus_number:
                bus_wanted_to_book = bus
                break

        if not bus_wanted_to_book :
            print("Bus not found.")
            return

        if bus_wanted_to_book.book_seat():
            passenger = Passenger(name, phone, bus_wanted_to_book)
            self.passengers.append(passenger)
            print(f"Ticket Booked For {name} , On Bus : {bus_wanted_to_book.number} On Route : {bus_wanted_to_book.route} Fare : {FARE},successfully!")

    def display_passengers(self):
        for passenger in self.passengers:
            print(passenger)




bus_system = BusSystem()
while True:
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")
    choice = input("Enter your choice: ")


    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        admin = Admin("admin", "1234")

        # checking admin login
        if not admin.login(username, password):
            print("Incorrect Username Or Password !")
            continue

        admin.set_bus_system(bus_system)


        while True:
            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                try:
                    number = int(input("Enter bus number: "))

                    # check is bus number already exists
                    bus_exists=False
                    for bus in bus_system.buses:
                        if bus.number == number:
                            print("Bus number already exists.")
                            bus_exists=True

                    if bus_exists:
                        continue

                    route = input("Enter bus route: ")
                    total_seats = int(input("Enter total seats: "))

                    if number<=0 or route =="" or total_seats<=0:
                        print("Please Fill All Of The Fields Correctly!")
                        continue

                    bus = Bus(number, route, total_seats)
                    admin.add_bus(bus)


                except Exception as e:
                    print("Please Enter Valid Number !")
                    continue


            elif choice == "2":
                bus_system.show_buses()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
    elif choice == "2":
        try:
            if len(bus_system.buses)<=0:
                print("No Buses Available !")
                continue
            bus_system.show_buses()
            bus_number = int(input("Enter bus number: "))
            name = input("Enter passenger name: ")
            phone = input("Enter passenger phone: ")
            if bus_number<=0 or name == "" or len(phone) !=11:
                print("Please Fill All Of The Fields Correctly !")
                continue
            bus_system.book_ticket(bus_number, name, phone)
        except Exception as e:
            print("Please Enter Valid Number !")
            continue

    elif choice == "3":
        bus_system.show_buses()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
























