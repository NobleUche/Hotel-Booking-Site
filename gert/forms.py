from dataclasses import fields
from django import forms
from .models import reservation



class reservation_form(forms.ModelForm):
    class Meta:
        model = reservation
        fields = "__all__"