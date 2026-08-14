"""
CHALLENGE: Build an Order Class
DIFFICULTY: Intermediate
FOLDER: 01-cafe-pos / tier3_intermediate

STORY
-----
The café wants each customer's order to be its own self-contained "thing"
in the code, with its own list of items and its own total — that's exactly
what a class is for.

YOUR TASK
---------
Complete the `Order` class below by implementing each method described in
its docstring. Then test it using the code at the bottom of the file.

EXAMPLE OUTPUT (from the test code at the bottom)
--------------------------------------------------
Added Coffee to the order.
Added Muffin to the order.
Added Tea to the order.
Removed Tea from the order.
Current order: ['Coffee', 'Muffin']
Order total: $9.5
"""

MENU = {
    "Coffee": 4.50,
    "Tea": 3.50,
    "Muffin": 5.00,
    "Toastie": 6.50,
    "Hot Chocolate": 4.00,
}


class Order:
    """Represents one customer's order at The Trendiest Café."""

    def __init__(self):
        """Set up an empty order. Hint: you'll need a list to store item names."""
        # TODO: create self.items as an empty list
        self.items = []
        pass

    def add_item(self, item_name):
        """
        Add item_name to this order if it exists on the MENU.
        Print "Added {item_name} to the order." if successful.
        Print "Sorry, {item_name} is not on the menu." if it isn't a valid item.
        """
        if item_name not in MENU:
            print(f"Sorry, {item_name} is not on the menu")
            pass
        else:
            print(f"Added {item_name} to the order!")
            self.items.append(item_name)
        # TODO: implement this method
        pass

    def remove_item(self, item_name):
        """
        Remove ONE occurrence of item_name from this order, if present.
        Print "Removed {item_name} from the order." if successful.
        Print "{item_name} isn't in this order." if it wasn't there.
        """
        # TODO: implement this method
        if item_name not in self.items:
            print(f"this {item_name} isn't in your order")
        else:
            print(f"happy birthday {item_name}")
            self.items.remove(item_name)
        pass

    def get_total(self):
        """Return the total price of everything currently in self.items."""
        # TODO: implement this method
        final_price = 0
        for item in self.items:
            final_price += MENU[item]
        return final_price



if __name__ == "__main__":
    my_order = Order()
    my_order.add_item("Coffee")
    my_order.add_item("Muffin")
    my_order.add_item("Tea")
    my_order.remove_item("Tea")

    print(f"Current order: {my_order.items}")
    print(f"Order total: ${my_order.get_total()}")
