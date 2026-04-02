#  Restaurant Menu & Order Management System

This project is a **Python-based Restaurant Management System** built using core data structures such as:

* Lists
* Dictionaries
* Nested dictionaries

It simulates real-world restaurant operations including menu handling, cart management, inventory tracking, and sales analysis.

---

# 📌 Features Overview

The system is divided into 4 main modules:

---

#  Task 1 — Menu Exploration

###  Features:

* Display menu grouped by category
* Show item price and availability
* Perform analysis:

  * Total number of items
  * Available items
  * Most expensive item
  * Items under ₹150

###  Output:

```
===== Starters =====
Paneer Tikka     ₹180.00   [Available]
Chicken Wings    ₹220.00   [Unavailable]
Veg Soup         ₹120.00   [Available]

===== Mains =====
Butter Chicken   ₹320.00   [Available]
Dal Tadka        ₹180.00   [Available]
Veg Biryani      ₹250.00   [Available]
Garlic Naan      ₹40.00    [Available]

===== Desserts =====
Gulab Jamun      ₹90.00    [Available]
Rasgulla         ₹80.00    [Available]
Ice Cream        ₹110.00   [Unavailable]

--- Summary ---
Total items on menu: 10
Total available items: 8
Most expensive item: Butter Chicken (₹320.00)

Items under ₹150:
Veg Soup (₹120.00)
Garlic Naan (₹40.00)
Gulab Jamun (₹90.00)
Rasgulla (₹80.00)
Ice Cream (₹110.00)

#  Task 2 — Cart Operations

###  Features:

* Add items to cart
* Update quantity instead of duplicates
* Remove items
* Handle unavailable/non-existent items
* Generate bill with GST (5%)

###  Output:

========== Order Summary ==========
Paneer Tikka       x3    ₹540.00
------------------------------------
Subtotal:                ₹540.00
GST (5%):                ₹27.00
Total Payable:           ₹567.00
====================================
```

---

#  Task 3 — Inventory Tracker (Deep Copy)

###  Features:

* Uses `copy.deepcopy()` for safe backup
* Demonstrates independent copy behavior
* Deducts stock after order
* Prevents negative stock
* Shows reorder alerts

###  Output:

```
 After modifying inventory:

Current Inventory (modified):
Paneer Tikka {'stock': 5, 'reorder_level': 3}

Backup Inventory (unchanged):
Paneer Tikka {'stock': 10, 'reorder_level': 3}

 Inventory restored.

 Processing Order...

 Paneer Tikka: Deducted 3, Remaining 7

 Reorder Alerts:

 Reorder Alert: Rasgulla — Only 4 unit(s) left (reorder level: 3)

 Final Inventory:
Paneer Tikka {'stock': 7, 'reorder_level': 3}

 Backup Inventory:
Paneer Tikka {'stock': 10, 'reorder_level': 3}


#  Task 4 — Sales Log Analysis

###  Features:

* Calculate revenue per day
* Identify best-selling day
* Find most ordered item
* Add new sales data dynamically
* Display all orders using `enumerate()`

###  Output:

 Revenue Per Day:

2025-01-01 : ₹790.00
2025-01-02 : ₹560.00
2025-01-03 : ₹960.00
2025-01-04 : ₹570.00

 Best Selling Day: 2025-01-03 (₹960.00)

 Most Ordered Item: Garlic Naan (5 times)


###  After Adding New Day:

```
2025-01-05 : ₹750.00

 New Best Selling Day: 2025-01-03 (₹960.00)
```

---

###  All Orders (Enumerated):

```
1.  [2025-01-01] Order #1  — ₹220.00 — Items: Paneer Tikka, Garlic Naan
2.  [2025-01-01] Order #2  — ₹210.00 — Items: Gulab Jamun, Veg Soup
3.  [2025-01-01] Order #3  — ₹360.00 — Items: Butter Chicken, Garlic Naan
4.  [2025-01-02] Order #4  — ₹220.00 — Items: Dal Tadka, Garlic Naan
...
```

---

#  How to Run

1. Install Python 3.x
2. Open terminal or VS Code
3. Run:

```
python restaurant.py
```

---

#  Concepts Used

* Dictionaries & Nested Dictionaries
* Lists & List Comprehension
* Functions
* Loops & Conditional Logic
* `copy.deepcopy()`
* `enumerate()`
* Data Aggregation

---

#  Future Improvements

* Add interactive user input system
* Connect with database (SQLite/MySQL)
* Build GUI (Tkinter / Web App)
* Add authentication system

---


 This project demonstrates how core Python data structures can be used to build a real-world restaurant management system.
