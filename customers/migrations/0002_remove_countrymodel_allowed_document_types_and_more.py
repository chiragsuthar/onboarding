# Generated by Django 5.0.6 on 2024-05-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countrymodel',
            name='allowed_document_types',
        ),
        migrations.RemoveField(
            model_name='countrymodel',
            name='textract_document_type',
        ),
        migrations.AlterField(
            model_name='customerdocumentmodel',
            name='attached_file',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='customerdocumentmodel',
            name='extracted_json',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='documentsetmodel',
            name='ocr_labels',
            field=models.JSONField(),
        ),
    ]
