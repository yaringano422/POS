# tests/test_sales.py
import pytest
from services.sales import SalesService
from services.inventory import InventoryService
from data.models import Sale, Product, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.database import Base
from datetime import datetime

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    yield Session()

def test_register_sale(db_session):
    inventory_service = InventoryService(db_session)
    sales_service = SalesService(db_session)

    # Agregar producto
    inventory_service.add_product("Producto 1", "Marca A", "Categoría X", 100.0, 10)

    # Agregar usuario
    user = User(username="vendedor1", role="vendedor")
    db_session.add(user)
    db_session.commit()

    # Registrar venta
    product = db_session.query(Product).first()
    sales_service.register_sale(product_id=product.id, user_id=user.id, quantity=2)

    # Verificar la venta
    sales = db_session.query(Sale).all()
    assert len(sales) == 1
    assert sales[0].quantity == 2
    assert sales[0].total_price == 200.0