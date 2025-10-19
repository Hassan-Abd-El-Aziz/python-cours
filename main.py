class Food:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def eate(self):
        print(f"your food is {self.name} and the price is {self.price}")

class Apple(Food):
    def __init__(self,name,price,amount):
        super().__init__(name,price)
        self.amount=amount
    def say(self):
        print(f"{self.name} - {self.price} - {self.amount}")


food_one=Food("pizza",150)
food_one.eate()

apple=Apple("onion",50,500)
apple.say()
apple.eate()