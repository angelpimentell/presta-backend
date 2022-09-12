from django.db import models


class Loan(models.Model):
    client = models.ManyToManyField("users.User")
    payment_time = models.ManyToManyField("loans.Time")
    total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    due_amount = models.DecimalField(max_digits=9, decimal_places=2)
    interests = models.DecimalField(max_digits=3, decimal_places=2)
    fee_type = models.PositiveSmallIntegerField()
    start = models.DateField()
    finish = models.DateField(null=True)

