from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class ChooseOptions(FlaskForm):
    name = StringField('Imię i nazwisko')
    street = StringField('Ulica, nr domu, nr mieszkania')
    city = StringField('Miasto')
    green_general = BooleanField('Sprzeciwiam się przeznaczeniu całej południowej części (okolice Lasu Borkowskiego) pod inwestycje. Całą niezabudowaną jeszcze część obszaru należy przeznazyć pod zieleń.')
    green_roofs = BooleanField('Nawet jeśli południowa część terenu będzie przeznaczona pod inwestycje, wszędzie należy stosować tzw. intensywne zielone dachy (także na budynkach mieszkalnych).')
    green_mw11 = BooleanField('Nawet jeśli teren MW11 zostanie przeznaczony pod inwestycje, powinien zostać poszerzony zaplanowany na nim obszar zieleni.')
    green_mw14 = BooleanField('Nawet jeśli teren MW14 zostanie przeznaczony pod inwestycje, powinien zostać poszerzony zaplanowany na nim obszar zieleni osiedlowej.')
    green_mw15 = BooleanField('Nawet jeśli teren MW15 zostanie przeznaczony pod inwestycje, powinien zostać poszerzony zaplanowany na nim obszar zieleni osiedlowej.')
    green_mwu6 = BooleanField('Należy zwiększyć park, który ma sąsiadować z ulicami Bułgarską i Pszczelną (zamiast zabudowy terenu MW/U.6).')
    submit = SubmitField('Wyślij')