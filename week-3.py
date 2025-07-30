def calculate_discount(price: float, discount_percent: float) -> float:
    """
        The function should take the original price (price) and the discount 
        percentage (discount_percent) as parameters. If the discount is 20% or higher, 
        apply the discount; otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price
    
# Usage de la fonction
price = float(input("Entrez le prix original: "))
discount_percent = float(input("Entrez le pourcentage de réduction: "))
final_price = calculate_discount(price, discount_percent)
print(f"Le prix final après réduction est: {final_price}")