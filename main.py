import store
import products

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


def start():
    """
    Displays the store menu and prompts the user for a choice.

    Returns:
        str: The user's menu selection.
    """
    while True:
        print("\nSTORE MENU")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_choice = input("Please choose a number: ").strip()
        return user_choice


def list_all_products(best_buy):
    """
    Lists and prints all active products in the store.

    Args:
        best_buy (Store): The store instance containing products.
    """
    product_list = best_buy.get_all_products()
    print("\nALL PRODUCTS IN STORE")
    print("----------")
    for index, product in enumerate(product_list):
        print(f"{index + 1}. {product.show()}")


def show_total_amount(best_buy):
    """
    Displays the total quantity of all active products in the store.

    Args:
        best_buy (Store): The store instance containing products.
    """
    total_amount = best_buy.get_total_quantity()
    print("\nTOTAL AMOUNT IN STORE")
    print("----------")
    print(f"Total of {total_amount} items in store.")


def make_order(best_buy):
    """
    Handles the process of making a purchase order from the store.

    Args:
        best_buy (Store): The store instance used to process the order.
    """
    list_all_products(best_buy)
    product_list = best_buy.get_all_products()
    shopping_list = []
    while True:
        print("----------")
        print("When you want to finish order, enter empty text.")
        user_input = input("Which product # do you want? ").strip()
        if user_input == "":
            if not shopping_list:
                print(f"{RED}No products selected. Returning to main menu...{RESET}")
            else:
                total = best_buy.order(shopping_list)
                print(f"{GREEN}ORDER MADE! TOTAL PAYMENT: {total}€ {RESET}")
            break
        try:
            user_choice_product = int(user_input)
        except:
            print(f"{RED}Type in valid number: 1 - {len(product_list) + 1}{RESET}")
            continue
        if not 1 <= user_choice_product <= len(product_list):
            print(f"{RED}Please enter a number between 1 and {len(product_list)}.{RESET}")
            continue

        index = user_choice_product - 1
        selected_product = product_list[index]
        try:
            user_choice_amount = int(input("What amount do you want? ").strip())
        except:
            print(f"{RED}Type in valid number: 1 - {selected_product.get_quantity()}{RESET}")
            continue
        if user_choice_amount > selected_product.get_quantity():
            print(f"{RED}Type in valid amount. Only {selected_product.get_quantity()} left in stock{RESET}")
            continue
        if user_choice_amount == "":
            break
        shopping_list.append((selected_product, user_choice_amount))
        print("******")
        print(f"{GREEN}PRODUCTS IN YOUR SHOPPING BASKET:{RESET}")
        for product, amount in shopping_list:
            print(f"{GREEN}- {product}, AMOUNT: {amount}{RESET}")
    print("******")



def quit():
    """
    Prints exit message and terminates the program.
    """
    print("**** YOU LEFT THE SHOP - END OF PROGRAM **** ")
    exit()


def main():
    """
    Main driver of the program. Initializes products and store, and runs the menu loop.
    """
    # 1. Create the product inventory (Product instances)
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    # 2. Create the store with the product inventory
    best_buy = store.Store(product_list)

    # 3. Menu loop
    while True:
        user_choice = start()
        print("----------")

        options = {
            "1": lambda: list_all_products(best_buy),
            "2": lambda: show_total_amount(best_buy),
            "3": lambda: make_order(best_buy),
            "4": lambda: quit()
        }

        action = options.get(user_choice)
        if action:
            action()
        else:
            keys = [int(k) for k in options.keys()]
            print(f"{RED}Invalid choice. Please enter a number between {min(keys)} and {max(keys)}.{RESET}")


if __name__ == "__main__":
    main()

