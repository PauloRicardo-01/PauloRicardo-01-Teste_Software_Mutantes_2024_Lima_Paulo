def calculate_final_price(base_price, discount_percentage, tax_rate):
    """Calculate the final price after applying discount and tax."""
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    if tax_rate < 0:
        raise ValueError("Tax rate must be positive")

    discount_amount = base_price * (discount_percentage / 100)
    discounted_price = base_price - discount_amount
    tax_amount = discounted_price * tax_rate
    final_price = discounted_price + tax_amount

    return round(final_price, 2)


def get_currency_symbol():
    return "USD$"  # Probar pragma: no mutate
