'''Instructions
You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.
You have five tasks, all related to cooking your recipe.

Task 1
Define expected bake time in minutes
Define an EXPECTED_BAKE_TIME constant that returns how many minutes the lasagna should bake in the oven. According to your cookbook, the Lasagna should be in the oven for 40 minutes:

Task 2
Calculate remaining bake time in minutes
Implement the bake_time_remaining() function that takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME.

Task 3
Calculate preparation time in minutes
Implement the preparation_time_in_minutes(number_of_layers) function that takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.

Task 4
Calculate total elapsed cooking time (prep + bake) in minutes
Implement the elapsed_time_in_minutes(number_of_layers, elapsed_bake_time) function that has two parameters: number_of_layers (the number of layers added to the lasagna) and elapsed_bake_time (the number of minutes the lasagna has been baking in the oven). This function should return the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.

Task 5
Update the recipe with notes
Go back through the recipe, adding "notes" in the form of function docstrings.

'''
def exchange_money(budget, exchange_rate):
    """
 
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget/exchange_rate
    
def get_change(budget, exchanging_value):
    """
 
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget-exchanging_value
def get_value_of_bills(denomination, number_of_bills):
    """
 
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return denomination*number_of_bills
def get_number_of_bills(budget, denomination):
    """
 
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget/denomination)
def get_leftover_of_bills(budget, denomination):
    """
 
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    return budget%denomination
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
 
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_decimal=spread/100
    new_exchange_rate=exchange_rate+(exchange_rate*spread_decimal)
    max_value=budget/new_exchange_rate
    return int(max_value/denomination)*denomination
