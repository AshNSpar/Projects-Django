from django import forms

class CalculationForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

    def clean(self):
        cleaned_data=super().clean()
        num1=cleaned_data["num1"]
        num2=cleaned_data["num2"]
        if int(num1)<0:
            msg="please enter postive number"
            self.add_error("num1",msg)
        if int(num2)<0:
            msg="please enter postive number"
            self.add_error("num2",msg)

class CubeForm(forms.Form):
    num=forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        num=cleaned_data["num"]
        if num<0:
            msg="please enter positive number"
            self.add_error("num",msg)