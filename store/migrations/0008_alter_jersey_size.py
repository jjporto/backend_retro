# Generated by Django 5.1.3 on 2024-11-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_jersey_size_alter_jersey_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jersey',
            name='size',
            field=models.CharField(default='S M L XL 2XL 3XL 4XL', max_length=100),
        ),
    ]
