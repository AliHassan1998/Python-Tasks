# Perishable Product System (Product → PerishableProduct)

This project demonstrates a simple product model and a perishable-product extension with expiry handling.

## Overview

- `Product` — base class with `product_id`, `name`, `price`, `quantity`, property validation, discount, and update methods.
- `PerishableProduct` — inherits from `Product`, adds `expiry_date` handling and utility methods:
  - `is_expired(current_date)`
  - `days_until_expiry(current_date)`
  - `reduce_price_if_near_expiry(current_date, days_threshold, reduction_percentage)`

## Features

- Property getters/setters for `price` and `quantity` with validation
- `from_string()` factory constructors
- Date validation (`YYYY-MM-DD` or `datetime.date`)
- Practical expiry utilities (days until expiry, automatic price reduction)
- Nicely formatted `__str__` and `display_details()`

## Usage

```python
from perishable_product_system.perishable_product_system import Product, PerishableProduct
import datetime

p = Product("P001", "Notebook", 10.0, 50)
pp = PerishableProduct("PP003", "Milk", 20.0, 150, "2025-08-14")

print(pp.days_until_expiry("2025-08-12"))
pp.reduce_price_if_near_expiry("2025-08-12", days_threshold=3, reduction_percentage=30)
```python
## Run locally
# run the script
python perishable_product_system/perishable_product_system.py

## Notes
Date format accepted: YYYY-MM-DD or datetime.date object.
This task uses only Python standard library (datetime) — no external packages required.
