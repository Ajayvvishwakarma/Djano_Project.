from SMS.models import*
from django import forms

class StudentForm(forms.ModelForm):  # MODEL FORM
    class Meta:
        model=Student
        fields='__all__'  #['name,'age']
    def in__init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in self.field.values():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']='Enter '+ field.label+' *'
    
class PaymentDetailsForm(forms.ModelForm):  # MODEL FORM
    class Meta:
        model=PaymentDetails
        fields='__all__'  