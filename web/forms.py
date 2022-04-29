from django import forms

class Kontakt(forms.Form):
    od = forms.IntegerField()
    do = forms.IntegerField()
    sheet = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(Kontakt, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
        self.fields['od'].widget.attrs['placeholder'] = "Od(Redak)"
        self.fields['do'].widget.attrs['placeholder'] = "Do(Redak)"
        self.fields['sheet'].widget.attrs['placeholder'] = "Redni broj Excel liste"



        
        