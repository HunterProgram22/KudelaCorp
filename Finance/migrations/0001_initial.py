# Generated by Django 2.1.2 on 2018-10-19 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthBal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fifththird_check', models.DecimalField(decimal_places=2, max_digits=8)),
                ('huntington_check', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fifththird_save', models.DecimalField(decimal_places=2, max_digits=8)),
                ('huntington_save', models.DecimalField(decimal_places=2, max_digits=8)),
                ('capone_save', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amex_save', models.DecimalField(decimal_places=2, max_digits=8)),
                ('robinhood_invest', models.DecimalField(decimal_places=2, max_digits=8)),
                ('buckeye_invest', models.DecimalField(decimal_places=2, max_digits=8)),
                ('deacon_invest', models.DecimalField(decimal_places=2, max_digits=8)),
                ('four57_retire', models.DecimalField(decimal_places=2, max_digits=8)),
                ('four01_retire', models.DecimalField(decimal_places=2, max_digits=8)),
                ('roth_retire', models.DecimalField(decimal_places=2, max_digits=8)),
                ('opers_retire', models.DecimalField(decimal_places=2, max_digits=8)),
                ('justin_car', models.DecimalField(decimal_places=2, max_digits=8)),
                ('kat_car', models.DecimalField(decimal_places=2, max_digits=8)),
                ('main_home', models.DecimalField(decimal_places=2, max_digits=8)),
                ('car_loan', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pubstudent_loan', models.DecimalField(decimal_places=2, max_digits=8)),
                ('privstudent_loan', models.DecimalField(decimal_places=2, max_digits=8)),
                ('main_mortgage', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amex_credit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discover_credit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('capone_credit', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='MonthInc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('huntington_interest', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fifththird_interest', models.DecimalField(decimal_places=2, max_digits=8)),
                ('capone_interest', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amex_interest', models.DecimalField(decimal_places=2, max_digits=8)),
                ('schwab_interest', models.DecimalField(decimal_places=2, max_digits=8)),
                ('schwab_dividends', models.DecimalField(decimal_places=2, max_digits=8)),
                ('expense_checks', models.DecimalField(decimal_places=2, max_digits=8)),
                ('miscellaneous_income', models.DecimalField(decimal_places=2, max_digits=8)),
                ('refund_rebate_repayment', models.DecimalField(decimal_places=2, max_digits=8)),
                ('gift_income', models.DecimalField(decimal_places=2, max_digits=8)),
                ('supremecourt_salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cdm_salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('opers_retirement', models.DecimalField(decimal_places=2, max_digits=8)),
                ('four57b_retirement', models.DecimalField(decimal_places=2, max_digits=8)),
                ('four01k_retirement', models.DecimalField(decimal_places=2, max_digits=8)),
                ('roth_retirement', models.DecimalField(decimal_places=2, max_digits=8)),
                ('robinhood_investments', models.DecimalField(decimal_places=2, max_digits=8)),
                ('schwab_investments', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amex_savings', models.DecimalField(decimal_places=2, max_digits=8)),
                ('fifththird_savings', models.DecimalField(decimal_places=2, max_digits=8)),
                ('capone_savings', models.DecimalField(decimal_places=2, max_digits=8)),
                ('five29_college', models.DecimalField(decimal_places=2, max_digits=8)),
                ('huntington_savings', models.DecimalField(decimal_places=2, max_digits=8)),
                ('federal_tax', models.DecimalField(decimal_places=2, max_digits=8)),
                ('social_security', models.DecimalField(decimal_places=2, max_digits=8)),
                ('medicare', models.DecimalField(decimal_places=2, max_digits=8)),
                ('ohio_tax', models.DecimalField(decimal_places=2, max_digits=8)),
                ('columbus_tax', models.DecimalField(decimal_places=2, max_digits=8)),
                ('health_insurance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('supplementallife_insurance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('flex_spending', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cdm_std', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cdmsupplemental_ltd', models.DecimalField(decimal_places=2, max_digits=8)),
                ('parking', models.DecimalField(decimal_places=2, max_digits=8)),
                ('parking_admin', models.DecimalField(decimal_places=2, max_digits=8)),
                ('main_mortgage', models.DecimalField(decimal_places=2, max_digits=8)),
                ('hoa_fees', models.DecimalField(decimal_places=2, max_digits=8)),
                ('auto_insurance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('aep_electric', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rumpke_trash', models.DecimalField(decimal_places=2, max_digits=8)),
                ('delaware_sewer', models.DecimalField(decimal_places=2, max_digits=8)),
                ('delco_water', models.DecimalField(decimal_places=2, max_digits=8)),
                ('suburban_gas', models.DecimalField(decimal_places=2, max_digits=8)),
                ('verizon_kat', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sprint_justin', models.DecimalField(decimal_places=2, max_digits=8)),
                ('directtv_cable', models.DecimalField(decimal_places=2, max_digits=8)),
                ('timewarner_internet', models.DecimalField(decimal_places=2, max_digits=8)),
                ('caponeauto_loan', models.DecimalField(decimal_places=2, max_digits=8)),
                ('public_loan', models.DecimalField(decimal_places=2, max_digits=8)),
                ('private_loan', models.DecimalField(decimal_places=2, max_digits=8)),
                ('capone_creditcard', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amex_creditcard', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discover_creditcard', models.DecimalField(decimal_places=2, max_digits=8)),
                ('kohls_vicsec_macy_eddiebauer_creditcards', models.DecimalField(decimal_places=2, max_digits=8)),
                ('katwork_creditcard', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cashorcheck_purchases', models.DecimalField(decimal_places=2, max_digits=8)),
                ('daycare', models.DecimalField(decimal_places=2, max_digits=8)),
                ('taxdeductible_giving', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]