from django.db import models

class OptionPosition(models.Model):
    NAKED_CALL = "Naked Call"
    NAKED_PUT = "Naked Put"
    CALL_CREDIT_SPREAD = "Call Credit Spread"
    CALL_DEBIT_SPREAD = "Call Debit Spread"
    PUT_CREDIT_SPREAD = "Put Credit Spread"
    PUT_DEBIT_SPREAD = "Put Debit Spread"
    IRON_CONDOR = "Iron Condor"
    IRON_BUTTERFLY = "Iron Butterfly"
    CALENDAR_SPREAD = "Calendar Spread"
    JADE_LIZARD = "Jade Lizard"
    PUT_RATIO_BACKSPREAD = "Put Ratio Backspread"
    SYNTHETIC_COVERED_CALL = "Synthetic Covered Call"
    CUSTOM = "Custom"
    OPTIONS_PLAYBOOK = (
        (NAKED_CALL, "Naked Call"),
        (NAKED_PUT, "Naked Put"),
        (CALL_CREDIT_SPREAD, "Call Credit Spread"),
        (CALL_DEBIT_SPREAD, "Call Debit Spread"),
        (PUT_CREDIT_SPREAD, "Put Credit Spread"),
        (PUT_DEBIT_SPREAD, "Put Debit Spread"),
        (IRON_CONDOR, "Iron Condor"),
        (IRON_BUTTERFLY, "Iron Butterfly"),
        (CALENDAR_SPREAD, "Calendar Spread"),
        (JADE_LIZARD, "Jade Lizard"),
        (PUT_RATIO_BACKSPREAD, "Put Ratio Backspread"),
        (SYNTHETIC_COVERED_CALL, "Synthetic Covered Call"),
        (CUSTOM, "Custom"),
    )

    BULLISH = "Bullish"
    BEARISH = "Bearish"
    NEUTRAL = "Neutral"
    DIRECTIONAL_BIAS_CHOICES = (
        (BULLISH, "Bullish"),
        (BEARISH, "Bearish"),
        (NEUTRAL, "Neutral"),
    )

    SELL_PREMIUM = "Sell Premium"
    TREND_TRADE = "Trend Trade"
    SPEC_TRADE = "Spec Trade"
    QUICK_TRADE = "Quick Trade"
    FLAT_TRADE = "Flat Trade"
    EARNINGS_PLAY = "Earnings Play"
    OPTIONS_STRATEGY = (
        (SELL_PREMIUM, "Sell Premium"),
        (TREND_TRADE, "Trend Trade"),
        (SPEC_TRADE, "Spec Trade"),
        (QUICK_TRADE, "Quick Trade"),
        (FLAT_TRADE, "Flat Trade"),
        (EARNINGS_PLAY, "Earnings Play"),
    )

    ROBINHOOD = "Robinhood"
    TASTYWORKS = "Tastyworks"
    ACCOUNTS = (
        (ROBINHOOD, "Robinhood"),
        (TASTYWORKS, "Tastyworks"),
    )

    OPEN = "Open"
    CLOSED = "Closed"
    POSITION_STATUS = (
        (OPEN, "Open"),
        (CLOSED, "Closed"),
    )

    stock = models.CharField(max_length=10)
    account = models.CharField(max_length=30,
        choices=ACCOUNTS,
        default=ROBINHOOD )
    position_status = models.CharField(max_length=10,
        choices=POSITION_STATUS,
        default=OPEN)
    position_open_date = models.DateField()
    position_expiration_date = models.DateField()
    position_close_date = models.DateField(null=True, blank=True)
    option_play = models.CharField(max_length=50,
        choices=OPTIONS_PLAYBOOK,
        default=NAKED_CALL  )
    strike_prices = models.CharField(max_length=100)
    directional_bias = models.CharField(max_length=20,
        choices=DIRECTIONAL_BIAS_CHOICES,
        default=BULLISH )
    contracts_bought = models.DecimalField(max_digits=6, decimal_places=0)
    strategy = models.CharField(max_length=50,
        choices=OPTIONS_STRATEGY)
    probability_of_profit = models.DecimalField(max_digits=5, decimal_places=2)
    max_profit = models.DecimalField(max_digits=8, decimal_places=2)
    max_loss = models.DecimalField(max_digits=8, decimal_places=2)
    buying_power_reduction = models.DecimalField(max_digits=8, decimal_places=2)
    cost_to_enter_trade = models.DecimalField(max_digits=8, decimal_places=2)
    fees_to_enter_trade = models.DecimalField(max_digits=8, decimal_places=2)
    cost_to_exit_trade = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fees_to_exit_trade = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)



    def days_to_expiration(self):
        return self.position_expiration_date - time.today()

    def profit_or_loss(self):
        return self.cost_to_exit_trade - self.cost_to_enter_trade - (self.fees_to_enter_trade + self.fees_to_exit_trade)
