from django import forms
from .models import CollectorModel, GameModel
from datetime import date


class CollectorForm(forms.ModelForm):
    class Meta:
        model = CollectorModel
        fields = ["username", "password1", "password2"]


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords DO NOT MATCH!!!!!!!!!!!!!")


class GameForm(forms.ModelForm):
    class Meta:
        model = GameModel
        exclude = ["foreignKeyToCollector"]

    def clean_ageLimit(self):
        cleanAgeData = self.cleaned_data["ageLimit"]

        if cleanAgeData < 13:
            raise forms.ValidationError("Age too young")

        return cleanAgeData

    def clean_dateMade(self):
        cleanDateData = self.cleaned_data["dateMade"]

        if cleanDateData == None:
            raise forms.ValidationError("No date was entered")

        if cleanDateData > date.today():
            raise forms.ValidationError("Future date should not be entered")

        return cleanDateData
