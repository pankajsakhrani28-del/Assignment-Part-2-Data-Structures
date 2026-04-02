menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


##### Task 1 — Explore the Menu

# Group menu by category
categories = set(item["category"] for item in menu.values())

for category in categories:
    print(f"\n===== {category} =====")
    
    for name, details in menu.items():
        if details["category"] == category:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{name:<15} ₹{details['price']:.2f}   [{status}]")

# ---- Calculations ----

# Total number of items
total_items = len(menu)

# Total available items
available_items = sum(1 for item in menu.values() if item["available"])

# Most expensive item
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])

# Items under ₹150
cheap_items = [(name, details["price"]) for name, details in menu.items() if details["price"] < 150]

# ---- Print Results ----
print("\n--- Summary ---")
print("Total items on menu:", total_items)
print("Total available items:", available_items)

print(f"Most expensive item: {most_expensive[0]} (₹{most_expensive[1]['price']:.2f})")

print("\nItems under ₹150:")
for name, price in cheap_items:
    print(f"{name} (₹{price:.2f})")


##### Task 2 — Cart Operations

cart = []

# ---------------- FUNCTIONS ---------------- #

def add_to_cart(item_name, quantity):
    # Check if item exists
    if item_name not in menu:
        print(f"❌ {item_name} not found in menu.")
        return

    # Check availability
    if not menu[item_name]["available"]:
        print(f"❌ {item_name} is currently unavailable.")
        return

    # Check if already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"✅ Updated {item_name} quantity to {item['quantity']}")
            return

    # Add new item
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    print(f"✅ Added {item_name} x{quantity} to cart")


def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"🗑️ Removed {item_name} from cart")
            return

    print(f"❌ {item_name} not found in cart")


def update_quantity(item_name, quantity):
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = quantity
            print(f"🔄 Updated {item_name} quantity to {quantity}")
            return

    print(f"❌ {item_name} not found in cart")


def print_cart():
    print("\n🛒 Current Cart:")
    if not cart:
        print("Cart is empty")
        return

    for item in cart:
        print(f"{item['item']} x{item['quantity']} (₹{item['price']})")


# ---------------- SIMULATION ---------------- #

# Step 1
add_to_cart("Paneer Tikka", 2)
print_cart()

# Step 2
add_to_cart("Gulab Jamun", 1)
print_cart()

# Step 3
add_to_cart("Paneer Tikka", 1)
print_cart()

# Step 4
add_to_cart("Mystery Burger", 1)
print_cart()

# Step 5
add_to_cart("Chicken Wings", 1)
print_cart()

# Step 6
remove_from_cart("Gulab Jamun")
print_cart()


# ---------------- ORDER SUMMARY ---------------- #

print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    total_price = item["quantity"] * item["price"]
    subtotal += total_price
    print(f"{item['item']:<18} x{item['quantity']}    ₹{total_price:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):                ₹{gst:.2f}")
print(f"Total Payable:           ₹{total:.2f}")
print("====================================")    



##### Task 3 — Inventory Tracker with Deep Copy

import copy

# --------- STEP 1: Deep Copy --------- #
inventory_backup = copy.deepcopy(inventory)

print(" Backup created.\n")

# --------- STEP 2: Modify inventory to prove deep copy --------- #
inventory["Paneer Tikka"]["stock"] = 5

print("🔍 After modifying inventory:\n")

print("Current Inventory (modified):")
for item, details in inventory.items():
    print(item, details)

print("\nBackup Inventory (should be unchanged):")
for item, details in inventory_backup.items():
    print(item, details)

# --------- STEP 3: Restore inventory --------- #
inventory = copy.deepcopy(inventory_backup)
print("\n Inventory restored.\n")


# --------- STEP 4: Deduct items from cart --------- #
print(" Processing Order...\n")

for cart_item in cart:
    name = cart_item["item"]
    qty = cart_item["quantity"]

    stock = inventory[name]["stock"]

    if stock >= qty:
        inventory[name]["stock"] -= qty
        print(f" {name}: Deducted {qty}, Remaining {inventory[name]['stock']}")
    else:
        print(f"⚠ Not enough stock for {name}. Only {stock} available.")
        inventory[name]["stock"] = 0


# --------- STEP 5: Reorder Alerts --------- #
print("\n Reorder Alerts:\n")

for item, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")


# --------- STEP 6: Final Comparison --------- #
print("\n Final Inventory:")
for item, details in inventory.items():
    print(item, details)

print("\n Backup Inventory (Original):")
for item, details in inventory_backup.items():
    print(item, details)



##### Task 4 — Daily Sales Log Analysis

# --------- STEP 1: Total revenue per day --------- #
print(" Revenue Per Day:\n")

daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date} : ₹{total:.2f}")

# --------- STEP 2: Best-selling day --------- #
best_day = max(daily_revenue.items(), key=lambda x: x[1])

print(f"\n Best Selling Day: {best_day[0]} (₹{best_day[1]:.2f})")


# --------- STEP 3: Most ordered item --------- #
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count.items(), key=lambda x: x[1])

print(f"\n Most Ordered Item: {most_ordered[0]} ({most_ordered[1]} times)")


# --------- STEP 4: Add new day --------- #
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print("\n Updated Revenue Per Day:\n")

daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    print(f"{date} : ₹{total:.2f}")

# Updated best day
best_day = max(daily_revenue.items(), key=lambda x: x[1])
print(f"\n New Best Selling Day: {best_day[0]} (₹{best_day[1]:.2f})")


# --------- STEP 5: Numbered list of all orders --------- #
print("\n All Orders:\n")

all_orders = []

for date, orders in sales_log.items():
    for order in orders:
        all_orders.append((date, order))

for i, (date, order) in enumerate(all_orders, start=1):
    items = ", ".join(order["items"])
    print(f"{i}.  [{date}] Order #{order['order_id']}  — ₹{order['total']:.2f} — Items: {items}")