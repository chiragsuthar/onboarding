from django.db import models
from django.contrib.auth.models import User

class CountryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DocumentSetModel(models.Model):
    name = models.CharField(max_length=100)
    countries = models.ManyToManyField(CountryModel)
    has_backside = models.BooleanField(default=False)
    ocr_labels = models.JSONField()  # Requires Django 3.1+

    def __str__(self):
        return self.name

class CustomerModel(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    nationality = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.surname}"

class CustomerDocumentModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to='documents/')
    extracted_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document for {self.customer}"
