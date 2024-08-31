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


class Category_edit_form(forms.Form):
    id = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'hidden': 'hidden',
            }
        )
    )
    category = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter category'
            }
        )
    )
