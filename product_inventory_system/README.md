# 📦 Product Inventory System with Operator Overloading

This project demonstrates how to build a basic inventory system using Python classes and dunder methods (magic methods).

## 🧾 Features

- Add products with name, price, and quantity
- Overload operators:
  - `+` ➜ Merge similar products
  - `*` ➜ Multiply quantity or apply discount
  - `==`, `<`, `>` ➜ Compare products
  - `len()` ➜ Get name length
  - `__call__()` ➜ Restock quantity with function call syntax
- Create products from strings
- Display all created products

## 💡 Concepts Used

- Object-Oriented Programming
- Operator Overloading
- Static & Class Methods
- Data Validation
- Error Handling

## 🚀 Example

```python
p1 = Product("Notebook", 5.0, 10)
p2 = Product.from_string("Notebook,3.0,20")
p3 = p1 + p2
p4 = p3 * 0.5   # 50% discount
p5 = p4 * 2     # restock

## 🧠 Output Snapshot
Product's Details: 
Product Name: Notebook 
Product Price: 8.0 
Product Quantity: 30
