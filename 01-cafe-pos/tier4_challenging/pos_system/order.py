"""
CHALLENGE PART 2 of 4: The Order

See menu.py for an overview of this whole project. Complete menu.py first,
since this file needs it.

YOUR TASK (this file)
----------------------
Build an Order class that stores items WITH QUANTITIES (this is harder
than the tier3 Order class, which only stored a plain list). For example,
if a customer orders 2 coffees and 1 muffin, self.items should end up
looking something like: {"Coffee": 2, "Muffin": 1}
"""

from menu import Menu


class Order:
    """Represents one customer's order, including quantities."""

    def __init__(self, menu: Menu):
        """
        Store the given menu so this order can check prices, and set up
        an empty dictionary (self.items) to hold {item_name: quantity}.
        """
        self.menu = menu
        self.items = {}

    def add_item(self, item_name, quantity=1):
        """
        Add `quantity` of item_name to the order.
        - If the item isn't on the menu, print a message and don't add it.
        - If the item is already in the order, increase its quantity.
        - Otherwise, add it as a new entry.
        """
        # TODO: implement this method
        if item_name in self.menu.items:
            if item_name in self.items:
                self.items[item_name] += quantity
            self.items[item_name] = quantity
        else:
            print("i am not falling for this -papyrus")

    def remove_item(self, item_name, quantity=1):
        """
        Remove `quantity` of item_name from the order.
        - If removing would take the quantity to 0 or below, remove the
          item entirely.
        - If the item isn't in the order, print a message saying so.
        """
        # TODO: implement this method
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        pass

    def get_subtotal(self):
        """
        Return the total price of everything in the order BEFORE tax,
        taking quantities into account (price * quantity for each item).
        """
        # TODO: implement this method
        pass


if __name__ == "__main__":
    menu = Menu()
    order = Order(menu)
    order.add_item("Coffee", 2)
    order.add_item("Muffin", 1)
    print("Order items:", order.items)
    print("Subtotal:", order.get_subtotal())
