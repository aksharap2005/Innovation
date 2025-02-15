from django.db import models

class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.FloatField()
    currency = models.CharField(max_length=3, default="USD")  # Example: "USD", "INR"
    airline = models.CharField(max_length=100)
    departure_date = models.DateTimeField()  # Changed to DateTimeField

    def __str__(self):
        return f"{self.airline} - {self.origin} to {self.destination} ({self.price} {self.currency})"

    class Meta:
        verbose_name_plural = "Flights"


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price_per_night = models.FloatField()
    currency = models.CharField(max_length=3, default="USD")  # Example: "USD", "INR"
    rating = models.FloatField()
    check_in_date = models.DateField(null=True, blank=True)  # Optional
    check_out_date = models.DateField(null=True, blank=True)  # Optional

    def __str__(self):
        return f"{self.name} - {self.location} ({self.price_per_night} {self.currency})"

    class Meta:
        verbose_name_plural = "Hotels"
