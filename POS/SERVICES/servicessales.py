# services/sales.py
from sqlalchemy.orm import Session
from ..data.models import Sale, Product, User
from datetime import datetime

class SalesService:
    def __init__(self, db: Session):
        self.db = db

    def register_sale(self, product_id: int, user_id: int, quantity: int):
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if not product or product.stock < quantity:
            raise ValueError("Stock insuficiente")

        product.stock -= quantity
        sale = Sale(
            product_id=product_id,
            user_id=user_id,
            quantity=quantity,
            total_price=quantity * product.price,
            date=datetime.now()
        )
        self.db.add(sale)
        self.db.commit()

    def get_sales_by_user(self, user_id: int):
        return self.db.query(Sale).filter(Sale.user_id == user_id).all()

    def get_all_sales(self):
        return self.db.query(Sale).all()