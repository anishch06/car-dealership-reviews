from django.db import models

class Dealer(models.Model):
    full_name = models.CharField(max_length=120)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    address = models.CharField(max_length=240, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    class Meta:
        ordering = ["id"]
    def __str__(self):
        return self.full_name

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=80)
    review = models.TextField()
    purchase = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.dealer.full_name} - {self.name}"
