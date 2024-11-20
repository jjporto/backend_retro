from django.db import models

class Jersey(models.Model):
    CATEGORY_CHOICES = [
        ('Retro', 'Camisetas Retro'),
        ('Camisetas2425', 'Camisetas 24/25'),
        ('Kids', 'Niños'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    imageUrl = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

