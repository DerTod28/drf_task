# Generated by Django 4.2.2 on 2023-06-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='employee_photos'),
        ),
    ]
