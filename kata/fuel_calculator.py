def fuel_price(litres, price_per_litre):
    if litres < 1:
        raise Exception("Enter 1 or more litres")

    price_per_litre_in_cents = price_per_litre * 100
    discount_in_cents = round((litres / 2)) * 5
    print(discount_in_cents)

    if discount_in_cents > 25:
        discount_in_cents = 25

    total_cost = ((litres * price_per_litre_in_cents) - (discount_in_cents * litres)) / 100.0

    return total_cost

print(fuel_price(7, 35))