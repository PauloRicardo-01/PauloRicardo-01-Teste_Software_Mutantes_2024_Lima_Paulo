import pytest

from src.inventory_manager import InventoryManager


@pytest.fixture
def inventory():
    inv = InventoryManager()
    inv.add_product("Apple", 10)
    return inv


def test_add_product(inventory):
    inventory.add_product("Banana", 5)
    assert inventory.inventory["Banana"] == 5


def test_sell_product(inventory):
    assert inventory.sell_product("Apple", 5) is True
    assert inventory.inventory["Apple"] == 5


def test_sell_product_not_enough_stock(inventory):
    assert inventory.sell_product("Apple", 15) is False


def test_check_stock(inventory):
    assert inventory.check_stock("Apple") is True
    assert inventory.check_stock("Banana") is False

## Testes adicionais

def test_add_product_increments_existing_product(inventory):
    # Adiciona um produto existente com uma quantidade adicional
    initial_quantity = inventory.inventory["Apple"]
    inventory.add_product("Apple", 5)  # Incrementa a quantidade
    assert inventory.inventory["Apple"] == initial_quantity + 5, "The quantity of the existing product should be incremented correctly"

# Testes adicionais mutantes

def test_sell_product_exact_stock(inventory):
    inventory.add_product("Grape", 10)
    
    assert inventory.sell_product("Grape", 10) is True
    assert inventory.inventory["Grape"] == 0

def test_check_stock_single_item(inventory):
    inventory.add_product("SingleItem", 1)
    
    has_stock = inventory.check_stock("SingleItem")
    assert has_stock, "'SingleItem' should be in stock when 1 item is added"