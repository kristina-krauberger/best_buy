
class Product:
    """
    Represents a product in the store with name, price, quantity, and active status.
    Attributes:
        name (str): The name of the product.
        price (float): The unit price of the product.
        quantity (int): The available quantity in stock.
        active (bool): Indicates whether the product is currently active.
    """


    def __init__(self, name, price, quantity):
        """
        Initializes a new Product instance with name, price, and quantity.
        Args:
            name (str): The name of the product.
            price (float): The price per unit.
            quantity (int): The amount of stock available.

        Raises:
            TypeError: If name is not a string, or if price/quantity are not numeric.
            ValueError: If name is empty or if price/quantity are non-positive.
        """
        if not isinstance(name, str):
            raise TypeError("Expected name is string.")
        if name.strip() == "":
            raise ValueError("Name is was empty, type in name.")
        if not isinstance(price, (float, int)):
            raise TypeError("Expected price is Integer or Float.")
        if price <= 0:
            raise ValueError("Price needs to be a positive number.")
        if not isinstance(quantity, int):
            raise TypeError("Expected quantity is Integer or Float.")
        if quantity <= 0:
            raise ValueError("Quantity needs to be a positive number.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """
        Returns the current quantity in stock.
        Returns:
            int: The quantity of the product.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Sets a new quantity for the product. Deactivates the product if quantity is 0.
        Args:
            quantity (int): The new quantity to set.
        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity needs to be a positive number.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()


    def is_active(self):
        """
        Checks if the product is currently active.
        Returns:
            bool: True if active, False otherwise.
        """
        return self.active


    def activate(self):
        """
        Activates the product (sets active to True).
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product (sets active to False).
        """
        self.active = False


    def show(self):
        """
        Prints the product details in a human-readable format.
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """
        Processes a purchase of the product.
        Args:
            quantity (int): The number of units to buy.
        Returns:
            Float: The total cost for the purchase.
        Raises:
            ValueError: If the quantity is invalid or exceeds available stock.
            TypeError: If the product is not active or if quantity is not an integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity needs to be a positive number.")
        if not isinstance(quantity, int):
            raise TypeError("Expected number.")
        if quantity > self.get_quantity():
            raise ValueError("Quantity is bigger than the available amount.")
        if not self.is_active():
            raise TypeError("Item is not available at the moment.")
        total = quantity * self.price
        self.set_quantity(self.get_quantity() - quantity)
        return round(total, 2)


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()


