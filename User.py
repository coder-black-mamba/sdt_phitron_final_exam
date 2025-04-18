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