from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import CustomerModel, CustomerDocumentModel, DocumentSetModel
from .forms import CustomerForm, DocumentUploadForm
import boto3

class CustomerListView(ListView):
    model = CustomerModel
    template_name = 'customer_list.html'
    context_object_name = 'customers'

class CreateCustomerView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'create_customer.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_by = request.user
            customer.save()
            return redirect('upload_document', customer_id=customer.id)
        return render(request, 'create_customer.html', {'form': form})

class UploadDocumentView(View):
    def get(self, request, customer_id):
        form = DocumentUploadForm()
        return render(request, 'upload_document.html', {'form': form, 'customer_id': customer_id})

    def post(self, request, customer_id):
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            customer = CustomerModel.objects.get(id=customer_id)
            document = form.save(commit=False)
            document.customer = customer
            document.save()

            # Trigger OCR process here and update extracted_json field
            extracted_data = self.process_document(document.attached_file.path)
            document.extracted_json = extracted_data
            document.save()

            return redirect('customer_detail', customer_id=customer_id)
        return render(request, 'upload_document.html', {'form': form, 'customer_id': customer_id})

    def process_document(self, file_path):
        textract = boto3.client('textract', region_name='your-region')

        with open(file_path, 'rb') as document:
            response = textract.analyze_document(
                Document={'Bytes': document.read()},
                FeatureTypes=['FORMS']
            )

        extracted_data = {}
        for block in response['Blocks']:
            if block['BlockType'] == 'KEY_VALUE_SET':
                key, value = '', ''
                for relationship in block['Relationships']:
                    if relationship['Type'] == 'CHILD':
                        for id in relationship['Ids']:
                            if block['BlockType'] == 'KEY':
                                key += block['Text']
                            if block['BlockType'] == 'VALUE':
                                value += block['Text']
                extracted_data[key] = value

        return extracted_data
