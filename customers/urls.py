from django.urls import path
from .views import CreateCustomerView, UploadDocumentView, CustomerListView

urlpatterns = [
    path('create_customer/', CreateCustomerView.as_view(), name='create_customer'),
    path('upload_document/<int:customer_id>/', UploadDocumentView.as_view(), name='upload_document'),
    path('customer_list/', CustomerListView.as_view(), name='customer_list'),  # Updated URL pattern name
]
