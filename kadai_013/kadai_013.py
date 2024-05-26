def calculate_total(price: int, tax_rate: float) -> int:
    total_price = price * (1 + tax_rate)

    print(f"{total_price}円")
    

calculate_total(3000, 0.1)
