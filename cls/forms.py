
from django import forms
from django.forms import fields, widgets
from . models import Attendance, Employ, Training, Vacation 


class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class AttendForm(forms.ModelForm):
    class Meta:
        model=Attendance
        fields=[
            'name_employ',
            'status',
            'date'
        ]        
        widgets ={
            'name_employ': forms.Select(attrs={'class':'form-control','placeholder':'Name'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'date':forms.TextInput(attrs={'class':'form-control','type':'Date'})

        }

class VacationForm(forms.ModelForm):
    class Meta:
        model=Vacation
        fields=[
            'employ_name',
            'title',
            'start_date',
            'end_date',
            'purpose',
        ]        
        widgets ={
            'employ_name': forms.Select(attrs={'class':'form-control','placeholder':'Name'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'start_date':forms.TextInput(attrs={'class':'form-control','type':'Date'}),
            'end_date':forms.TextInput(attrs={'class':'form-control','type':'Date'}),
            'purpose':forms.TextInput(attrs={'class':'form-control','type':'Text'}),
        }
        
class TrainingForm(forms.ModelForm):
    class Meta:
        model=Training
        fields=[
            'names',
            'title',
            'description'
        ]        
        widgets ={
            'names': forms.Select(attrs={'class':'form-control','placeholder':'Name'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),
            'description':forms.TextInput(attrs={'class':'form-control','type':'Text'})

        }