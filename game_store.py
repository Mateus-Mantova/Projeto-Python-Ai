# Online Game Store
import math

games = {
    1: {"name": "Minecraft", "price": 99.90},
    2: {"name": "Grand Theft Auto V", "price": 89.90},
    3: {"name": "The Witcher 3", "price": 79.90},
    4: {"name": "Stardew Valley", "price": 24.90},
    5: {"name": "Hollow Knight", "price": 46.90},
    6: {"name": "Terraria", "price": 19.90},
    7: {"name": "Celeste", "price": 36.99},
    8: {"name": "Hades", "price": 73.99},
    9: {"name": "Red Dead Redemption 2", "price": 249.90},
    10: {"name": "Cyberpunk 2077", "price": 199.90},
    11: {"name": "Elden Ring", "price": 229.90},
    12: {"name": "Portal 2", "price": 21.99},
    13: {"name": "Undertale", "price": 20.99},
    14: {"name": "Cuphead", "price": 54.99},
    15: {"name": "Among Us", "price": 9.99}
}

cart = []


def show_games(page):
    game_list = list(games.items())
    total_pages = math.ceil(len(game_list) / 5)

    start = (page - 1) * 5
    end = start + 5

    print(f"\n===== AVAILABLE GAMES (Page {page}/{total_pages}) =====")

    for game_id, game in game_list[start:end]:
        print(f"{game_id} - {game['name']} - R$ {game['price']:.2f}")

    return total_pages

def add_to_cart():
    page = 1

    while True:
        total_pages = show_games(page)

        print("\n[N] Next page | [P] Previous page | [0] Finish")
        choice = input("Enter a game ID or an option: ").strip().lower()

        if choice == "0":
            break
        elif choice == "n":
            if page < total_pages:
                page += 1
            else:
                print("You are already on the last page.")
        elif choice == "p":
            if page > 1:
                page -= 1
            else:
                print("You are already on the first page.")
        elif choice.isdigit() and int(choice) in games:
            game_id = int(choice)
            if games[game_id] in cart:
                print(f"{games[game_id]['name']} is already in your cart.")
            else:
                cart.append(games[game_id])
                print(f"{games[game_id]['name']} added to your cart!")
        else:
            print("Invalid option or game not found.")

def remove_from_cart():
    if len(cart) == 0:
        print("\nYour cart is empty. Nothing to remove.")
        return

    show_cart()

    while True:
        choice = input("\nEnter the number of the item to remove (0 to cancel): ").strip()

        if choice == "0":
            print("No item removed.")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(cart):
            removed = cart.pop(int(choice) - 1)
            print(f"{removed['name']} removed from your cart.")
            break
        else:
            print("Invalid item number.")

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
    print("3 - Remove game from cart")
    print("4 - Checkout")
    print("5 - Exit")

    option = input("\nChoose an option: ")

    if option == "1":
        add_to_cart()

    elif option == "2":
        show_cart()

    elif option == "3":

        remove_from_cart()

    elif option == "4":

        checkout()

    elif option == "5":

        print("Thank you for visiting the store!")

        break
    else:
        print("Invalid option.")