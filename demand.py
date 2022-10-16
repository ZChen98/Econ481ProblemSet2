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
    elif elasticity < 1:
        return 'Inelastic'
    else:
        return 'Unit-Elastic'

def compute_demand(sales:float, init_price:float, new_price:float, elasticity:float) -> float:
    """Compute the predicted demand at the new price
    
    Parameters
    ==========
    sales:
    init_price:
    new_price:
    elasticity:

    Returns
    =======

    """
    pass