# Python E-commerce Command Line Project

## Project Description
Create a command-line e-commerce system that manages products, orders, and users using Python. The system should use lists and dictionaries for data storage and tabulate for formatted output.

## Required Data Structures

### 1. Users Data Structure
```python
users = [
    {
        "id": 1,
        "username": "admin",
        "password": "admin123",
        "role": "admin"
    },
    {
        "id": 2,
        "username": "john",
        "password": "john123",
        "role": "customer"
    }
]
```

### 2. Products Data Structure
```python
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 999.99,
        "stock": 10
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 499.99,
        "stock": 15
    }
]
```

### 3. Cart Data Structure
```python
cart = [
    {
        "user_id": 2,
        "product_id": 1,
        "quantity": 2
    }
]
```

### 4. Orders Data Structure
```python
orders = [
    {
        "id": 1,
        "user_id": 2,
        "items": [
            {
                "product_id": 1,
                "quantity": 2
            }
        ],
        "date": "2024-11-12 10:30:45",
        "total": 1999.98
    }
]
```

## Required Features & Expected Outputs

### 1. Main Menu
Expected Output:
```
=== E-commerce Management System ===
1. Login
2. Exit

Enter your choice: 
```

### 2. Admin Menu After Login
Expected Output:
```
Welcome, admin!

1. Manage Products
2. View All Products
3. Logout

Enter your choice:
```

### 3. Customer Menu After Login
Expected Output:
```
Welcome, john!

1. View Products
2. Add to Cart
3. View Cart
4. Checkout
5. Order History
6. Logout

Enter your choice:
```

### 4. Product Display (Using tabulate)
Expected Output:
```
=== Products ===
+----+--------------+---------+-------+
| ID | Name         | Price   | Stock |
+====+==============+=========+=======+
| 1  | Laptop       | $999.99 | 10    |
| 2  | Smartphone   | $499.99 | 15    |
| 3  | Headphones   | $99.99  | 20    |
+----+--------------+---------+-------+
```

### 5. Cart Display
Expected Output:
```
=== Your Cart ===
+-----------+----------+---------+---------+
| Product   | Quantity | Price   | Total   |
+===========+==========+=========+=========+
| Laptop    | 2        | $999.99 | $1999.98|
+-----------+----------+---------+---------+

Total Amount: $1999.98
```

### 6. Order History Display
Expected Output:
```
=== Order History ===

Order ID: 1
Date: 2024-11-12 10:30:45
+-----------+----------+---------+---------+
| Product   | Quantity | Price   | Total   |
+===========+==========+=========+=========+
| Laptop    | 2        | $999.99 | $1999.98|
+-----------+----------+---------+---------+
Total Amount: $1999.98
```

## Required Libraries
```python
from tabulate import tabulate
from datetime import datetime
```

## Project Requirements

1. **Code Structure**
   - Organize code into functions
   - Use while loops for menus
   - Implement proper error handling
   - Use tabulate for all table displays

2. **User Authentication**
   - Login system with role-based access
   - Input validation for credentials

3. **Product Management (Admin)**
   - Add/Update/Delete products
   - View all products
   - Stock management

4. **Shopping Cart**
   - Add products to cart
   - View cart
   - Stock validation when adding
   - Clear cart after checkout

5. **Order Management**
   - Generate unique order IDs
   - Store order history
   - Update product stock after order
   - Display order details with totals

## Submission Requirements

### GitHub Repository Structure
```
ecommerce-cli/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── auth.py        (optional - authentication functions)
│   ├── products.py    (optional - product management)
│   ├── orders.py      (optional - order management)
│   └── utils.py       (optional - utility functions)
├── data/              (optional - if implementing file storage)
│   ├── users.json
│   ├── products.json
│   └── orders.json
└── tests/             (optional - unit tests)
    └── test_main.py
```

### README.md Should Include
1. Project description
2. Setup instructions
3. Features implemented
4. Sample test credentials
5. Screenshots of running application (optional)

### Requirements.txt Should Include
```
tabulate==0.9.0
```

## Test Credentials
```
Admin:
- Username: admin
- Password: admin123

Customer:
- Username: john
- Password: john123
```

## Sample User Flow

1. **Login as Admin:**
   - Add new products
   - Update stock
   - View all products

2. **Login as Customer:**
   - View products
   - Add items to cart
   - View cart
   - Checkout
   - View order history

## Bonus Features (Optional)
1. Data persistence using JSON files
2. Password hashing
3. Product search functionality
4. Input validation with proper error messages
5. Unit tests
6. Product categories
7. Discount system

## Evaluation Criteria
1. Code organization and clarity
2. Implementation of all required features
3. Proper error handling
4. User interface design
5. GitHub repository structure
6. Documentation quality
7. Code consistency and style

## Additional Notes
- Use meaningful variable and function names
- Add comments for complex logic
- Handle edge cases (empty cart, insufficient stock, etc.)
- Maintain data integrity throughout operations
- Follow Python PEP 8 style guide

Would you like me to provide any additional details or clarify any part of the requirements?