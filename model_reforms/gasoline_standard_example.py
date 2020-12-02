# -*- coding: utf-8 -*-

# Here we construct a very standard exemple to study the tax incidence on one consumer
# consuming 1000€ of gasoline per year, and using electricity only in housing.

from __future__ import division


from define_tax_incidence import *


def gasoline_example(expenditures):

    dict_gasoline = dict()
    vat = 0.2
    e_transports = -0.4
    i = 0.8
    
    current_price = 1.441 # This is the value of gasoline prices
        
    old_carbon_tax = 44.6 # Carbon tax in 2018
    new_carbon_tax = 44.6 + 50 # Carbon tax that we simulate
    carbon_intensity = 0.002286 # Carbon content of gasoline (deduced from art 265 code des douanes)
    
    initial_excise_tax = 0.6069 - 0.026 # This is the value of the TICPE without carbon tax
    
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
    current_quantity = quantity(current_price, expenditures)
    new_quantity = adjusted_quantity(current_quantity, e_transports, final_price_variation)
    
    
    # Compute expenditures :
    new_expenditures = adjusted_expenditures(expenditures, e_transports, final_price_variation)
    variation_expenditures = new_expenditures - expenditures
    
    
    # Compute taxes paid :
    current_taxes = taxes(current_price_without_tax, current_quantity, old_excise_tax)
    new_taxes = taxes(new_price_without_tax, new_quantity, new_excise_tax)


    dict_gasoline['new_expenditures'] = new_expenditures
    dict_gasoline['variation_expenditures'] = variation_expenditures
    dict_gasoline['new_quantity'] = new_quantity
    dict_gasoline['current_quantity'] = current_quantity
    dict_gasoline['current_taxes'] = current_taxes
    dict_gasoline['new_taxes'] = new_taxes

    return dict_gasoline


if __name__ == "__main__":
    expenditures = 1000
    example = gasoline_example(expenditures)