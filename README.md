#Restaurant Management System (Python OOP Project)

A fully functional Restaurant POS (Point of Sale) System built using Python’s Object-Oriented Programming principles.

This project includes:

- User Management
- Menu Management
- Order Processing
- VAT & Discount Calculation
- Payment Handling
- Order History
- JSON File-Based Storage
- Clean Modular Architecture

---

##Features

###User Module

- Register new users
- Login authentication
- Duplicate username check
- JSON-based user storage

---

###Menu Management

- Add Pizza, Burger, and Drink items
- Dynamic price calculation using Polymorphism
- Menu search feature
- JSON-based menu database
- Extensible structure for adding more items

---

###Order & Billing

- Add multiple items to an order
- Order summary with itemized breakdown
- Subtotal calculation
- VAT (5%) auto calculation
- Optional discount (%)
- Accept customer cash
- Auto-change calculation
- Mark order as paid
- Save order history in JSON file

---

##What I Learned

- Python OOP (Encapsulation, Inheritance, Polymorphism, Abstraction)
- Composition (Order → OrderItem → FoodItem)
- Modular project structure
- JSON as a mini database
- Error handling & input validation
- CLI-based application design
- Clean coding practices
- Version control with Git & GitHub

---

##Project Structure
RestaurantSystem/
│── users/
│ ├── user.py
│ └── users.json
│
│── menu/
│ ├── base_item.py
│ ├── pizza.py
│ ├── burger.py
│ ├── drink.py
│ ├── menu_manager.py
│ └── menu.json
│
│── orders/
│ ├── order_item.py
│ ├── order.py
│ ├── order_manager.py
│ └── orders.json
│
│── main.py
│── README.md

---

##Example Order Output
===== ORDER SUMMARY =====
Customer: Fahim
2 x Chicken Petty Burger = 200.0
Subtotal: 200.0
VAT (5%): 10.0
Total with VAT: 210.0
Discount: 10%
Total Payable: 189.0
Cash: 200
Change: 11.0
Order Completed!

---

##Tech Stack

- Python
- JSON Storage
- CLI Interface
- OOP Architecture

---

##Future Improvements

- Stock / Inventory system
- Sales report (daily / weekly / monthly)
- GUI version
- Upgraded admin dashboard
- Django web version

---

##Author

**MD Fahim Shahriar**  
Python Developer
---If you found this project helpful, feel free to star the repository!
