# Facade is a structural design pattern. It provides a simplified interface to a complex system of classes,
# library or framework
# hides some of the actual interface


# complex subsystem 1:
class Inventory:
    def checkStock(self, itemId, quantity):
        return True

    def reduceStock(self, itemId, quantity):
        print(f"Reduced {quantity} unit of item {itemId} from the inventory...")


# complex subsystem 2:
class Payment:
    def processPayment(self, amount):
        print(f"Payment of {amount}$ processed successfully !!!")


# complex subsystem 3:
class Shipping:
    def shipOrder(self, address):
        print(f"Order shipped to {address}")

    def returnOrder(self, pickupAddress):
        print(f"")


# FACADE
class OrderFacade:
    def __init__(self) -> None:
        self.inventory = Inventory()
        self.payment = Payment()
        self.shipping = Shipping()

    def placeOrder(self, itemId, quantity, amount, address):
        if self.inventory.checkStock(itemId, quantity):
            self.inventory.reduceStock(itemId, quantity)

            self.payment.processPayment(amount)
            self.shipping.shipOrder(address)

        else:
            print("Sorry the item is out of stock!!!")


if __name__ == "__main__":
    orderFacade = OrderFacade()
    itemId = "1234"
    quantity = 2
    amount = 50
    address = "PTC Thoraipakkam"
    print("Placing order ....")
    orderFacade.placeOrder(itemId, quantity, amount, address)
