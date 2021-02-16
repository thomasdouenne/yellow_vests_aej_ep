# How to use this repo to reproduce the paper "Yellow Vests, Pessimistic Beliefs, and Carbon Tax Aversion" (AEJ:EP)?

# Authors:
- Thomas Douenne, University of Amsterdam, Roetersstraat 11, 1018 WB Amsterdam, Netherlands (email: t.r.g.r.douenne@uva.nl)
- Adrien Fabre, ETH Zürich (D-MTEC), Zürichberstrasse 18, 8032 Zürich, Switzerland (email: fabre.adri1@gmail.com)

# Summary:
- The code is in R and Python.
- The main file is code/papier.R: it enables researchers to reproduce all the empirical findings of the paper section by section.
- In order to run this script, a few preliminary steps are needed. They are described below.

# Option 1 (short version):
- First, go to code/preparation.R and run this script. It will prepare the dataset (called "s") used all along the paper, and load the packages needed.
- Second, go to code/papier.R and run the main code.

# Option 2 (long version):
- In this repository you will find some .csv files, some of which are produced by the .py files. You can reproduce these .csv yourself.
- These .csv files use official statistics, in particular to compute the objective distribution of gains and losses from the carbon tax and dividend.
    - Step 1: go to model_reforms_data/prepare_dataset.py and run the script to build a dataset from data_menages.csv. This .csv provides data from the survey "Budget de Famille 2011".
    - Step 2: then the script model_reforms_data/gains_losses_data.py can be used to compute the incidence of the tax and dividend policy on all households in the dataset.
    From there several things can be done:
        - consistency_bdf_ptc.py compares the distribution of the tax incidence computed from official statistics to the ones of our survey (hence, need to run code/preparation.R before).
        This script can also be used to reproduce df_subjective_gains.csv, df_objective_gains.csv, or df_objective_gains_inelastic.csv (by changing parameters' values in the computation of the tax incidence).
        - model_reforms_data/regression_feedback.py enables to regress the policy's incidence for housing energies. This will be used to estimate a respondent-specific tax incidence.
        It can be done either from the consumer ('bdf') or housing ('enl') survey. Both datasets for housing energies can be generated using model_reforms_data/prepare_dataset_housing.py
        - test_predictions_ols_regression_with_transports.py, test_predictions_binary_models.py, and code/matching_predict_winner.R assess the precision of our respondent-specific estimation of the tax incidence.
        This is used to provide a customized feedback on respondents' expected net gain (see Section 4 of the paper).
- Then, you can run code/preparation.R, and the main code code/papier.R


# List of files
code/agglos.csv: data used to match town code to information on town size, provided by the survey company Bilendi
code/correspondance-code-insee-code-postal.csv: data from Insee, matches postal code with characteristics of the town, unused
code/df_menages_domicile_teg.csv: data used in preparation.R but not in the paper: subsample from transport survey used in companion paper
code/df_objective_gains.csv: distribution of respondents objective gains plotted in section 3 and procuded by consistency_beliefs_losses.py
code/df_objective_gains_inelastic.csv: distribution of respondents objective gains assuming inelastic demand, plotted in section 3 and procuded by consistency_beliefs_losses.py
code/df_subjective_gains.csv: distribution of respondents subjective gains plotted in section 3 and procuded by consistency_beliefs_losses.py
code/matching_predict_winner.R: performs statistical matching as an alternative way to predict winners and losers
code/packages_functions.R: loads all the necessary packages
code/papier.R: main code, enables to reproduce all the findings of the paper
code/preparation.R: necessary to run this script before executing papier.R, prepares the dataset to be used
code/questionnaire.qsf: enables to import the questionnaire in Qualtrics
code/quotas.xlsx: provides objectives quotas from Insee, information obtained from Insee's website
code/rev_i_erfs2014.csv: data from survey ERFS used to get information on actual income distribution of the French population (selected variables)
code/survey.csv: raw data from Qualtrics survey
code/survey_prepared.csv: data from Qualtrics survey after preparation

images/: different images generated from papier.R, also includes images from companion paper

model_reforms/define_tax_incidence.py: defines formulas to study the tax incidence
model_reforms/diesel_standard_example.py: specific example applied to diesel
model_reforms/domestic_fuel_standard_example.py: specific example applied to domestic_fuel
model_reforms/gas_standard_example.py: specific example applied to natural gas
model_reforms/gasoline_standard_example: specific example applied to gasoline

model_reforms_data/computation_co2_emissions.py: compute the reduction in CO2 emissions from the policy
model_reforms_data/define_tax_incidence_data.py: defines formulas to study the tax incidence on households in surveys
model_reforms_data/gains_losses_data.py: computes tax incidence on households in surveys
model_reforms_data/prepare_dataset.py: prepares the dataset (selects variables, translates names to English, inflates sectoral expenditures)
model_reforms_data/prepare_dataset_housing.py: prepares the dataset for housing energies only (selects variables, translates names to English, inflates sectoral expenditures)
model_reforms_data/regression_feedback.py: regress households' expenditures in housing energies on househlds' characteristics
model_reforms_data/standardize_data_bdf_ptc.py: defines functions to compare new survey with official statistics (in particular subjective vs objective gains), functions are used by consistency_beliefs_losses.py
model_reforms_data/data_menages.csv: data to be used in prepare_dataset.py : comes from the matching of the consumer and transport surveys (Douenne, 2020, The Energy Journal) (selected variables)
model_reforms_data/data_matching_bdf.csv: data to be used in prepare_dataset_housing.py : comes from the French consumer survey (selected variables)
model_reforms_data/data_matching_enl.csv: data to be used in prepare_dataset_housing.py : comes from the French housing survey (selected variables)
model_reforms_data/prediction expenditures.csv: data on objective gains and losses produced in test_predictions_ols_regression_with_transports.py. and used to assess precision of our prediction
model_reforms_data/prediction expenditures (2).csv: alternative specification for the prediction, called in code/preparation.R but unused in the paper
model_reforms_data/prediction housing expenditures.csv: same thing but specific to housing energies, called in code/preparation.R but unused in the paper
model_reforms_data/prediction housing expenditures (2).csv: same thing but specific to housing energies, called in code/preparation.R but unused in the paper

Questionnaire/: files used for questionnaire on Qualtrics

consistency_beliefs_losses.py: compares new survey with official statistics (in particular subjective vs objective gains) and produces figures C.3 and df_objective_gains.csv, df_objective_gains_inelastic.csv, and df_subjective_gains.csv
df_donor_enl.csv: data produced by test_predictions_ols_regression_with_transports.py from housing survey and used for the statistical matching (alternative method to predict winners and losers)
df_objective_gains.csv: distribution of respondents objective gains plotted in section 3 and procuded by consistency_beliefs_losses.py
df_objective_gains_inelastic.csv: distribution of respondents objective gains assuming inelastic demand, plotted in section 3 and procuded by consistency_beliefs_losses.py
df_subjective_gains.csv: distribution of respondents subjective gains plotted in section 3 and procuded by consistency_beliefs_losses.py
df_receiver_bdf.csv: data produced by test_predictions_ols_regression_with_transports.py from consumer survey and used for the statistical matching (alternative method to predict winners and losers)
LICENSE: License to use the present repository
test_predictions_binary_models.py: tests accuracy of our respondent-specific win/lose prediction for alternative specifications and methods
test_predictions_ols_regression_with_transports.py: tests accuracy of our respondent-specific estimation of the tax incidence
utils.py: defines useful functions to plot graphs

# Data and Code Availability Statements
## Authors' Survey Data
Fully available. 
URL: https://github.com/thomasdouenne/yellow_vests_aej_ep/tree/main/code/survey_prepared.csv

## Douenne (2020)
Fully available. 
URL: https://github.com/thomasdouenne/yellow_vests_aej_ep/tree/main/model_reforms_data/data_menages.csv

## Insee Budget de Famille (BdF 2011)
Fully available to researchers upon completion of a form.
Presentation of the survey: https://www.insee.fr/en/metadonnees/source/serie/s1194
URL: http://www.progedo-adisp.fr/enquetes/XML/lil.php?lil=lil-0831

## Insee Enquete Nationale Transports et Deplacements (ENTD 2008)
Fully available to researchers upon completion of a form.
Presentation of the survey: https://www.insee.fr/en/metadonnees/source/serie/s1277
URL: http://www.progedo-adisp.fr/enquetes/XML/lil.php?lil=lil-0634

## Insee Enquete Logement (EL 2013)
Fully available to researchers upon completion of a form.
Presentation of the survey: https://www.insee.fr/en/metadonnees/source/serie/s1004
URL: http://www.progedo-adisp.fr/enquetes/XML/lil.php?lil=lil-1022

## Insee Enquête sur les Revenus Socio-Fiscaux (ERFS 2014)
Fully available to researchers upon completion of a form.
URL: http://www.progedo-adisp.fr/enquetes/XML/lil.php?lil=lil-1177

## National Accounts

## CEREN
Fully available. It consists of the following quote: “3,4 millions de résidences principales sont encore chauffées au fioul en France. Cela représente 12 % des foyers”.
URL: https://www.lesechos.fr/industrie-services/energie-environnement/le-chauffage-au-fioul-devient-de-plus-en-plus-cher-147372