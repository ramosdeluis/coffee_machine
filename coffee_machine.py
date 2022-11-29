

class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 4.1
        self.coins = {'quarters': 10,
                      'dimes': 10,
                      'nickles': 10,
                      'pennies': 10}

    def show(self, what) -> float:
        if what == "water":
            return self.water
        if what == "milk":
            return self.milk
        if what == "coffee":
            return self.coffee
        if what == "money":
            return self.money
        if what == 'coins':
            return self.coins

    def change(self, what, quantity, to_do='remove'):
        if what == "water":
            if to_do == 'remove':
                self.water -= quantity
            else:
                self.water += quantity
        if what == "milk":
            if to_do == 'remove':
                self.milk -= quantity
            else:
                self.milk += quantity
        if what == "coffee":
            if to_do == 'remove':
                self.coffee -= quantity
            else:
                self.coffee += quantity
        if what == "money":
            if to_do == 'remove':
                self.money -= quantity
            else:
                self.money += quantity

    def sum_money(self):
        self.money = self.coins['quarters']*0.25 + self.coins['dimes']*0.1 + self.coins['nickles']*0.05 + self.coins['pennies']*0.01

