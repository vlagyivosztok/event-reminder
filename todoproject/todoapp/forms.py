from django import forms
from .models import MainCategory, SubCategory, Person, Event

class MainCategoryForm(forms.ModelForm):
    class Meta:
        model = MainCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Főkategória neve'}),
        }

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['main_category', 'name']
        widgets = {
            'main_category': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alkategória neve'}),
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'email', 'phone']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teljes név'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (opcionális)'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon (opcionális)'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'person', 'subcategory', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Esemény vagy Okmány neve'}),
            'person': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
