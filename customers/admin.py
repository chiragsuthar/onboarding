from django.contrib import admin
from .models import CountryModel, DocumentSetModel, CustomerModel, CustomerDocumentModel

@admin.register(CountryModel)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(DocumentSetModel)
class DocumentSetAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['countries']

class CustomerDocumentInline(admin.TabularInline):
    model = CustomerDocumentModel
    extra = 1  # Number of empty forms to display

@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'surname', 'nationality', 'gender', 'created_by']
    inlines = [CustomerDocumentInline]

@admin.register(CustomerDocumentModel)
class CustomerDocumentAdmin(admin.ModelAdmin):
    list_display = ['customer', 'attached_file', 'created_at']
    readonly_fields = ['extracted_json']
