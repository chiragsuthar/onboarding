from django import forms
from .models import CustomerModel, CustomerDocumentModel

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ['surname', 'firstname', 'nationality', 'gender']

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = CustomerDocumentModel
        fields = ['attached_file']
