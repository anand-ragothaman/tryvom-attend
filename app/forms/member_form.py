from django import forms

from app.models.category_models import Category


class Member_add_form(forms.Form):
    name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }
        )
    )
    member_id = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter member id'
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label='Select category',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Select category'
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter description',
                'id': 'ckeditor'
            }
        )
    )


class Member_edit_form(forms.Form):
    id = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'hidden': 'hidden',
            }
        )
    )
    name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }
        )
    )
    member_id = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter member id'
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label='Select category',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Select category'
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter description',
                'id': 'ckeditor'
            }
        )
    )
