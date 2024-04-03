from django import forms

class TriangleForm(forms.Form):
    side1 = forms.FloatField(label="Strana A")
    side2 = forms.FloatField(label="Strana B")
    side3 = forms.FloatField(label="Strana C")

    def calculate_perimeter(self):
        return self.cleaned_data['side1'] + self.cleaned_data['side2'] + self.cleaned_data['side3']

    def calculate_area(self):
        p = self.calculate_perimeter() / 2
        return ((p * (p - self.cleaned_data['side1']) * (p - self.cleaned_data['side2']) * (p - self.cleaned_data['side3'])) ** 0.5)
    
class SquareForm(forms.Form):
    side = forms.FloatField(label="Strana")

    def calculate_perimeter(self):
        return self.cleaned_data['side'] * 4

    def calculate_area(self):
        return self.cleaned_data['side'] ** 2

class CircleForm(forms.Form):
    radius = forms.FloatField(label="Poloměr")

    def calculate_perimeter(self):
        return 2 * 3.14 * self.cleaned_data['radius']

    def calculate_area(self):
        return 3.14 * self.cleaned_data['radius'] ** 2