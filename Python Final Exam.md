**Final Exam**

**Bangladesh Bus Ticket Booking System** 

**OOP with Python 										       (100 Marks)**

| Part | Requirement | Details | Marks |
| ----- | ----- | ----- | ----- |
| **1** | **Bus Class** | \- Attributes: `number`, `route`, `total_seats`, `booked_seats = 0` \- Method `available_seats()` returns unbooked seats \- Method `book_seat()` books if seats available | 20 |
| **2** | **Passenger Class** | \- Attributes: `name`, `phone`, `bus` (reference to a `Bus` object) | 15 |
| **3** | **BusSystem Class** | \- Manages all buses and bookings \- Attributes: `buses` list, `passengers` list | 5 |
| **4** | **Admin Class**  | \- Class `Admin` with attributes: `username`, `password` \- Method: `login()` to validate credentials | 5 |
| **5** | **Add Bus Method** | \- Method: `add_bus(number, route, seats)` \- Adds new `Bus` to system (Only admin can do this) | 10 |
| **6** | **Book Ticket Method** | \- Method: `book_ticket(bus_number, name, phone)` \- Finds bus, checks seat availability, books ticket, adds `Passenger` | 15 |
| **7** | **View Buses Method** | \- Method: `show_buses()` \- Displays each bus with available seats | 5 |
| **8** | **Admin Login (Feature)** | \- Simple login system using `Admin` class Username \= `"admin"` Password \= `"1234"` \- Only after login, admin can access the Admin Menu | 10 |
| **9** | **User Menu (for everyone)** | Menu options for all users: 1\. Admin Login 2\. Book Ticket 3\. View Buses 4\. Exit | 5 |
| **10** | **Admin Menu (after successful login)** | Admin-only options after login: 1\. Add Bus 2\. View All Buses 3\. Logout | 5 |
| **11** | **Fixed Fare System** | \- Each ticket must show a fixed fare of ৳500 | 5 |
| **12** | **Input Validation & User Feedback** | \- Handle invalid choices and show clear prompts and messages | 5 |
| **Total Marks:** |  |  | 100 |

#### **Things To Submit:**

* Keep full code in one Google Doc and make it public.  
* Submit the public link.