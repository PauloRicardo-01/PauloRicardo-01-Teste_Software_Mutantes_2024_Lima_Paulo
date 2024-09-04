import pytest

from src.discount_processor import calculate_final_price, get_currency_symbol


@pytest.mark.parametrize(
    "base_price, discount_percentage, tax_rate, expected",
    [
        (100, 0, 0, 100),  # Caso trivial
        (100, 10, 0.1, 99),  # Caso estándar
        (100, 0, 0.1, 110),  # Sin descuento
        (100, 10, 0, 90),  # Sin impuestos
    ],
)
def test_calculate_final_price(base_price, discount_percentage, tax_rate, expected):
    assert (
        calculate_final_price(base_price, discount_percentage, tax_rate) == expected
    ), "Calcula el precio final correcto"


# Verifica que se lance una excepción para un porcentaje de descuento inválido
@pytest.mark.parametrize("discount_percentage", [-1, 101])
def test_invalid_discount_percentage_raises_error(discount_percentage):
    with pytest.raises(ValueError):
        calculate_final_price(100, discount_percentage, 0.1)


# Verifica que se lance una excepción para una tasa de impuesto negativa
def test_negative_tax_rate_raises_error():
    with pytest.raises(ValueError):
        calculate_final_price(100, 10, -0.1)

def test_get_currency_symbol():
    assert get_currency_symbol() == "USD$"

## Testes adicionais

def test_discount_percentage_of_exactly_100_is_valid():
    final_price = calculate_final_price(100, 100, 0.1)
    expected_price = 0  
    assert final_price == expected_price, "A 100% discount should reduce the price to 0 before tax"

def test_invalid_discount_percentage_error_message():
    with pytest.raises(ValueError) as exc_info:
        calculate_final_price(100, 101, 0.1)
    assert str(exc_info.value) == "Discount percentage must be between 0 and 100"

def test_negative_tax_rate_error_message():
    with pytest.raises(ValueError) as exc_info:
        calculate_final_price(100, 10, -0.1)
    assert str(exc_info.value) == "Tax rate must be positive"

def test_rounding_to_two_decimals():
    assert calculate_final_price(100, 10, 0.12345) == 101.11
