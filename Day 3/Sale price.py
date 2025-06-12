"""Sale price"""
def get_regular_price():
    """get_regular_price"""
    price = float(input())
    return price

def discount(price):
    """discount"""
    total = price * 0.8
    return total

a = discount(get_regular_price())
print(f"The sale price is ${a:.2f}")
