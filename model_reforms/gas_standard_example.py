# -*- coding: utf-8 -*-

# Here we construct a very standard exemple to study the tax incidence on one consumer
# consuming 1000€ of natural gas per year, and not driving a car.

from __future__ import division


from define_tax_incidence import *


def natural_gas_example(expenditures):
    
    dict_gas = dict()
    vat = 0.2
    e_housing = -0.2
    i = 0.8
    
    current_price = 0.0651 # This is the value of natural gas unitary prices
    
    fixed_price_contract = 150
    
    old_carbon_tax = 44.6 # Carbon tax in 2018
    new_carbon_tax = 44.6 + 50 # Carbon tax that we simulate
    carbon_intensity = 0.000181
    
    initial_excise_tax = 0.0003
    
    # Compute tax rates :
    new_carbon_tax = carbon_tax(new_carbon_tax, carbon_intensity)
    old_carbon_tax = carbon_tax(old_carbon_tax, carbon_intensity)
    
    new_excise_tax = excise_tax(new_carbon_tax, initial_excise_tax)
    old_excise_tax = excise_tax(old_carbon_tax, initial_excise_tax)
    
    
    # Compute prices :
    new_final_price = final_price_adjusted(current_price, i, new_excise_tax, old_excise_tax)
    final_price_variation = variation_final_price(i, current_price, new_excise_tax, old_excise_tax)
    
    current_price_without_tax = price_without_tax(current_price, old_excise_tax)
    new_price_without_tax = price_without_tax(new_final_price, new_excise_tax)
    
    
    # Compute quantities :
    current_quantity = quantity(current_price, expenditures - fixed_price_contract)
    new_quantity = adjusted_quantity(current_quantity, e_housing, final_price_variation)
    
    
    # Compute expenditures :
    new_expenditures = adjusted_expenditures(expenditures - fixed_price_contract, e_housing, final_price_variation) + fixed_price_contract
    variation_expenditures = new_expenditures - expenditures
    
    
    # Compute taxes paid :
    current_taxes = taxes(current_price_without_tax, current_quantity, old_excise_tax)
    new_taxes = taxes(new_price_without_tax, new_quantity, new_excise_tax)

    dict_gas['new_expenditures'] = new_expenditures
    dict_gas['variation_expenditures'] = variation_expenditures
    dict_gas['new_quantity'] = new_quantity
    dict_gas['current_quantity'] = current_quantity
    dict_gas['current_taxes'] = current_taxes
    dict_gas['new_taxes'] = new_taxes

    return dict_gas


if __name__ == "__main__":
    expenditures = 1000
    example = natural_gas_example(expenditures)
