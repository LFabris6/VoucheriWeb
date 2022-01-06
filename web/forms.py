from django import forms

class Kontakt(forms.Form):
    email = forms.EmailField(max_length=50)
    poruka = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

    def __init__(self, *args, **kwargs):
        super(Kontakt, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['poruka'].widget.attrs['placeholder'] = "Poruka"
        
        