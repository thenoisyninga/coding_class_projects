products = {
    'bronze ring': 1.00,
    'gold ring': 20.00,
}

class Customer:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__balance = 0

    def buy(self, name_of_product):
        cost = products[name_of_product]
        if cost <= self.__balance:
            self.__balance = self.__balance - cost
            print(f"Purchase Successful: {name_of_product} bought for {cost} dollars.")
        else:
            print(f"Purchase Unsuccessful: {name_of_product} is too expensive.")

    def add_balance(self, amount_to_add):
        self.__balance = self.__balance + amount_to_add

a_customer = Customer(
    name= 'John',
    age='34'
)

a_customer.add_balance(100)
a_customer.buy('bronze ring')