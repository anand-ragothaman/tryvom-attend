from django import forms


class Category_add_form(forms.Form):
    category = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter category'
            }
        )
    )
