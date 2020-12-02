# -*- coding: utf-8 -*-

from __future__ import division

import pandas as pd

from prepare_dataset import prepare_dataset
from gains_losses_data import compute_gains_losses


def match_households_per_categ(df_hh, cu, heating, size, hh_income):
    
    # Select household size
    df_hh = df_hh.query('consumption_units == {}'.format(cu))

    # Select energy for heating
    df_hh = df_hh.query('{} == 1'.format(heating))

    # Select accomodation size : up to plus or minus 30% than the hh
    df_hh = df_hh.query('accommodation_size > 0.7 * {}'.format(size))
    df_hh = df_hh.query('accommodation_size < 1.3 * {}'.format(size))
    
    # Select income
    df_hh = df_hh.query('hh_income > 0.7 * {}'.format(hh_income * 12))
    df_hh = df_hh.query('hh_income < 1.3 * {}'.format(hh_income * 12))

    return df_hh


if __name__ == "__main__":
    df_hh = prepare_dataset()

    consumption_units = 1.8
    heating = 'natural_gas'
    accommodation_size = 80
    hh_income = 2500

    df_hh = match_households_per_categ(df_hh, consumption_units, heating, accommodation_size, hh_income)
    
    print df_hh['{}_expenditures'.format(heating)].mean()
