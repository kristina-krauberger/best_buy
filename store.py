import products


class Store:
    """
    Represents a store that holds and manages a list of products.

    Provides functionality to add, remove, list, and order products.
    """

    def __init__(self, list_products):
        """
        Initializes the Store with a list of Product instances.

        Args:
            list_products (list): A list of Product instances.

        Raises:
            TypeError: If list_products is not a list of Product instances.
        """
        if not isinstance(list_products, list):
            raise TypeError("Expected a list of Product instances.")
        for product in list_products:
            if not isinstance(product, products.Product):
                raise TypeError("All items must be instances of Product.")
        self.list_products = list_products


    def add_product(self, product):
        """
        Adds a Product instance to the store.

        Args:
            product (Product): The product to be added.

        Raises:
            TypeError: If the provided object is not a Product instance.
        """
        if not isinstance(product, products.Product):
            raise TypeError("Only Product instances can be added to the store.")
        self.list_products.append(product)


    def remove_product(self, product):
        """
        Removes a Product instance from the store.

        Args:
            product (Product): The product to be removed.

        Raises:
            TypeError: If the provided object is not a Product instance.
            ValueError: If the product is not in the store.
        """
        if not isinstance(product, products.Product):
            raise TypeError("Only Product instances can be removed from the store.")
        if product in self.list_products:
            self.list_products.remove(product)
        else:
            raise ValueError(f"Product '{product}' is not in store.")


    def get_total_quantity(self):
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: The sum of all product quantities.
        """
        counter = 0
        for product in self.list_products:
            counter += product.get_quantity()
        return counter


    def get_all_products(self):
        """
        Retrieves all active products in the store.

        Returns:
            list: A list of active Product instances.
        """
        active_products = []
        for product in self.list_products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """
        Processes a list of product purchase orders.

        Args:
            shopping_list (list): A list of tuples, each containing a Product instance
            and quantity to purchase.

        Returns:
            float: The total price for all valid purchases.

        Raises:
            TypeError: If the elements in the tuple are not a Product instance and an integer.
        """
        total_price = 0
        for product, amount in shopping_list:
            if not isinstance(product, products.Product):
                raise TypeError("First element in shopping list tuple must be a Product.")
            if not isinstance(amount, int):
                raise TypeError("Second element in shopping list tuple must be an integer.")
            if product.is_active():
                total_price += product.buy(amount)
        return round(total_price, 2)


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    available_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(available_products[0], 1), (available_products[1], 2)]))


if __name__ == "__main__":
    main()