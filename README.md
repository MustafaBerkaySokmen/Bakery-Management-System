# Bakery-Management-System

The **Bakery Management System** is a simple Python-based application designed to manage a small bakery that sells muffins and cupcakes. The system tracks inventory, processes customer orders, and calculates total revenue at the end of the day.

## Features
- Tracks initial stock of muffins and cupcakes.
- Accepts customer orders.
- Ensures sufficient stock before processing orders.
- Computes total daily revenue.
- Provides an end-of-day summary of sales and remaining inventory.

## Installation
To run this project, ensure you have **Python 3.x** installed.

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/bakery-management.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd bakery-management
   ```
3. **Run the script:**
   ```bash
   python BakeryManagement.py
   ```

## Usage
1. The program starts by asking the user to enter:
   - Number of muffins and cupcakes in stock.
   - The price of each item.
2. Customers then place their orders.
   - If there’s enough stock, the order is processed.
   - If stock is insufficient, the order is rejected.
3. Entering **-1** as the order quantity ends the day.
4. The system prints the total revenue and remaining stock.

## Example Output
```
Good morning, welcome to the bakery!
-----------------
How many muffins do we have in stock for today?: 10
How much does each muffin cost?: 2.0
How many cupcakes do we have in stock for today?: 15
How much does each cupcake cost?: 2.5
Great! Let’s start accepting customers..
-----------------
```

## License
This project is licensed under the **MIT License**.

## Contributions
Contributions are welcome! If you’d like to improve this project:
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact
For any questions or support, please open an issue on GitHub.

