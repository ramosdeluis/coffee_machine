def menu(machine):
    while True:
        decision = input(f'Hello! What would you like? (espresso/latte/cappuccino): ').lower().strip()

        if decision in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
            if decision == 'espresso' or decision == 'latte' or decision == 'cappuccino':
                deposited_money, coins_dict = get_money(machine)
                print(machine.show('coins'))
                if checking(decision, MENU, machine, deposited_money):
                    get_drink(decision, MENU, machine)
                    give_change(decision, MENU, machine, deposited_money, coins_dict)
                    machine.sum_money()
                    print(machine.show('coins'))
                    print(f"Here's yours {decision.title()}. Thanks for the purchase!")
                else:
                    give_change(decision, MENU, machine, deposited_money, coins_dict)

            if decision == 'report':
                print(f'-=-=-=-=-=-=-=-\n'
                      f'Water: {machine.water} ml\n'
                      f'Milk: {machine.milk} ml\n'
                      f'Coffee: {machine.coffee} g\n'
                      f'Money: $ {machine.money:.2f}\n'
                      f'-=-=-=-=-=-=-=-\n')
            if decision == 'off':
                print('Shutting down the machine...')
                return False
        else:
            print('Sorry, this is not a valid option.')


def give_change(decision, dic, machine, deposited_money, coins_dict):
    global remove_dict
    cost = dic[decision]['cost']
    if cost > deposited_money:
        for coin, value in coins_dict.items():
            machine.coins[coin] -= value
        return print(f'Here is yours $ {deposited_money:.2f} back. Try again.')
    if deposited_money == cost:
        return print('Thank you for the purchase!')
    if cost < deposited_money:
        remove_dict = {'quarters': 0, 'dimes': 0, 'nickles': 0, 'pennies': 0}
        thing = deposited_money - cost
        while thing - 0.25 > 0 and machine.coins['quarters'] - remove_dict['quarters'] > 0:
            remove_dict['quarters'] += 1
            thing -= 0.25
        while thing - 0.1 > 0 and machine.coins['dimes'] - remove_dict['dimes'] > 0:
            remove_dict['dimes'] += 1
            thing -= 0.1
        while thing - 0.05 > 0 and machine.coins['nickles'] - remove_dict['nickles'] > 0:
            remove_dict['nickles'] += 1
            thing -= 0.05
        while thing - 0.01 > (-0.01) and machine.coins['pennies'] - remove_dict['pennies'] > 0:
            remove_dict['pennies'] += 1
            thing -= 0.01
        remove_money(machine, remove_dict)
        print(f'Your change are $ {deposited_money - cost:.2f}')


def remove_money(machine, coins_dict):
    machine.coins['quarters'] -= coins_dict['quarters']
    machine.coins['dimes'] -= coins_dict['dimes']
    machine.coins['nickles'] -= coins_dict['nickles']
    machine.coins['pennies'] -= coins_dict['pennies']


def insert_money(machine, coins_dict):
    machine.coins['quarters'] += coins_dict['quarters']
    machine.coins['dimes'] += coins_dict['dimes']
    machine.coins['nickles'] += coins_dict['nickles']
    machine.coins['pennies'] += coins_dict['pennies']


def get_money(machine):
    print('Now, deposit your coins!')
    quarters = int(input(f'How many quarters? '))
    dimes = int(input(f'How many dimes? '))
    nickles = int(input(f'How many nickles? '))
    pennies = int(input(f'How many pennies? '))
    coins_dict = {'quarters': quarters, 'dimes': dimes, 'nickles': nickles, 'pennies': pennies}
    deposited_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    insert_money(machine, coins_dict)
    return deposited_money, coins_dict


def get_drink(decision, dic, machine):
    ingredients = dic[decision]['ingredients']
    for ingredient in ingredients.keys():
        machine.change(ingredient, ingredients[ingredient], 'remove')


def checking(decision, dic, machine, deposited_money):
    ingredients = dic[decision]['ingredients']
    cost = dic[decision]['cost']
    cont = 0
    for ingredient, quantity in ingredients.items():
        if machine.show(ingredient) < quantity:
            cont += 1

    if cont != 0:
        print(f"I am sorry. I can not do {decision.title()} now. Try another option.")
        return False
    else:
        if cost <= deposited_money:
            return True
        else:
            print(f'I am sorry. You deposited $ {deposited_money:.2f}, but the {decision.title()} cost $ {cost:.2f}.')
            print(machine.show('coins'))
            return False


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
