from django import forms
from .models import MonthBal, MonthInc

class MonthBalForm(forms.ModelForm):

    class Meta:
        model = MonthBal
        fields = ('date', 'huntington_check', 'fifththird_check',  'huntington_save',
                  'fifththird_save', 'capone_save', 'amex_save', 'robinhood_invest', 'deacon_invest',
                  'buckeye_invest', 'opers_retire', 'four57_retire', 'four01_retire', 'roth_retire',
                  'main_home', 'justin_car', 'kat_car', 'capone_credit', 'amex_credit',
                  'discover_credit', 'car_loan', 'pubstudent_loan', 'privstudent_loan',
                  'main_mortgage',)

class MonthIncForm(forms.ModelForm):

    class Meta:
        model = MonthInc
        fields = ('date', 'huntington_interest', 'fifththird_interest',
                  'capone_interest', 'amex_interest', 'schwab_interest',
                  'schwab_dividends', 'expense_checks', 'miscellaneous_income',
                  'refund_rebate_repayment', 'gift_income', 'supremecourt_salary',
                  'cdm_salary', 'opers_retirement', 'four57b_retirement',
                  'four01k_retirement', 'roth_retirement', 'robinhood_investments', 'schwab_investments',
                  'amex_savings', 'fifththird_savings', 'capone_savings', 'five29_college',
                  'huntington_savings', 'federal_tax', 'social_security', 'medicare',
                  'ohio_tax', 'columbus_tax', 'health_insurance',
                  'supplementallife_insurance', 'flex_spending', 'cdm_std',
                  'cdmsupplemental_ltd', 'parking', 'parking_admin', 'main_mortgage',
                  'hoa_fees', 'auto_insurance', 'aep_electric', 'rumpke_trash',
                  'delaware_sewer', 'delco_water', 'suburban_gas', 'verizon_kat',
                  'sprint_justin', 'directtv_cable', 'timewarner_internet',
                  'caponeauto_loan', 'public_loan', 'private_loan', 'capone_creditcard',
                  'amex_creditcard', 'discover_creditcard', 'kohls_vicsec_macy_eddiebauer_creditcards',
                  'katwork_creditcard', 'cashorcheck_purchases', 'daycare',
                  'taxdeductible_giving',)