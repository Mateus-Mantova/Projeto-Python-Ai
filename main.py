# Online Game Store

games = {
    1: {"name": "Minecraft", "price": 99.90},
    2: {"name": "Grand Theft Auto V", "price": 89.90},
    3: {"name": "The Witcher 3", "price": 79.90},
    4: {"name": "Stardew Valley", "price": 24.90},
    5: {"name": "Hollow Knight", "price": 46.90}
}

cart = []


def show_games():
    print("\n===== AVAILABLE GAMES =====")

    for game_id, game in games.items():
        print(f"{game_id} - {game['name']} - R$ {game['price']:.2f}")


def add_to_cart():
    show_games()

    while True:
        try:
            game_id = int(input("\nEnter the ID of the game you want to buy (0 to finish): "))

            if game_id == 0:
                break

            if game_id in games:
                cart.append(games[game_id])
                print(f"{games[game_id]['name']} added to your cart!")
            else:
                print("Game not found.")

        except ValueError:
            print("Please enter a valid number.")

def calculate_total():
    total = 0
    for game in cart:
        total += game["price"]
    return total


def calculate_discount(total):
    if total >= 200:
        rate = 0.20
    elif total >= 100:
        rate = 0.10
    else:
        rate = 0.0
    return rate

def show_cart():
    if len(cart) == 0:
        print("\nYour cart is empty.")
        return

    print("\n===== YOUR CART =====")

    for i, game in enumerate(cart, 1):
        print(f"{i} - {game['name']} - R$ {game['price']:.2f}")

    subtotal = calculate_total()
    discount_rate = calculate_discount(subtotal)
    discount_value = subtotal * discount_rate
    final_total = subtotal - discount_value

    print(f"\nSubtotal: R$ {subtotal:.2f}")
    print(f"Discount ({discount_rate * 100:.0f}%): -R$ {discount_value:.2f}")
    print(f"Total: R$ {final_total:.2f}")

def checkout():
    if len(cart) == 0:
        print("\nYour cart is empty. Add some games first.")
        return

    show_cart()

    answer = input("\nDo you want to complete the purchase? (y/n): ")

    if answer.strip().lower() == "y":
        print("\n===== PURCHASE COMPLETED =====")
        print("Thank you for your purchase!")

        for game in cart:
            print(f"- {game['name']}")

        cart.clear()

    else:
        print("Purchase cancelled.")


# Main program
while True:
    print("\n==============================")
    print("       ONLINE GAME STORE")
    print("==============================")
    print("1 - Buy games")
    print("2 - View cart")
    print("3 - Checkout")
    print("4 - Exit")

    option = input("\nChoose an option: ")

    if option == "1":
        add_to_cart()

    elif option == "2":
        show_cart()

    elif option == "3":
        checkout()

    elif option == "4":
        print("Thank you for visiting the store!")
        break

    else:
        print("Invalid option.")