def calculate_total(price: int, tax_rate: float) -> int:
    total_price = price * (1 + tax_rate)
    return total_price
    

print(f"{calculate_total(3000, 0.1)}円")
