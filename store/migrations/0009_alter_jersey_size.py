# Generated by Django 5.1.3 on 2024-11-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_jersey_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jersey',
            name='size',
            field=models.CharField(choices=[('XS XSS', 'XS XSS'), ('S M L XL 2XL 3XL 4XL', 'S M L XL 2XL 3XL 4XL')], max_length=100),
        ),
    ]
