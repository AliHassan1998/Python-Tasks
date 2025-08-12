
```python
import datetime
from perishable_product_system.perishable_product_system import Product, PerishableProduct

def test_product_from_string_and_discount():
    p = Product.from_string("P002,Pencils,4.0,100")
    assert p.name == "Pencils"
    assert p.apply_discount(10) == 3.6  # 10% off 4.0 -> 3.6

def test_perishable_days_and_expiry():
    pp = PerishableProduct.from_string("PP004,Yogurt,15.0,200,2025-08-20")
    days = pp.days_until_expiry("2025-08-18")
    assert days == 2
    assert not pp.is_expired("2025-08-18")
    assert pp.is_expired("2025-08-21")

def test_reduce_price_near_expiry_sets_price_or_zero():
    pp = PerishableProduct("PP005", "Cheese", 10.0, 10, "2025-08-14")
    # within 3 days threshold on 2025-08-12 -> reduce by 50%
    new_price = pp.reduce_price_if_near_expiry("2025-08-12", days_threshold=3, reduction_percentage=50)
    assert new_price == pp.price
