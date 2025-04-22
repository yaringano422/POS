# tests/test_inventory.py
import pytest
from services.inventory import InventoryService
from data.models import Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data.database import Base

@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    yield Session()

def test_add_product(db_session):
    service = InventoryService(db_session)
    service.add_product("Producto 1", "Marca A", "Categoría X", 100.0, 10)
    products = service.get_products_by_category("Categoría X")
    assert len(products) == 1
    assert products[0].name == "Producto 1"