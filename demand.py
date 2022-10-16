"""
Justin Chen
Problem Set 2: Demand Exercise
"""
import math

def compute_elasticity(price1:float, price2:float, quant1:float, quant2:float) -> float:
    """Compute the elasticity

    Parameters
    ==========
    price1: float; the first numeric price of the good
    price2: float; the second numeric price of the good
    quant1: float; the first numeric quantity of the good
    quant2: float; the second numeric quantity of the good

    Returns
    =======
    Elasticity
    """
    elasticity = math.log(quant2 / quant1, math.e) / math.log(price2 / price1, math.e)
    return elasticity

def check_elasticity(elasticity:float) -> str:
    """Return one of 'Elastic' | 'Inelastic' | Unit-Elastic'

    Parameters
    ==========
    elasticity: float; the numeric elasticity of a good

    Returns
    =======
    String of whether an elasticity is elastic, inelastic, or unit-elastic
    """
    if elasticity > 1:
        return 'Elastic'
    if elasticity < 1:
        return 'Inelastic'
    return 'Unit-Elastic'

def compute_demand(sales:float, init_price:float, new_price:float, elasticity:float) -> float:
    """Compute the predicted demand at the new price

    Parameters
    ==========
    sales: float; the numeric sales of the good
    init_price: float; the numeric initial price
    new_price: float; the numeric new price
    elasticity: float; the numeric elasticity of the good

    Returns
    =======
    Predicted demand at the new price
    """
    predicted_demand = 0.0
    predicted_demand = elasticity * sales * (new_price / init_price)
    return predicted_demand

def main():
    """Main function to ask the user whether to calculate either
    elasticity or demand
    """
    user_input = str(input('Would you like calculate elasticity or demand? ')).lower()
    if user_input == 'elasticity':
        old_price = float(input('Please enter the old price: '))
        new_price = float(input('Please enter the new price: '))
        old_quantity = float(input('Please enter the old quantity: '))
        new_quantity = float(input('Please enter the new quantity: '))
        elasticity = compute_elasticity(old_price, new_price, old_quantity, new_quantity)

        print(elasticity)
        print(f'The good is {check_elasticity(elasticity)}.')
    else:
        sales = float(input('Please enter the sales quantity: '))
        init_price = float(input('Please enter the initial price: '))
        elasticity = float(input('Please enter the elasticity: '))
        price_points = int(input('Please enter the number of new price points: '))
        demand_dict = {}

        while price_points > 0:
            new_price = float(input('Please enter the new price point: '))
            demand_dict[new_price] = round(compute_demand(sales, init_price, new_price, elasticity), 2)
            price_points -= 1

        print(demand_dict)

if __name__=="__main__":
    main()
