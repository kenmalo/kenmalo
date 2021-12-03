class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        customer = " "
        flavor = " "
        scoops = 0
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops
        order = {"customer": customer, "flavor": flavor, "scoops": self.scoops}

        if self.flavor in self.flavors and 1 <= self.scoops <= 3:
            print("Order created")
            self.orders.enqueue(order)
        if self.flavor not in self.flavor:
            print("Unfortunately, we do not have that flavor")
        else:
            print("Make a selection between 1 to 3")

    def show_all_orders(self):
        print("All pending Ice cream orders:")
