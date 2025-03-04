# Generated by Django 5.1.3 on 2024-11-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_jersey_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='jersey',
            name='size',
            field=models.CharField(default='S, M, L, XL, 2XL, 3XL, 4XL', max_length=100),
        ),
        migrations.AlterField(
            model_name='jersey',
            name='category',
            field=models.CharField(choices=[('Retro', 'Camisetas Retro'), ('Camisetas2425', 'Camisetas 24/25'), ('Kids', 'Niños')], max_length=20),
        ),
    ]
