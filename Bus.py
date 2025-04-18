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
        else :
            print("Sorry, no seats available.")


    def __repr__(self):
        return f"Bus : {self.number} , Route : {self.route} Available Seats : {self.available_seats()} "




class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []

    def add_bus(self, bus):
        self.buses.append(bus)
        print(f"{bus} Added Successfully .")

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def book_seat(self, bus_number):
        for bus in self.buses:
            if bus.number == bus_number:
                bus.book_seat()
                return
        print("Bus not found.")

    def show_buses(self):
        for bus in self.buses:
            print(bus)

    def book_ticket(self,bus_number, name, phone):
        self.show_buses()


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
            print(f"Ticket Booked For {name} , On Bus : {bus_wanted_to_book.number} On Route : {bus_wanted_to_book.route},successfully!")

    def display_passengers(self):
        for passenger in self.passengers:
            print(passenger)



























