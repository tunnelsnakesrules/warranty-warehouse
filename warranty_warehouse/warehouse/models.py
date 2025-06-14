from django.db import models

class Order(models.Model):
    number = models.CharField(max_length=50, unique=True)
    vin = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.number

class StorageLocation(models.Model):
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.code

class Part(models.Model):
    STATUS_CHOICES = [
        ('stored', 'На хранении'),
        ('disposed', 'Утилизировано'),
        ('returned', 'Отправлено производителю'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    storage_location = models.ForeignKey(StorageLocation, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='stored')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.part_number})"

class LogEntry(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
