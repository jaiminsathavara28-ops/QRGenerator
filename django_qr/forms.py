from django import forms

class QRCodeForm(forms.Form):
    company_name = forms.CharField(
        max_length=200,
        label='Company_name',
        widget=forms.TextInput(attrs={
            'class':'form-control'                           ,
            'placeholder':'Enter company name'
       })
       )
    url = forms.URLField(
        max_length=200,
        required=False,
        label='Url',
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'Enter URL'
        })
        
        )