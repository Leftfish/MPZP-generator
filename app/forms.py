from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class ChooseOptions(FlaskForm):
    name = StringField('Imię i nazwisko')
    street = StringField('Ulica, nr domu, nr mieszkania')
    city = StringField('Miasto')
    green_general = BooleanField('Sprzeciwiam się przeznaczeniu całej południowej części (okolice Lasu Borkowskiego) pod inwestycje. Całą niezabudowaną jeszcze część obszaru należy przeznazyć pod zieleń.')
    green_roofs = BooleanField('Nawet jeśli południowa część terenu będzie przeznaczona pod inwestycje, wszędzie należy stosować tzw. intensywne zielone dachy (także na budynkach mieszkalnych, nie tylko na garażach).')
    green_mw11 = BooleanField('Nawet jeśli teren MW11 (graniczący z osiedlem przy ul. Torfowej i planowaną ul. 8 Pułku Ułanów) zostanie przeznaczony pod inwestycje, powinien zostać poszerzony zaplanowany na nim obszar zieleni, a zabudowa powinna być mniej intensywna.')
    green_mw12 = BooleanField('Nawet jeśli teren MW12 (graniczący z osiedlem przy ul. Torfowej i domami jednorodzinnymi przy ul. Studzianki i ul. Zalesie) zostanie przeznaczony pod inwestycje, zabudowa powinna być mniej intensywna.')
    green_mw14 = BooleanField('Nawet jeśli teren MW14 (sąsiedztwo bloków przy ul. Obozowej 114-120 i ul. Zdunów) zostanie przeznaczony pod inwestycje, powinien zostać poszerzony zaplanowany na nim obszar zieleni osiedlowej.')
    green_mw15 = BooleanField('Nawet jeśli teren MW15 (sąsiedztwo bloków przy ul. Obozowej 114-120 i ul. Podhalańskiej) zostanie przeznaczony pod inwestycje, powinien zostać poszerzony zaplanowany na nim obszar zieleni osiedlowej.')
    green_mwu6 = BooleanField('Należy zwiększyć park, który ma sąsiadować z ulicami Bułgarską i Pszczelną (zamiast zabudowy terenu MW/U.6).')
    submit = SubmitField('Przygotuj pismo')