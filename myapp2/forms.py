from django import forms


class ChooseGameForm(forms.Form):
    game = forms.ChoiceField(choices=[('C', 'Coin'), ('D', 'Dice'), ('H', 'Hundred')])
    count = forms.IntegerField(min_value=1)

