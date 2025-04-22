# services/inventory.py
from sqlalchemy.orm import Session
from ..data.models import Product

class InventoryService:
    def __init__(self, db: Session):
        self.db = db

    def add_product(self, name: str, brand: str, category: str, price: float, stock: int):
        new_product = Product(
            name=name,
            brand=brand,
            category=category,
            price=price,
            stock=stock
        )
        self.db.add(new_product)
        self.db.commit()

    def get_products_by_category(self, category: str):
        return self.db.query(Product).filter(Product.category.ilike(f"%{category}%")).all()

    def get_all_categories(self):
        return list(set([product.category for product in self.db.query(Product).all()]))