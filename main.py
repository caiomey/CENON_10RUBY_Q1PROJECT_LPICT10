# main.py

# Restaurant info
restaurant_name = "Twirl and Toss"
owner = "Caiomey Cenon"
location = "Paranaque Village, Paranaque City"
contact_numbers = ["(+63) 960 122 4567", "(+63) 123 456 7891"]
email = "twirlandtoss@gmail.com"

# Menu items and prices
menu = {
    "Carbonara": 120,
    "Garlic Bread": 70,
    "Caesar Salad": 150,
    "Iced Tea": 30,
    "Pancakes": 120,
    "Rice with Chicken": 140
}

def show_menu():
    print(f"🍽️ Welcome to {restaurant_name} Menu:")
    for item, price in menu.items():
        print(f"- {item}: ₱{price}")

