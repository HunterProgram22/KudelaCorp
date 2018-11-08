from django import forms
from .models import OptionPosition

class OptionPositionForm(forms.ModelForm):

    class Meta:
        model = OptionPosition
        fields = ('stock', 'account', 'position_status', 'position_open_date',
                  'position_expiration_date', 'position_close_date', 'option_play',
                  'strike_prices', 'directional_bias', 'contracts_bought', 'strategy',
                  'probability_of_profit', 'max_profit', 'max_loss', 'buying_power_reduction',
                  'cost_to_enter_trade', 'fees_to_enter_trade', 'cost_to_exit_trade',
                  'fees_to_exit_trade',)
