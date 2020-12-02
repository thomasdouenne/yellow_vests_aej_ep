# How to use this repo to reproduce the paper "Yellow Vests, Pessimistic Beliefs, and Carbon Tax Aversion" (AEJ:EP)?

Authors :
- Thomas Douenne, University of Amsterdam, Roetersstraat 11, 1018 WB Amsterdam, Netherlands (email: t.r.g.r.douenne@uva.nl)
- Adrien Fabre, ETH Zürich (D-MTEC), Zürichberstrasse 18, 8032 Zürich, Switzerland (email: fabre.adri1@gmail.com)

- The code is in R and Python.
- The main file is papier.R: it enables researchers to reproduce all the empirical findings of the paper section by section.
- In order to run this script, a few preliminary steps are needed. They are described below.

# Option 1 (short version):
- First, go to preparation.R and run this script. It will prepare the dataset (called "s") used all along the paper, and load the packages needed.
- Second, go to papier.R and run the main code.

# Option 2 (long version):
- In this repository you will find some .csv files, some of which are produced by the .py files. You can reproduce these .csv yourself.
- These .csv files use official statistics, in particular to compute the objective distribution of gains and losses from the carbon tax and dividend.
    - Step 1: go to prepare_dataset.py and run the script to build a dataset from data_menages.csv. This .csv provides data from the survey "Budget de Famille 2011".
    - Step 2: then the script gains_losses_data.py can be used to compute the incidence of the tax and dividend policy on all households in the dataset.
    From there several things can be done:
        - consistency_bdf_ptc.py compares the distribution of the tax incidence computed from official statistics to the ones of our survey (hence, need to run preparation.R before).
        This script can also be used to reproduce df_subjective_gains.csv, df_objective_gains.csv, or df_objective_gains_inelastic.csv (by changing parameters' values in the computation of the tax incidence).
        - regression_feedback.py enables to regress the policy's incidence for housing energies. This will be used to estimate respondent-specific tax incidence.
        It can be done either from the consumer ('bdf') or housing ('enl') survey. Both dataset for housing energies can be generated using prepare_dataset_housing.py
        - test_predictions_ols_regression_with_transports.py, test_predictions_binary_models.py, and matching_predict_winner.R assess the precision of our respondent-specific estimation of the tax incidence.
        This is used to provide a customized feedback on respondents expected net gain (see Section 4 of the paper).
- Then, you can run preparation.R, and the main code papier.R
